import os
import xml.etree.ElementTree as ET
import numpy as np

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)


batch = input("Batch: ")
wfer = input("Wafer: ")
drow = input("DoeRow: ")
dcol = input("DieColumn: ")
mset = input("Maskset: ")
tsite = input("TestSite: ")

fname = batch+"_"+wfer+"_("+drow+","+dcol+")_"+mset+"_"+tsite+".xml"
print(fname)

fpath = findfile(fname,"/")

print(fpath)


a = fpath.replace("\\","/")
print(a)

tree = ET.parse(a)
root = tree.getroot()

def spfl(a):    # spfl 함수 정의
    sp = a.text.split(',')  # ,를 기준으로 나누고 값 가져오기
    fl = list(map(float, sp))   # 가져온 값을 실수로 바꾸고 리스트에 넣기
    return fl   # fl 반환

for data in root.iter('Voltage'):
    vlt = spfl(data)  # 'Voltage'안에 있는 값을 spfl함수를 사용해 v에 저장

print(vlt)