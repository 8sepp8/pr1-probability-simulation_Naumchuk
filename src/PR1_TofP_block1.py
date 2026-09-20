import matplotlib.pyplot as mb
import random as r
import os

P_true = 0.3
N_list = [10,100,1000,10000,100000,1000000]
frequency = []

print(45*'-')
print(10*'=','БЛОК 1.Прості події та перевірка ЗВЧ',10*'=')
print(f'Теоретична ймовірність P(A) = {P_true}')
print(f"{'N':<10} | {'W(A)':<15} | {'похибка ':<15}")
print(45*'-')

for n in N_list:
    M = sum(1 for i in range(n) if r.random() < P_true)
    wa = M / n
    frequency.append(wa)
    delta  = abs(wa - P_true)

    print(f"{n:<10} | {wa:<15.5f} | {delta:<15.5f}")

os.makedirs('graphics', exist_ok = True)
mb.plot(N_list, frequency, marker = 'o', label = 'Статистична частота')
mb.axhline (y = P_true, color = 'g', linestyle = '--', label = 'Теоретична ймовірність')
mb.xscale('log')
mb.xlabel('N(логарифмічна шкала)')
mb.ylabel('Частота W(A)')
mb.legend()
mb.grid(True, linestyle = '--')
mb.savefig('graphics/block1_plot.png')
mb.show()
