# import sys
# sys.path.append('[C:/Users/user/PycharmProjects/A3TW_YS/src/filter.py]')
# from src import filter

batch = []
wfer = ["D07","D08"]
drow = ["(0,0)","(0,1)"]
dcol = []
mset = []
tsite = []

for i in range(len(wfer)):
    for t in range(len(drow)):
      print(f"{wfer[i]}+{drow[t]}")
