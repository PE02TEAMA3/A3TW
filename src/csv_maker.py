# import pandas as pd
# import sys
# import os
# from pathlib import Path
# import xml.etree.ElementTree as ET
#
# h = ((os.path.dirname(os.path.abspath(__file__))).replace("\\","/")).replace("src","results/csvs")
#
# def csvname(a):
#     a = a.replace("\\","/")
#     b = a.split("/")
#     c = b[-1].split(".")
#     d = c[0]
#     e = h+"/"+d+".csv"
#     return e
#
# class csv():
#     def __init__(self,a,b,g,p):
#         self.a = a
#         self.b = b
#         tree = ET.parse(self.a)
#         root = tree.getroot()
#         columns = ['Lot', 'Wafer', 'Mask', 'TestSite', 'Name', 'Date', 'Script Owner', 'Operator', 'Row', 'Column', 'ErrorFlag', 'Error description', 'Analysis Wavelength', 'Rsq of Ref. spectrum (Nth)', 'Max transmission of Ref. spec. (dB)', 'Rsq of Left IV','Rsq of right IV', 'I at -1V [A]', 'I at 1V[A]']
#         # 'Script ID', 'Script Version'
#         data = []
#         values = []
#
#         TestSiteInfo = root.find('TestSiteInfo').attrib
#         values.append(TestSiteInfo['Batch'])
#         values.append(TestSiteInfo['Wafer'])
#         values.append(TestSiteInfo['Maskset'])
#         values.append(TestSiteInfo['TestSite'])
#         DeviceInfo = root.find('.//DeviceInfo')
#         values.append(DeviceInfo.attrib['Name'])
#         PortCombo = root.find('.//PortCombo')
#         values.append(PortCombo.attrib['DateStamp'])
#         values.append('A3')
#         ModulatorSite = root.find('.//ModulatorSite')
#         values.append(ModulatorSite.attrib['Operator'])
#         values.append(TestSiteInfo['DieRow'])
#         values.append(TestSiteInfo['DieColumn'])
#         values.append('0')
#         values.append('No Error')
#         # wl = root[6][0][0][1][0][1]
#         # values.append(wl.text)
#         values.append(root.find(".//DesignParameter[@Name='Design wavelength']").text)
#         values.append(round(g.ref_rsq(), 4))  # ref rsq
#         values.append(g.ref_max()) # ref max
#         values.append(g.IV_left_rsq()) # rsq left
#         values.append(g.IV_right_rsq()) # rsq right
#         index1 = p.vlt(self.a).index(-1)    # voltage -1V 인덱스 구하기
#         index2 = p.vlt(self.a).index(1)     # voltage -V 인덱스 구하기
#         values.append(p.crt1(self.a)[index1]) # I at -1V
#         values.append(p.crt1(self.a)[index2]) # I at 1V
#         # print(values)
#
#         data.append(values)
#         df = pd.DataFrame(data, columns=columns).set_index('Lot')
#         # print(df)
#
#         df.to_csv(self.b, mode = 'w')

import pandas as pd
import sys
import os
from pathlib import Path
import xml.etree.ElementTree as ET

h = ((os.path.dirname(os.path.abspath(__file__))).replace("\\","/")).replace("src","results/csvs")

# def csvname(a):
#     a = a.replace("\\","/")
#     b = a.split("/")
#     c = b[-1].split(".")
#     d = c[0]
#     e = h+"/"+d+".csv"
#     return e

