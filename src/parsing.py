import xml.etree.ElementTree as ET
import numpy as np




# tree = ET.parse('C:/Users/user/PycharmProjects/A3TW_YS/dat/D07/20190715_190855/HY202103_D07_(0,0)_LION1_DCM_LMZC.xml')
# root = tree.getroot()


def spfl(a):    # spfl 함수 정의
    sp = a.text.split(',')  # ,를 기준으로 나누고 값 가져오기
    fl = list(map(float, sp))   # 가져온 값을 실수로 바꾸고 리스트에 넣기
    return fl   # fl 반환



def v(a):
    tree = ET.parse(a)
    root = tree.getroot()
    for data in root.iter('Voltage'):
        vlt = spfl(data)  # 'Voltage'안에 있는 값을 spfl함수를 사용해 v에 저장
        v = np.array(vlt)
    return v

def i(a):
    tree = ET.parse(a)
    root = tree.getroot()
    for data in root.iter('Current'):
        crt1 = spfl(data)
        crt = list(map(abs, spfl(data)))  # 'Current'안에 있는 값을 spfl함수를 사용하고, 절댓값을 사용해 리스트 안에 넣어
        i = np.array(crt)
    return i

def wvl(a):
    tree = ET.parse(a)
    root = tree.getroot()
    wvl = []
    for data in root.iter('L'):
        L = spfl(data)
        wvl.append(L)
    return wvl

def itst(a):
    tree = ET.parse(a)
    root = tree.getroot()
    itst = []
    for data in root.iter('IL'):
        IL = spfl(data)
        itst.append(IL)
    return itst

def lgds(a):
    tree = ET.parse(a)
    root = tree.getroot()
    lgds = []
    for data in root.iter("WavelengthSweep"):
        lgds.append(data.get("DCBias"))
    return lgds

# # plt.subplot(2, 3, 1)
# for n in range(len(wvl)):
#     # plt.title("Transmission spectra-as measured")
#     # plt.xlabel("Wavelength [nm]")
#     # plt.ylabel("Measured transmission [dB]")
#     # plt.rc("legend", fontsize=7)
#     if n == 6:
#         plt.plot(wvl[6], itst[6], label = 'DCBias = REF')
#     else:
#         plt.plot(wvl[n], itst[n], label = f'DCBias = {lgds[n]}V')
#     plt.legend(loc = 'best', ncol = 3)

