from src import csv_maker, filter, graph, parsing, get_start,fitting, rsq
import time as t
start = t.time()

'''Enter the Lot_id of the file you want to find'''
Lot_id = []

'''Enter the Wafer_id of the file you want to find'''
Wafer_id = []

'''Enter the matrix of files you want to find. ex) (0,0),(0,1)...'''
xy_coord = []

'''Enter the maskset of the file you want to find'''
Mask_set = []

'''Enter the devive_name of the file you want to find'''
device_name =[]

'''Enter 'True' if you want to save the graph, 'False' otherwise'''
Opt_savefig = False

'''Enter 'True' if you want to see the graph, 'False' otherwise'''
Opt_showfig = False

a = filter.cmp(Lot_id,Wafer_id,xy_coord,Mask_set,device_name)
b = get_start.run2u(filter,parsing,graph,csv_maker,Opt_showfig,Opt_savefig,fitting,rsq)
get_start.err(a,b)
end = t.time()
get_start.runtime(start,end)
