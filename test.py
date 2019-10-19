a = [246,34,23,21,19,16,4,2,2,1]
b = [1,2,3,4,5,6,7,8,9,10]
s = 0
for i in a:
    s+=i
print(s)


import matplotlib.pyplot as plt
plt.bar(b,a)
plt.xlabel('用户交易排名')
plt.ylabel('用户交易量')
plt.title('猪八戒网python接单交易量')
plt.show()


