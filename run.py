import sys
import os
from src import filter

'''찾고 싶은 파일의 Lot_id를 입력하세요.'''
Lot_id = ['HY202103']

'''찾고 싶은 파일의 Wafer_id를 입력하세요.'''
Wafer_id = ['D07']

'''찾고 싶은 파일의 행렬을 입력하세요. ex) [0,0]'''
xy_coord = ['(0,0)']

'''찾고 싶은 파일의 maskset을 입력하세요.'''
Mask_set = ['LION1']

'''찾고 싶은 파일의 devive_name을 입력하세요.'''
device_name =['LMZ']

'''그래프를 저장하고 싶다면 True, 저장하고 싶지 않다면 False를 입력하세요.'''
Opt_savefig = True

'''그래프를 보고 싶다면 True, 보고 싶지 않다면 False를 입력하세요.'''
Opt_showfig = True

a = [Lot_id, Wafer_id,xy_coord, Mask_set, device_name]

def num(c):
    if len(c) == 0:
        c.append("_")

for c in range(len(a)):
    num(a[c])
    print(a[c])

fname = []
for fst in range(len(Lot_id)):
    for scd in range(len(Wafer_id)):
        for trd in range(len(xy_coord)):
            for fth in range(len(Mask_set)):
                for fith in range(len(device_name)):
                    fname.append(f"*{Lot_id[fst]}*{Wafer_id[scd]}*{xy_coord[trd]}*{Mask_set[fth]}*{device_name[fith]}")
print(fname)
