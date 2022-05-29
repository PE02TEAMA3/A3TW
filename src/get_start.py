import warnings
import time as t

def run2u(a,b,c,d,f,g,fit,rsq):
    print('Hello')
    if len(a.dlst) == 0:
        print("No file exists matching the input values.")
    else:
        data = []
        for i in range(len(a.dlst)):
            warnings.filterwarnings('ignore')
            aa = b.v(a.dlst[i])
            bb = b.i(a.dlst[i])
            cc = b.wvl(a.dlst[i])
            dd = b.itst(a.dlst[i])
            ee = b.lgds(a.dlst[i])
            ff = c.figname(str(a.dlst[i]))
            print(a.dlst[i])
            t = c.grp(aa, bb, cc, dd, ee, f, g, ff, fit)
            t.grph()
            d.csv(a.dlst[i], t, b,data,rsq,fit)
        d.all_csv(data)
        print(f'Analysis of {len(a.dlst)} files completed successfully. \nThank you.')

class err():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        try:
            self.a
            self.b
        except Exception as e:
            print(f"ERROR:{e}! <Please check the entered value again.>")

def runtime(a,b):
    print(f'Run time: {b-a}[s]')