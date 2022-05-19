import sys
sys.path.append('[C://src]')
from src import filter

Lot_id = []
Wafer_id = []
xy_coord = ["(0,0)","(0,-1)"]
Mask_set = []
device_name =['LMZ']
Opt_savefig = True
Opt_showfig = True

a = [Lot_id, Wafer_id,xy_coord, Mask_set, device_name]
b = []

def num(c):
    if len(c) == 0:
        b.append(1)
    else:
        b.append(len(c))

for c in range(len(a)):
    num(a[c])

# for a in range(len[b]):
#     for a in range():


