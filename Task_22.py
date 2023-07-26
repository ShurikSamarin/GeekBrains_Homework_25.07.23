n = int(input("Input n\n"))
list_1 = []
for i in range(n):
    list_1.append(int(input("Input number N\n")))
m = int(input("Input m\n"))
list_2 = []
for i in range(m):
    list_2.append(int(input("Input number M\n")))
print("N: ", list_1)
print("M: ", list_2)
list_1.sort()
list_2.sort()
s_1 = set(list_1)
s_2 = set(list_2)
s_res = s_1 & s_2
print("Res: ", s_res)