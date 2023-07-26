list_1 = [3, 1, 2, 4]
list_1.append(list_1[0])
list_1.append(list_1[1])
sum = list_1[0]+list_1[1]+list_1[2]
for i in range(1, len(list_1)-1):
    if list_1[i-1]+list_1[i]+list_1[i+1] > sum:
        sum = list_1[i-1]+list_1[i]+list_1[i+1]
print(sum)