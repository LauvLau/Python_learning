import random
import matplotlib.pyplot as plt
import sys

# print("Please input the w0:")
w0 = eval(sys.argv[1])
print(w0)
# print("Please input the w1:")
w1 = eval(sys.argv[2])
print(w1)
# print("Please input the w2:")
w2 = eval(sys.argv[3])
print(w2)
# print("Please input the number with positive label:")
num_positive = eval(sys.argv[4])
print(num_positive)
# print("Please input the number with negative label:")
num_negative = eval(sys.argv[5])
print(num_negative)
num_positive_count = 0
num_negative_count = 0
file_name = ('DataEmit %d %d %d %d %d .txt' % (w0, w1, w2, num_positive, num_negative))
f = open(file_name, 'w')
while num_negative_count < num_negative or num_positive_count < num_positive:
    x1 = random.uniform(-100, 101)
    x2 = random.uniform(-100, 101)
    if x1 * w1 + x2 * w2 + w0 > 0 and num_positive_count < num_positive:
        f.write("%f %f +\n" % (x1, x2))
        num_positive_count += 1
    elif x1 * w1 + x2 * w2 + w0 < 0 and num_negative_count < num_negative:
        f.write("%f %f -\n" % (x1, x2))
        num_negative_count += 1
    else:
        continue
f.close()
f = open(file_name)
X_o = []
Y_o = []
X_x = []
Y_x = []
X = []
Y = []
data = f.readlines()
print(data)
for i in data:
    # print(i)
    temp = i.split()
    if temp[2][0] == '+':
        X_o.append(eval(temp[0]))
        Y_o.append(eval(temp[1]))
    else:
        X_x.append(eval(temp[0]))
        Y_x.append(eval(temp[1]))
    # print(temp)
    X.append(eval(temp[0]))
    Y.append(eval(temp[1]))
f.close()
print(X_o)
print(Y_o)
print(X_x)
print(Y_x)
plt.xlabel('x1')
plt.ylabel('x2')
plt.scatter(X_o, Y_o, c='b', marker='o')
plt.scatter(X_x, Y_x, c='r', marker='x')
# plt.xlim(-100,101)
# plt.ylim(-100,101)
# x=np.linspace(-100,101,50)
# y=x+2
# plt.plot(x,y)
# plt.scatter(X,Y,c='r',marker='x')
plt.show()
