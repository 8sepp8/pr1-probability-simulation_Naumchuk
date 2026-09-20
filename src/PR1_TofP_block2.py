import random as r

print(10*'='," БЛОК 2. Геометрична ймовірність: задача про зустріч",10*'=')

T = 60
tau = 10

exact_p_meet = 1 - ((T - tau) / T) ** 2
exact_p_no_meet = 1 - exact_p_meet

print(f"Точна P(Зустріч) = {exact_p_meet:.5f}")
print(f"Точна P(Відсутність) = {exact_p_no_meet:.5f}\n")
print(f"{'N':<10} | {'W (зустрічі)':<15} | {'похибка':<15}")
print("-" * 45)

N_list = [10, 100, 1000, 10000, 100000, 1000000]

for n in N_list:
    meetings = 0
    for _ in range(n):
        x = r.uniform(0, T)
        y = r.uniform(0, T)
        if abs(x - y) <= tau:
            meetings += 1
            
    w_meet = meetings / n
    error = abs(w_meet - exact_p_meet)
    
    print(f"{n:<10} | {w_meet:<15.5f} | {error:<15.5f}")