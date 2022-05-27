
import os

from pathlib import Path

def num(c):
    for i in range(len(c)):
        if c[0] == '':
            del c[0]
    if len(c) == 0:
        c.append("_")





#wafer리스트
wafer = []
#data리스트
date = []
#data리스트


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

# dat 디렉토리의 하위 디렉토리를 찾아 wafer리스트에 append
search(h,wafer)

# wafer리스트 각 요소들의 하위 디렉터리를 찾아 date디렉토리에 append
for i in range(len(wafer)):
    if not ".gitkeep" in wafer[i]:
        search(wafer[i],date)


fname = []
dlst = []
# def cmp(a,b,c,d,e):
class cmp():
    def __init__(self,a,b,c,d,e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        clst = [self.a, self.b, self.c, self.d, self.e]
        for hu in range(len(clst)-1):
            num(clst[hu])
        if len(self.e) == 0:
            self.e.append("LMZ")
        for fst in range(len(self.a)):
            for scd in range(len(self.b)):
                for trd in range(len(self.c)):
                    for fth in range(len(self.d)):
                        for fith in range(len(self.e)):
                            fname.append(f"*{self.a[fst]}*{self.b[scd]}*{self.c[trd]}*{self.d[fth]}*{self.e[fith]}*")
        for t in range(len(fname)):
            for i in range(len(date)):
                ph = Path(date[i]).resolve()
                for ret in ph.glob(fname[t]):
                    dlst.append(ret)

        # return dlst


# '''찾고 싶은 파일의 Lot_id를 입력하세요.'''
# Lot_id = ['HY202103']
#
# '''찾고 싶은 파일의 Wafer_id를 입력하세요.'''
# Wafer_id = ['D07']
#
# '''찾고 싶은 파일의 행렬을 입력하세요. ex) [0,0]'''
# xy_coord = ['(0,0)','(0,-1)']
#
# '''찾고 싶은 파일의 maskset을 입력하세요.'''
# Mask_set = ['LION1']
#
# '''찾고 싶은 파일의 devive_name을 입력하세요.'''
# device_name =['LMZ']
#
# print(cmp(Lot_id,Wafer_id,xy_coord,Mask_set,device_name))


