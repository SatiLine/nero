a0 = [10, 1] # начальная точка
h = 0.1 # шаг
      
def f(x,y):
    return x**2 + 10 * y**2
    
def grad_f(x, y):
    return [2 * x, 20 * y]

a = a0[:]

for i in range(10):
    grad = grad_f(a[0], a[1])
    a[0] = a[0] - h * grad[0]
    a[1] = a[1] - h * grad[1]
    
    print(a, f(a[0], a[1]))
