from src import csv_maker, filter, graph, parsing, get_start
import time as t
start = t.time()

'''찾고 싶은 파일의 Lot_id를 입력하세요.'''
Lot_id = []

'''찾고 싶은 파일의 Wafer_id를 입력하세요.'''
Wafer_id = [""]

'''찾고 싶은 파일의 행렬을 입력하세요. ex) (0,0),'''
xy_coord = ["(0,2)"]

'''찾고 싶은 파일의 maskset을 입력하세요.'''
Mask_set = []

'''찾고 싶은 파일의 devive_name을 입력하세요.'''
device_name =[]

'''그래프를 저장하고 싶다면 True, 저장하고 싶지 않다면 False를 입력하세요.'''
Opt_savefig = True

'''그래프를 보고 싶다면 True, 보고 싶지 않다면 False를 입력하세요.'''
Opt_showfig = False

a = filter.cmp(Lot_id,Wafer_id,xy_coord,Mask_set,device_name)
b = get_start.run2u(filter,parsing,graph,csv_maker,Opt_showfig,Opt_savefig)
get_start.err(a,b)
end = t.time()
get_start.runtime(start,end)