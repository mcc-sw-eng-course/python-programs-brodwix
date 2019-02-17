# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:42:40 2019

@author: Bruno Vergaray
"""

import csv
import numpy


def L1E8(filename):
    raw_data = open(filename, 'rt')
    reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
    x = list(reader)
    data = numpy.array(x).astype('float')
    A = numpy.reshape(data, -1)

    # suma de todos los elementos de la matriz
    my_list = data.sum()
    dim = data.shape
    n = len(A)

    # Sample mean
    smean = my_list / n

    # Sample standard deviation
    step2 = data - smean
    step3 = step2 * step2
    step4 = step3.sum()
    step5 = step4 / n
    step6 = step5 ** 0.5
    # print('Sample standard deviation = ',step6)

    # Median
    Amed = numpy.median(A)
    # print('median = ', Amed)

    # n-quartil
    nquartil = numpy.percentile(A, [25, 50, 75])
    # print('Q1, Q2, Q3 = ',nquartil)

    return my_list, A, smean, step6, Amed, nquartil


def n_percentil(filename):
    sw = 0
    a = L1E8(filename);

    while sw == 0:
        print('Ingrese un valor percentil :')
        K = input()
        intK = int(K)
        if 1 < intK < 100:
            p = numpy.percentile(a[1], intK)
            print(f"el percentil {intK} = {p}")
            sw = 1
        else:
            print('Ingrese valores entre 1 y 100')
