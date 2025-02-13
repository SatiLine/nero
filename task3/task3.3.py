a = a1 = -2 # начальная точка
h = 0.1 # шаг
d = 0.05 # небольшое положительное число 
         # для формулы производной
      
def f(x):
    return x*(x**2 - 9)
    
def df_dx(x, d = d):
    return (f(x + d) - f(x))/d 
    
for i in range(19):
    grad = df_dx(a)
    #print(grad)
    new_a = a - h * grad
    print(new_a)
    a = new_a

print("-------")

def df_dx1(x, d = d):
    return (f(x - 2 * d) - 8 * f(x - d) + 8 * f(x + d) - f(x + 2 * d)) / (12 * d)

for i in range(19):
    grad = df_dx1(a1)
    #print(grad)
    new_a1 = a1 - h * grad
    print(new_a1)
    a1 = new_a1