# class csv():
#     def __init__(self,a,b,g,p):
#         self.a = a
#         self.b = b
#         tree = ET.parse(self.a)
#         root = tree.getroot()
#         columns = ['Lot', 'Wafer', 'Mask', 'TestSite', 'Name', 'Date', 'Script Owner', 'Operator', 'Row', 'Column', 'ErrorFlag', 'Error description', 'Analysis Wavelength', 'Rsq of Ref. spectrum (Nth)', 'Max transmission of Ref. spec. (dB)', 'Rsq of Left IV','Rsq of right IV', 'I at -1V [A]', 'I at 1V[A]']
#         # 'Script ID', 'Script Version'
#         data = []
#         values = []
#
#         TestSiteInfo = root.find('TestSiteInfo').attrib
#         values.append(TestSiteInfo['Batch'])
#         values.append(TestSiteInfo['Wafer'])
#         values.append(TestSiteInfo['Maskset'])
#         values.append(TestSiteInfo['TestSite'])
#         DeviceInfo = root.find('.//DeviceInfo')
#         values.append(DeviceInfo.attrib['Name'])
#         PortCombo = root.find('.//PortCombo')
#         values.append(PortCombo.attrib['DateStamp'])
#         values.append('A3')
#         ModulatorSite = root.find('.//ModulatorSite')
#         values.append(ModulatorSite.attrib['Operator'])
#         values.append(TestSiteInfo['DieRow'])
#         values.append(TestSiteInfo['DieColumn'])
#         Error_code = []
#         Error_name = []
#         if round(g.ref_rsq(),4) <= 0.996 :
#             Error_code.append('1')
#             Error_name.append('Ref.spec.Error')
#         if g.IV_left_rsq() <= 0.996:
#             Error_code.append('2')
#             Error_name.append('Rsq.left.Error')
#         if g.IV_left_rsq() <= 0.996:
#             Error_code.append('3')
#             Error_name.append('Rsq.right.Error')
#         if len(Error_code) == 0 :
#             Error_code.append('0')
#             Error_name.append('No Error')
#
#         values.append(''.join(Error_code))
#         values.append(''.join(Error_name))
#
#         values.append(root.find(".//DesignParameter[@Name='Design wavelength']").text)
#         values.append(round(g.ref_rsq(), 4))  # ref rsq
#         values.append(g.ref_max()) # ref max
#         values.append(g.IV_left_rsq()) # rsq left
#         values.append(g.IV_right_rsq()) # rsq right
#         index1 = p.vlt(self.a).index(-1)    # voltage -1V 인덱스 구하기
#         index2 = p.vlt(self.a).index(1)     # voltage -V 인덱스 구하기
#         values.append(p.crt1(self.a)[index1]) # I at -1V
#         values.append(p.crt1(self.a)[index2]) # I at 1V
#         # print(values)
#
#         data.append(values)
#         df = pd.DataFrame(data, columns=columns).set_index('Lot')
#         #print(df)
#
#         df.to_csv(self.b, mode = 'w')


class csv():
    def __init__(self,a,g,p,data):
        self.a = a
        # self.b = b
        # columns = ['Lot', 'Wafer', 'Mask', 'TestSite', 'Name', 'Date', 'Script Owner', 'Operator',
        #            'Row', 'Column', 'ErrorFlag', 'Error description',
        #            'Analysis Wavelength', 'Rsq of Ref. spectrum (Nth)', 'Max transmission of Ref. spec. (dB)',
        #            'Rsq of Left IV', 'Rsq of right IV', 'I at -1V [A]', 'I at 1V[A]']

        tree = ET.parse(self.a)
        root = tree.getroot()
        # 'Script ID', 'Script Version'
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
        if round(g.ref_rsq(),4) <= 0.996 :
            Error_code.append('1')
            Error_name.append('Ref.spec.Error')
        if g.IV_left_rsq() <= 0.996:
            Error_code.append('2')
            Error_name.append('Rsq.left.Error')
        if g.IV_left_rsq() <= 0.996:
            Error_code.append('3')
            Error_name.append('Rsq.right.Error')
        if len(Error_code) == 0 :
            Error_code.append('0')
            Error_name.append('No Error')

        values.append(','.join(Error_code))
        values.append(','.join(Error_name))

        values.append(root.find(".//DesignParameter[@Name='Design wavelength']").text)
        values.append(round(g.ref_rsq(), 4))  # ref rsq
        values.append(g.ref_max()) # ref max
        values.append(g.IV_left_rsq()) # rsq left
        values.append(g.IV_right_rsq()) # rsq right
        index1 = p.vlt(self.a).index(-1)    # voltage -1V 인덱스 구하기
        index2 = p.vlt(self.a).index(1)     # voltage -V 인덱스 구하기
        values.append(p.crt1(self.a)[index1]) # I at -1V
        values.append(p.crt1(self.a)[index2]) # I at 1V
        data.append(values)

        # df = pd.DataFrame(data, columns=columns).set_index('Lot')
        #print(df)

        # df.to_csv(self.b, mode = 'w')

class all_csv():
    def __init__(self,a):
        self.a = a
        columns = ['Lot', 'Wafer', 'Mask', 'TestSite', 'Name', 'Date', 'Script Owner', 'Operator',
                   'Row', 'Column', 'ErrorFlag', 'Error description',
                   'Analysis Wavelength', 'Rsq of Ref. spectrum (Nth)', 'Max transmission of Ref. spec. (dB)',
                   'Rsq of Left IV', 'Rsq of right IV', 'I at -1V [A]', 'I at 1V[A]']
        df = pd.DataFrame(self.a, columns=columns).set_index('Lot')
        df.to_csv(h+"/"+"AnalysisResult_A3"+".csv", mode= 'w')