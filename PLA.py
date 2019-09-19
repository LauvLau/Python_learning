import matplotlib.pyplot as plt
import sys

file_name = str(sys.argv[1])
f = open(file_name)
raw_data = f.readlines()

data = []
for i in raw_data:
    data.append(i.split())

w = [0, 567, 57]

while True:
    flag = True
    for i in range(0, len(data)):
        x1 = eval(data[i][0])
        x2 = eval(data[i][1])
        sign = w[0] + w[1] * x1 + w[2] * x2
        if sign > 0 and data[i][2] == '-':
            w[0] = w[0] - 1
            w[1] = w[1] - x1
            w[2] = w[2] - x2
            flag = False
            break
        elif sign < 0 and data[i][2] == '+':
            w[0] = w[0] + 1
            w[1] = w[1] + x1
            w[2] = w[2] + x2
            flag = False
            break
    if flag:
        break

X_o = []
Y_o = []
X_x = []
Y_x = []
for i in data:
    if i[2] == '+':
        X_o.append(eval(i[0]))
        Y_o.append(eval(i[1]))
    else:
        X_x.append(eval(i[0]))
        Y_x.append(eval(i[1]))

plt.xlabel('x1')
plt.ylabel('x2')
plt.scatter(X_o, Y_o, c='b', marker='o')
plt.scatter(X_x, Y_x, c='r', marker='x')

x1 = [x1 for x1 in range(-100, 101)]
x2 = [(w[0] + w[1] * i) / (-w[2]) for i in x1]
plt.plot(x1, x2, c=[0, 0, 0])

print(w)
plt.show()
