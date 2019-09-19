import matplotlib.pyplot as plt
import sys
import cmath

# 初始化用来generate training data的w
w0 = [7, 4, 5]

file_name = str(sys.argv[1])
f = open(file_name)
raw_data = f.readlines()
# print(raw_data)

data = []
for i in raw_data:
    data.append(i.split())

w = [0, 567, 57]

while True:
    flag = True
    for i in range(0, len(data)):
        x1 = eval(data[i][0])
        # print(x1)
        x2 = eval(data[i][1])
        # print(x2)
        # print(data[i][2])
        sign = w[0] + w[1] * x1 + w[2] * x2
        if sign > 0 and data[i][2] == '-':
            # w[0]不能忘记
            w[0] = w[0] - 1
            w[1] = w[1] - x1
            w[2] = w[2] - x2
            flag = False
            break
        elif sign < 0 and data[i][2] == '+':
            # w[0]不能忘记
            w[0] = w[0] + 1
            w[1] = w[1] + x1
            w[2] = w[2] + x2
            flag = False
            break
    if flag == True:
        break

X_o = []
Y_o = []
X_x = []
Y_x = []
for i in data:
    print(i)
    if i[2] == '+':
        X_o.append(eval(i[0]))
        Y_o.append(eval(i[1]))
    else:
        X_x.append(eval(i[0]))
        Y_x.append(eval(i[1]))

# print(X_o)
# print('')
# print(Y_o)
# print('')
# print(X_x)
# print('')
# print(Y_x)
# print('')
plt.xlabel('x1')
plt.ylabel('x2')
print(w)
plt.scatter(X_o, Y_o, c='b', marker='o')
plt.scatter(X_x, Y_x, c='r', marker='x')

x1 = [x1 for x1 in range(-100, 101)]
# 方法正确了，画线出了问题，画线依据这个公式，w1*x1+w2*x2+w0=0
x2 = [(w[0] + w[1] * i) / (-w[2]) for i in x1]
# 训练得到的wt
plt.plot(x1, x2, c=[0, 0, 0])

x1_ = [x1_ for x1_ in range(-100, 101)]
x2_ = [(-w0[0] - w0[1] * i) / w0[2] for i in x1_]
# 标准wt
plt.plot(x1_, x2_, c='r')


# 计算余弦相似度
def cal(x, y, z):
    x = pow(x, 2)
    y = pow(y, 2)
    z = pow(z, 3)
    return cmath.sqrt(x + y + z)


cos_ = (w[0] * w0[0] + w[1] * w0[1] + w[2] * w0[2]) / (cal(w0[0], w0[1], w0[2]) * cal(w[0], w[1], w[2]))
print(cos_)
# plt.plot(x,y)
plt.show()
