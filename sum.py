num1 = "1234567899999999"
num2 = "1234567899999999"
# 先将字符串反转
num1_list =  list(num1[::-1])
num2_list =  list(num2[::-1])

carrybit = 0
result = []

for i in range(max(len(num1_list),len(num2_list))):
    n1 = int(num1_list[i]) if i < len(num1_list) else 0
    n2 = int(num2_list[i]) if i < len(num2_list) else 0
    sum = n1 + n2 + carrybit
    if sum >= 10:
        carrybit = 1
        sum = sum -10
    else:
        carrybit = 0
    result.append(str(sum))

if carrybit > 0:
    result.append(str(carrybit))
result_str = result[::-1]

print(result_str)
