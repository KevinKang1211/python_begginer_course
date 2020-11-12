#定義函式
#函式內部的程式碼若沒有「呼叫」，就不會執行
def multiply(n1, n2):
    print(n1*n2) 
    return
#呼叫函式
multiply(10, 8)

###函式的呼叫是「流程」的變化，但呼叫完畢後這個函式「得到」什麼資料，要看「回傳值」
#函式跑完就算沒寫return的話也會自動return (= 回傳None，因為後面沒有回傳值)
x =multiply(3, 4)
print(x)


#跑進函式裡會將n3*n4印出，故先print"12"；又因設回傳值=10，
# 10會回傳到"multiply2(3, 4)"，並被放進y這個變數，故print(y)=10
def multiply2(n3, n4):
    print(n3*n4) 
    return 10
y = multiply2(3, 4)
print(y)

# 函式可用來做程式的包裝: 同樣的邏輯可重複運用
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum = sum+n
    print(sum)
calculate(23)
calculate(10)
