import random
import sys

w = str(sys.argv[1]).split(',')
w0 = eval(w[0])
w1 = eval(w[1])
w2 = eval(w[2])
num_positive = eval(sys.argv[2])
num_negative = eval(sys.argv[3])
num_positive_count = 0
num_negative_count = 0
f = open("train.txt", 'w')
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
