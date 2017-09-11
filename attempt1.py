f = open('/home/thealchemist/datasets/actual_data/user_000011').readlines()
data = eval(f[0])

print data.keys()

print len(data[1])

print data[1][1]
print
print data[1][2]
