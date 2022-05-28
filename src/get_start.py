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
            t = c.grp(aa, bb, cc, dd, ee, f, g, ff,fit)
            t.grph()
            d.csv(a.dlst[i], t, b,data,rsq,fit)
        d.all_csv(data)
        print(f'Analysis of {len(a.dlst)} files completed successfully. \nThank you.')

# print(str(filter.dlst[0]))
# for i in range(len(filter.dlst)):
#     warnings.filterwarnings('ignore')
#     a = parsing.v(filter.dlst[i])
#     b = parsing.i(filter.dlst[i])
#     c = parsing.wvl(filter.dlst[i])
#     d = parsing.itst(filter.dlst[i])
#     e = parsing.lgds(filter.dlst[i])
#     f = graph.figname(str(filter.dlst[i]))
#     print(filter.dlst[i])
#     t = graph.grp(a,b,c,d,e,Opt_showfig,Opt_savefig,f)
#     t.grph()
#     cs = csv_maker.csv(filter.dlst[i], csv_maker.csvname(str(filter.dlst[i])), t, parsing)


class err():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        try:
            self.a
            self.b
        except Exception as e:
            print(f"오류:{e}! <입력하신 값들을 다시 한번 확인 해주세요>")

def runtime(a,b):
    print(f'Run time: {b-a}[s]')