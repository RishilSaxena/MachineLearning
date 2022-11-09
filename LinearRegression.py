import matplotlib.pyplot as plt
import numpy as np



def cost_function(w0, w1, x, y):
    cost = 0
    m = len(x)
    for i in range(m):
        cost += (w0 + w1*x[i] - y[i])**2
    cost /= 2*m
    return cost


def find_best_fit(w0, w1, x, y, lr, epochs):
    cost_axis = []
    iteration_axis= list(range(epochs))
    for iteration in range(epochs):
        d1 = 0
        d2 = 0
        m=len(x)
        for i in range(m):
            d1 += (w0 + w1*x[i] - y[i])
            d2 += (w0 + w1*x[i] -y[i])*x[i]
        d1 /= m
        d2 /= m
        w0 -= lr*d1
        w1 -= lr*d2
        current_cost = cost_function(w0, w1, x, y)
        print(f"Current cost for iteration {iteration+1}: {current_cost}")
        cost_axis.append(current_cost)

    plt.plot(iteration_axis, cost_axis, "b-")
    plt.show()
    return w0, w1

x = [1, 3, 4, 7, 12, 18, 23]
y = [-2, 5, 9, 15, 22, 24, 40]

print(cost_function(0, 0, x, y))
w0 = 0
w1 = 0
lr = 0.001
epochs = 100
w0, w1 = find_best_fit(w0, w1, x, y, lr, epochs)
print(w0, w1)

plt.scatter(x, y)

axes = plt.gca()
x_vals = np.array(axes.get_xlim())
y_vals = w0 + w1 * x_vals
plt.plot(x_vals, y_vals, color="red")

plt.show()




