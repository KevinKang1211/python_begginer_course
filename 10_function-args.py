#參數的【預設資料】
def power(base, exp=0):
    print(base**exp)
power(3,2)
power(4) #上面這行有指定exp的值，若像這行沒給，就會跑預設值的exp=0

#使用【參數名稱對應】
def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n2=2, n1=4) #python提供的彈性

###【無限/不定參數】資料
#因為是要做「平均」，因此希望不管要做幾個數字都能運作此函數
#作法：參數名稱前面加 * 號
def avg(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n # n會進去tuple裡面一個一個處理
    print(sum/len(numbers)) #除以列表長度(=幾個變數)

avg(3,4)
avg(3,5,10)
avg(1,3,-1,-8)
#Tuple: 有序列表 / 迴圈是個很好運用tuple的方式→一個一個處理
