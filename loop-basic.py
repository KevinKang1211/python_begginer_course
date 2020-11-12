# for 變數名稱 in "列表"或"字串":
    #將列表中的項目或字串中的字元"逐一取出，逐一處理"
# for經常搭配range(): 製造連續數字的列表

# while迴圈
n=1
sum = 0 #用來記錄累加的結果
while n<=10:
    sum = sum+n #1加到10
    n+=1
print(sum)

# for 迴圈
for x in [3, 5, 1]:
    print(x)

for x1 in "Hello":
    print(x1)

for x2 in range(5): # 0-5不包含5
    print(x2)

for x3 in range(5, 10): # 包含開頭，不包含尾端
    print(x3)

sum1 = 0
for x4 in range(11): #用不同方式再寫一次1加到10
    sum1 = sum1 + x4
print(sum1) 

#自己練習
a = [1, 2, 3, 4, 5]
b = []
for y in a:
    b.append(y)
print(b)