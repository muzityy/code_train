num1 = input("请输入第一个大数：")
num2 = input("请输入第二个大数：")

# 将输入的字符串反转并转换成列表
num1_list = list(num1[::-1])
num2_list = list(num2[::-1])

# 初始化进位和结果列表
carry = 0
result = []

# 处理两个列表的相同位
for i in range(max(len(num1_list), len(num2_list))):
    # 取出相应位上的数字，如果为空则视为0
    n1 = int(num1_list[i]) if i < len(num1_list) else 0
    n2 = int(num2_list[i]) if i < len(num2_list) else 0

    # 将两个数字相加，并加上进位
    sum = n1 + n2 + carry

    # 如果相加的结果大于等于10，需要将进位设置为1，并将结果减去10
    if sum >= 10:
        carry = 1
        sum -= 10
    else:
        carry = 0

    # 将相加的结果添加到结果列表中
    result.append(str(sum))

# 如果还有进位，需要将进位添加到结果列表的末尾
if carry > 0:
    result.append(str(carry))

# 将结果列表反转并转换成字符串
result_str = ''.join(result[::-1])

print("两个大数的和为：", result_str)
