import sys
import os
import xml.etree.ElementTree as ET
from pathlib import Path


#wafer리스트
wafer = []
#data리스트
date = []
#data리스트
dlst = []

#디렉토리 이름을 넣으면 그 하위 디렉토리 경로를 a 리스트에 append
def search(dirname,a):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        a.append(full_filename)

#파일 이름을 넣으면 절대경로를 보여줌
def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename :
            return os.path.join(dirpath, name)

#현재 파일의 경로를 찾아 dat경로로 위치 변경
h = ((os.path.dirname(os.path.abspath(__file__))).replace("\\","/")).replace("src","dat")

print(h)

# dat 디렉토리의 하위 디렉토리를 찾아 wafer리스트에 append
search(h,wafer)
# search('/dat',b)
print(wafer)

# wafer리스트 각 요소들의 하위 디렉터리를 찾아 date디렉토리에 append
for i in range(len(wafer)):
    search(wafer[i],date)
print(date)
print("--"*10+"프로그램 시작"+"--"*10)
print("찾고자 하는 요소들의 이름을 입력하세요.")
print("모든 요소를 찾고 싶다면 all 입력")
batch = input("Batch: ")
wfer = input("Wafer: ")
drow = input("DieRow: ")
dcol = input("DieColumn: ")
mset = input("Maskset: ")
tsite = input("TestSite: ")

if tsite == "all":
    tsite = "LMZ"
if not drow == "all":
    drow = "(" + drow
if not dcol == "all":
    dcol = dcol + ")"

cmps = [batch, wfer, drow, dcol, mset, tsite]
shnm = []

# sech = "*"+batch+
for i in range(len(cmps)):
    if cmps[i] == 'all':
        shnm.append("")
    else:
        shnm.append(cmps[i])
print(shnm)

a = "*"
for i in range(len(cmps)):
    if not cmps[i] == 'all':
        a += cmps[i] + "*"
print(f"a: {a}")

# date디렉토리 하위의 파일들 중 입력받은 문자가 포함된 파일들을 찾아 dlst에 append
for i in range(len(date)):
    ph = Path(date[i]).resolve()
    for ret in ph.glob(a) :
     dlst.append(ret)

for i in range(len(dlst)):
    print(dlst[i])

print(len(dlst))
def spfl(a):    # spfl 함수 정의
    sp = a.text.split(',')  # ,를 기준으로 나누고 값 가져오기
    fl = list(map(float, sp))   # 가져온 값을 실수로 바꾸고 리스트에 넣기
    return fl   # fl 반환

for i in range(len(dlst)):
    tree = ET.parse(dlst[i])
    root = tree.getroot()
    for data in root.iter('Voltage'):
        vlt = spfl(data)  # 'Voltage'안에 있는 값을 spfl함수를 사용해 v에 저장
    print(vlt)


# Batch = []
# wafer = ['D06','D07']
# xy_coord = []
# maskset = []
# device = ['LMZ']