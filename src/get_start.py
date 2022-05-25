import warnings
def run2u(a,b,c,d,f,g):
    print('안녕하세요')
    for i in range(len(a.dlst)):
        warnings.filterwarnings('ignore')
        aa = b.v(a.dlst[i])
        bb = b.i(a.dlst[i])
        cc = b.wvl(a.dlst[i])
        dd = b.itst(a.dlst[i])
        ee = b.lgds(a.dlst[i])
        ff = c.figname(str(a.dlst[i]))
        print(a.dlst[i])
        t = c.grp(aa, bb, cc, dd, ee, f, g, ff)
        t.grph()
        d.csv(a.dlst[i], d.csvname(str(a.dlst[i])), t, b)
    print('분석이 완료되었습니다. 이용해 주셔서 감사합니다.')