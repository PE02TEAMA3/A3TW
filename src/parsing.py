import xml.etree.ElementTree as ET
import numpy as np


def spfl(a):
    sp = a.text.split(',')  # ,를 기준으로 나누고 값 가져오기
    fl = list(map(float, sp))   # 가져온 값을 실수로 바꾸고 리스트에 넣기
    return fl   # fl 반환

def v(a):
    root = ET.parse(a).getroot()
    for data in root.iter('Voltage'):
        vlt = spfl(data)
        v = np.array(vlt)
    return v

def vlt(a):
    tree = ET.parse(a)
    root = tree.getroot()
    for data in root.iter('Voltage'):
        vlt = spfl(data)
    return vlt

def crt1(a):
    tree = ET.parse(a)
    root = tree.getroot()
    for data in root.iter('Current'):
        crt1 = spfl(data)
    return crt1

def i(a):
    root = ET.parse(a).getroot()
    for data in root.iter('Current'):
        crt = list(map(abs, spfl(data)))
        i = np.array(crt)
    return i

def wvl(a):
    root = ET.parse(a).getroot()
    wvl = []
    for data in root.iter('L'):
        L = spfl(data)
        wvl.append(L)
    return wvl

def itst(a):
    root = ET.parse(a).getroot()
    itst = []
    for data in root.iter('IL'):
        IL = spfl(data)
        itst.append(IL)
    return itst

def lgds(a):
    root = ET.parse(a).getroot()
    lgds = []
    for data in root.iter("WavelengthSweep"):
        lgds.append(data.get("DCBias"))
    return lgds