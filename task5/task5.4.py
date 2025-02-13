a0 = [10, 1] # начальная точка
h0 = 0.1

def f(x, y):
    return x**2 + 10 * y**2
    
def grad_f(x, y):
    return [2 * x, 20 * y]

a = a0[:]
g = [0, 0]

for i in range(10):
    grad = grad_f(a[0], a[1])
    g[0] += grad[0]**2
    g[1] += grad[1]**2
    h_x = h0 / (g[0]**0.5)
    h_y = h0 / (g[1]**0.5)
    a[0] -= h_x * grad[0]
    a[1] -= h_y * grad[1]
    print(a, f(a[0], a[1]))
