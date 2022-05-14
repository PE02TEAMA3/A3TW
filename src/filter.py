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

row = (0)
col = (0)

# date디렉토리 하위의 파일들 중 ''문자가 포함된 파일들을 찾아 dlst에 append
for i in range(len(date)):
    ph = Path(date[i]).resolve()
    for ret in ph.glob(f"*({row},{col})*LMZC*") :
     dlst.append(ret)

print(dlst)
print(len(dlst))

tree = ET.parse(dlst[0])
root = tree.getroot()