import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
from lmfit import Model
from sklearn.metrics import r2_score
import os


h = ((os.path.dirname(os.path.abspath(__file__))).replace("\\","/")).replace("src","results/jpgs")


def figname(a):
    a = a.replace("\\","/")
    b = a.split("/")
    c = b[-1].split(".")
    d = c[0]
    e = h+"/"+d+".jpg"
    return e



# def eq(x, a, b, c, d, e):
#     return a * (x**4) + b * (x**3) + c * (x**2) + d * x + e
#
#
# def IV(x, q, w, alp, v = [], i = []):
#     polyfiti = np.polyfit(v, i, 12)
#     fiti = np.poly1d(polyfiti)
#     return abs(q*(np.exp(x/w)-1))+alp*fiti(x)


class grp():
    def __init__(self,v,i,wvl,itst,lgds,show,save,figname,fitting):
        self.v = v
        self.i = i
        self.wvl = wvl
        self.itst = itst
        self.lgds = lgds
        self.show = show
        self.save = save
        self.figname = figname
        self.fitting = fitting
    def grph(self):

        plt.figure(figsize = (12, 8))
        plt.subplot(2, 3, 4)
        plt.plot(self.v, self.i, 'o', label = 'I-V curve')
        plt.title("IV analysis")
        plt.xlabel("Voltage [V]")
        plt.ylabel("Current [A]")
        plt.yscale('logit')
        plt.legend(loc = 'best')

        plt.subplot(2,3,5)
        plt.plot(self.v, self.i, 'o', label = 'I-V curve')

        v1 = self.v[:10]
        v2 = self.v[9:]

        i1 = self.i[:10]
        i2 = self.i[9:]

        # start_time1 = time.time()
        lmodel = Model(self.fitting.eq)
        params1 = lmodel.make_params(a=1, b=1, c=1, d=1, e=1)
        result1 = lmodel.fit(i1, params1, x = v1)
        plt.plot(v1, result1.best_fit, '--', label = 'Fit-L')
        # # end_time1 = time.time()
        # # print(f'left fitting time : {end_time1 - start_time1}')

        # start_time2 = time.time()
        rmodel = Model(self.fitting.IV)
        # params2 = rmodel.make_params(Is=1, q=1, n=1, k=1)
        # result2 = rmodel.fit(i2, params2, x = v2)
        # params2 = rmodel.make_params(q=1, w=1, alp=1, v=v2, i=i2)
        result2 = rmodel.fit(i2, x=v2, q=1, w=1, alp=1, v=v2, i=i2)
        # result2 = rmodel.fit(i2, params2, x =v2)
        plt.plot(v2, result2.best_fit, '--', label = 'Fit-R')
        # end_time2 = time.time()
        # print(f'right fitting time : {end_time2 - start_time2}')

        plt.title("IV analysis")
        plt.xlabel("Voltage [V]")
        plt.ylabel("Current [A]")
        plt.yscale('logit')
        plt.legend(loc='best')


        plt.subplot(2, 3, 1)
        for n in range(len(self.wvl)):
            plt.title("Transmission spectra-as measured")
            plt.xlabel("Wavelength [nm]")
            plt.ylabel("Measured transmission [dB]")
            plt.rc("legend", fontsize=7)
            if n == 6:
                plt.plot(self.wvl[6], self.itst[6], label = 'DCBias = REF')
                plt.rc("legend", fontsize=5)
            else:
                plt.plot(self.wvl[n], self.itst[n], label = f'DCBias = {self.lgds[n]}V')
            plt.legend(loc = 'best', ncol = 3)

        # Fitting
        plt.subplot(2, 3, 2)
        for n in range(len(self.wvl)):
            if n == 6:
                plt.plot(self.wvl[n], self.itst[n], label="REF")
            else:
                continue
        for b in range(2,7):
            dp1 = np.polyfit(self.wvl[6], self.itst[6], b)
            f1 = np.poly1d(dp1)
            # ref_rsq = r2_score(self.itst[6], f1(self.wvl[6]))
            plt.plot(self.wvl[6], f1(self.wvl[6]), 'r--', label = f'{b} th R^2:{round(r2_score(self.itst[6], f1(self.wvl[6])),4)}')
            plt.rc("legend", fontsize=8)
            # print(f'I-IL R Squared {b}th : {r2_score((itst[6]),f1(wvl[6]))}') # 피팅 제곱의 값 즉, 1에 가까울 수록 정확하다.

        plt.xlabel('Wavelength[nm]')
        plt.ylabel('Transmissions[dB]')
        plt.title('Transmission spectra - fitted')
        plt.legend(loc='best')


        plt.subplot(2, 3, 3)
        for k in range(len(self.wvl)-1):
            plt.title("Fitting Function")
            plt.xlabel("Wavelength [nm]")
            plt.ylabel("Measured transmission [dB]")
            plt.plot(self.wvl[k], self.itst[k] - f1(self.wvl[k]), label = f'DCBias = {self.lgds[k]}V')
            plt.legend(loc = 'best', ncol = 3)
            plt.rc("legend", fontsize=5)
            # 각 DC Bias에서 빛의 세기의 최대값
            # print(f'Max intensity[dB] at DCBias = {lgds[k]} :{max(itst[k] - f1(wvl[k]))}')
            # # 빛의 세기가 최대일 때 파장
            # print(f'at {wvl[k][(np.argmax(itst[k] - f1(wvl[k])))]}nm')
            # # 각 DC Bias에서 빛의 세기의 최소값
            # print(f'Min intensity[dB] at DCBias = {lgds[k]} :{min(itst[k] - f1(wvl[k]))}')
            # # 빛의 세기가 최소일 때 파장
            # print(f'at {wvl[k][(np.argmin(itst[k] - f1(wvl[k])))]}nm')
        plt.tight_layout()
        if self.show == True:
            plt.show()
        if self.save == True:
            plt.savefig(self.figname, dpi=300, bbox_inches='tight')

    # def ref_rsq(self):
    #     dp1 = np.polyfit(self.wvl[6], self.itst[6], 4)
    #     f1 = np.poly1d(dp1)
    #     ref_rsq = r2_score(self.itst[6], f1(self.wvl[6]))
    #     return ref_rsq

    def ref_max(self):
        dp1 = np.polyfit(self.wvl[6], self.itst[6], 4)
        f1 = np.poly1d(dp1)
        ref_max = max(f1(self.wvl[6]))
        return ref_max

    # def IV_left_rsq(self):
    #     v1 = self.v[:10]
    #     i1 = self.i[:10]
    #     lmodel = Model(self.fitting.eq)
    #     params1 = lmodel.make_params(a=1, b=1, c=1, d=1, e=1)
    #     result1 = lmodel.fit(i1, params1, x=v1)
    #     IV_left_rsq = r2_score(i1, result1.best_fit)
    #     return IV_left_rsq
    #
    # def IV_right_rsq(self):
    #     v2 = self.v[9:]
    #     i2 = self.i[9:]
    #     rmodel = Model(self.fitting.IV)
    #     result2 = rmodel.fit(i2, x=v2, q=1, w=1, alp=1, v=v2, i=i2)
    #     IV_right_rsq = r2_score(i2, result2.best_fit)
    #     return IV_right_rsq
    # def IV_rsq(self):
    #     rmodel = Model(IVf)
    #     result2 = rmodel.fit(self.i, x=self.v, q=1, w=1, alp=1, v=self.v, i=self.i)
    #     IV_rsq = r2_score(self.i,result2.best_fit)
    #     return IV_rsq



# print(f'max :{max(itst[k]-f1(wvl[k]))}')


# fit1i = result1.best_fit
# fit2i = result2.best_fit
# h = [-2.0,-1.5,-1,-0.5,0.0]
# for t in range(len(fiti)):
#     print(f'{}: {fiti[t]}')

# # 좌측 best_fit일 때의 parameters 값
# print(f'Left best Parameters: {result1.best_values}')
# # 좌측 best_fit일 때의 Current 값들
# print(f'Left best Currents[A]: {fit1i}')
# # 우측 best_fit일 때의 parameters 값
# print(f'Right best Parameters: {result2.best_values}')
# # 우측 best_fit일 때의 Current 값들
# print(f'Right best Currents[A]: {fit2i}')







