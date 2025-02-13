a = 2 # начальная точка
h = 0.1 # шаг
d = 0.05 # небольшое положительное число 
         # для формулы производной
      
def f(x):
    return x**2
    
def df_dx(x, d = d):
    return (f(x + d) - f(x))/d 
    
for i in range(19):
    grad = df_dx(a)
    #print(grad)
    new_a = a - h * grad
    print(new_a)
    a = new_a