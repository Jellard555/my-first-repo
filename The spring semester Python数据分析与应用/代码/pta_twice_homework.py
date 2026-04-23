import numpy as np
matrix1 = np.array(eval(input()))
matrix2 = np.array(eval(input()))
print(matrix1)
print(matrix2)
if matrix1.shape[1] == matrix2.shape[0]:
    result = np.dot(matrix1,matrix2)
    print(result)
else:
    print("wrong!")




arr = eval(input())
result = []
for i, val in enumerate(arr):
    result.append(val)
    if i < len(arr) - 1:
        result.extend([0, 0])

print( '['+ ' '.join(map(str,result)) + ']')
import numpy as np

# 1. 读取输入
m, n = map(int, input().split( ))
x, y, z = map(int, input().split( ))

# 2. 生成随机数组并设置种子
np.random.seed(0)
A = np.random.randint(1, 21, size=(m, n))

# 3. 改变尺寸
B = A.reshape(x, y, z)

# 4. 计算统计量
max_val = B.max()
min_val = B.min()
mean_val = B.mean()
var_val = B.var()

# 5. 按维度求和：axis=1对应行，axis=2对应列
row_sum = B.sum(axis=1)
col_sum = B.sum(axis=2)

# 6. 严格匹配样例格式输出
print(B)
print(f"B最大元素: {max_val}")
print(f"B最小元素: {min_val}")
print(f"B均值: {mean_val:.2f}")
print(f"B方差: {var_val:.2f}")
print("B按行求和:")
print(row_sum)
print("B按列求和:")
print(col_sum)