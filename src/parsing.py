import xml.etree.ElementTree as ET
import numpy as np

def parse():
    tree = ET.parse()
    root = tree.getroot()

def spfl(a):    # spfl 함수 정의
    sp = a.text.split(',')  # ,를 기준으로 나누고 값 가져오기
    fl = list(map(float, sp))   # 가져온 값을 실수로 바꾸고 리스트에 넣기
    return fl   # fl 반환

# 3차
# I-V Graph
for data in root.iter('Voltage'):
    vlt = spfl(data)  # 'Voltage'안에 있는 값을 spfl함수를 사용해 v에 저장
    v = np.array(vlt)
for data in root.iter('Current'):
    crt1 = spfl(data)
    crt = list(map(abs, spfl(data)))  #'Current'안에 있는 값을 spfl함수를 사용하고, 절댓값을 사용해 리스트 안에 넣어
    i = np.array(crt)

# Raw data
wvl = []
itst = []
for data in root.iter('L'):
    L = spfl(data)
    wvl.append(L)
for data in root.iter('IL'):
    IL = spfl(data)
    itst.append(IL)

lgds = []
for data in root.iter("WavelengthSweep"):
    lgds.append(data.get("DCBias"))