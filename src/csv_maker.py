import pandas as pd
import os
import xml.etree.ElementTree as ET

h = ((os.path.dirname(os.path.abspath(__file__))).replace("\\","/")).replace("src","results/csvs")

class csv():
    def __init__(self,a,g,p,data,rsq,fit):
        self.a = a
        tree = ET.parse(self.a)
        root = tree.getroot()
        values = []

        TestSiteInfo = root.find('TestSiteInfo').attrib
        values.append(TestSiteInfo['Batch'])
        values.append(TestSiteInfo['Wafer'])
        values.append(TestSiteInfo['Maskset'])
        values.append(TestSiteInfo['TestSite'])
        DeviceInfo = root.find('.//DeviceInfo')
        values.append(DeviceInfo.attrib['Name'])
        PortCombo = root.find('.//PortCombo')
        values.append(PortCombo.attrib['DateStamp'])
        values.append('A3')
        ModulatorSite = root.find('.//ModulatorSite')
        values.append(ModulatorSite.attrib['Operator'])
        values.append(TestSiteInfo['DieRow'])
        values.append(TestSiteInfo['DieColumn'])

        Error_code = []
        Error_name = []
        if round(rsq.ref_rsq(p,a),4) <= 0.96 :
            Error_code.append('1')
            Error_name.append('Ref.spec.Error')
        if rsq.IV_left_rsq(p,fit,a) <= 0.96:
            Error_code.append('2')
            Error_name.append('Rsq.left.Error')
        if rsq.IV_right_rsq(p,fit,a) <= 0.96:
            Error_code.append('3')
            Error_name.append('Rsq.right.Error')

        if len(Error_code) == 0 :
            Error_code.append('0')
            Error_name.append('No Error')

        values.append(','.join(Error_code))
        values.append(','.join(Error_name))

        values.append(root.find(".//DesignParameter[@Name='Design wavelength']").text)
        values.append(round(rsq.ref_rsq(p,a), 4))  # ref rsq
        values.append(g.ref_max()) # ref max
        values.append(rsq.IV_left_rsq(p,fit,a)) # rsq left
        values.append(rsq.IV_right_rsq(p,fit,a)) # rsq right
        index1 = p.vlt(self.a).index(-1)    # voltage -1V 인덱스 구하기
        index2 = p.vlt(self.a).index(1)     # voltage -V 인덱스 구하기
        values.append(p.crt1(self.a)[index1]) # I at -1V
        values.append(p.crt1(self.a)[index2]) # I at 1V
        data.append(values)


class all_csv():
    def __init__(self,a):
        self.a = a
        columns = ['Lot', 'Wafer', 'Mask', 'TestSite', 'Name', 'Date', 'Script Owner', 'Operator',
                   'Row', 'Column', 'ErrorFlag', 'Error description',
                   'Analysis Wavelength', 'Rsq of Ref. spectrum (Nth)', 'Max transmission of Ref. spec. (dB)',
                   'Rsq of Left IV', 'Rsq of right IV', 'I at -1V [A]', 'I at 1V[A]']
        df = pd.DataFrame(self.a, columns=columns).set_index('Lot')
        df.to_csv(h+"/"+"AnalysisResult_A3"+".csv", mode= 'w')