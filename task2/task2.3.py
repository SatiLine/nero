h = 0.1  # шаг
d = 0.05  # небольшое положительное число

# Функция f(x) = x**2
def f2(x):
    return x**2

def df_dx_2(x, d = d):
    return (f2(x + d) - f2(x)) / d

# Функция f(x) = x**4
def f4(x):
    return x**4

def df_dx_4(x, d=d):
    return (f4(x - 2 * d) - 8 * f4(x - d) + 8 * f4(x + d) - f4(x + 2*d)) / (12 * d)

# Начальное значение a0
a0_values = [i for i in range(-10, 11)]  

for a0 in a0_values:
    a1_2 = a0 - h * df_dx_2(a0)
    a1_4 = a0 - h * df_dx_4(a0)
    
    if abs(a1_2 - a0) >= abs(a1_4 - a0):
        print(f"При начальном значении {a0}:")
        print(f"a1 для x^2: {a1_2}")
        print(f"a1 для x^4: {a1_4}")
  