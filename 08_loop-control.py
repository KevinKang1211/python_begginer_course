# break的簡易範例
n = 0
while n<5:
    if n==3:
        break
    print(n) #印出迴圈「中﹞的n
    n+=1
print("最後的n:",n) #印出迴圈「結束後」的n

# continue 的簡易範例 (重要)
r = 0
for x in [0, 1, 2, 3]:
    if x%2==0:    # x是偶數( % = 取餘數)
        continue  # (*重要) 符合條件的話，強制繼續/執行迴圈，忽略後續的code
    print(x)
    r+=1      #列表中只有1和3會跑到下面兩行程式碼，因此r只會加兩次
print("最後的r:", r)

# else的 簡易範例 (重要)
sum = 0
for a in range(11):
    sum+=a
else:
    print(sum) # 印出0+1+2...+10的結果
#(*重要) else是迴圈結束「前」(離開前)，執行此區塊命令

#綜合範例: 找出整數平方根
# 輸入9會得到3，輸入11會得到「沒有」整數的平方根

s = int(input("輸入一個正整數: "))
for i in range(s+1): 
        # i 從 0 ~ (s+1)-1 (這個概念要想清楚,range不含最後一個數),用s+1是為了解決輸入1會沒有整數平方根的解
    if i*i==s:
        print("整數平方根", i)
        break #用 break強制結束迴圈時，不會執行else區塊
else:
    print("沒有整數平方根")