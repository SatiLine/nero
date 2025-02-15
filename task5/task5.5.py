a0 = [10, 1]  # начальная точка
h0 = 0.1      # начальный шаг
beta1 = 0.9   # коэффициент для первого момента
beta2 = 0.9   # коэффициент для второго момента

def f(x, y):
    return x**2 + 10 * y**2

def grad_f(x, y):
    return [2 * x, 20 * y]


a = a0[:]  #
m = [0.0, 0.0]  # Первый момент (градиенты)
v = [0.0, 0.0]  # Второй момент (квадраты градиентов)
t = 0           # Счетчик итераций

# Основной цикл Adam
for i in range(10):  # Количество итераций
    t += 1  # Увеличиваем номер итерации
    grad = grad_f(a[0], a[1])  # Вычисляем градиент
    
    # Обновляем моменты
    m[0] = beta1 * m[0] + (1 - beta1) * grad[0]
    m[1] = beta1 * m[1] + (1 - beta1) * grad[1]
    
    v[0] = beta2 * v[0] + (1 - beta2) * (grad[0] ** 2)
    v[1] = beta2 * v[1] + (1 - beta2) * (grad[1] ** 2)
    
    # Коррекция смещения
    m_hat = [m[j] / (1 - beta1 ** t) for j in range(2)]
    v_hat = [v[j] / (1 - beta2 ** t) for j in range(2)]
    
    # Обновление параметров
    a[0] -= h0 * m_hat[0] / (v_hat[0] ** 0.5)
    a[1] -= h0 * m_hat[1] / (v_hat[1] ** 0.5)


    print(a, f(a[0], a[1]))

