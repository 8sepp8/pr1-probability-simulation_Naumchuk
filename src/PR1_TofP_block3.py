import random as r
import math
import matplotlib.pyplot as mb
import os

print(10*'=',"БЛОК 3. Метод Монте-Карло",10*'=')
print(f"Точне значення 𝝿 = {math.pi:.5f}")
print(f"{'N':<10} | {'Оцінка пі':<15} | {'Похибка Δ':<15}")
print("-" * 45)

N_list = [10, 100, 1000, 10000, 100000, 1000000]
pi = []

for N in N_list:
    M = 0
    for _ in range(N):
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)
        if x**2 + y**2 <= 1: # Перевірка влучання точки у вписане коло
            M += 1
            
    pi_approx = 4 * M / N
    pi.append(pi_approx)
    delta = abs(pi_approx - math.pi)
    
    print(f"{N:<10} | {pi_approx:<15.5f} | {delta:<15.5f}")

os.makedirs('graphics', exist_ok=True)
mb.plot(N_list, pi, marker='s', color='g', label='Оцінка')
mb.axhline(y=math.pi, color='r', linestyle='--', label='Точне значення')
mb.xscale('log')
mb.xlabel('N (логарифмічна шкала)')
mb.ylabel('Значення пі')
mb.title('Оцінка числа пі методом Монте-Карло')
mb.legend()
mb.grid(True, linestyle="--")
mb.savefig('graphics/block3_plot.png')
mb.show()