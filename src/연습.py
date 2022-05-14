

#
# import xml.etree.ElementTree as ET
# import matplotlib.pyplot as plt
# import numpy as np
# from numpy import exp
# from lmfit import Model
# from sklearn.metrics import r2_score
# import time
#
# tree = ET.parse('C:/Users/user/PycharmProjects/A3TW_YS/dat/D07/20190715_190855/HY202103_D07_(0,0)_LION1_DCM_LMZC.xml')
#
# root = tree.getroot()
#
# def spfl(a):    # spfl 함수 정의
#     sp = a.text.split(',')  # ,를 기준으로 나누고 값 가져오기
#     fl = list(map(float, sp))   # 가져온 값을 실수로 바꾸고 리스트에 넣기
#     return fl   # fl 반환
#
# def IV(x, Is, q, n, k):
#     return Is * (exp((q * x) / (n * k)) - 1)
# # 0.026은 이론값, 내가 변수로 설정해서 리스트 1~100
# def eq(x, a, b, c, d, e):
#     return a * (x**4) + b * (x**3) + c * (x**2) + d * x + e
#
# for data in root.iter('Voltage'):
#     vlt = spfl(data)  # 'Voltage'안에 있는 값을 spfl함수를 사용해 v에 저장
#     v = np.array(vlt)
# for data in root.iter('Current'):
#     crt = list(map(abs, spfl(data)))  #'Current'안에 있는 값을 spfl함수를 사용하고, 절댓값을 사용해 리스트 안에 넣어
#     i = np.array(crt)