### 有序「可變動」列表 List []
grades = [12, 15, 78, 99, 77]
print(grades[0]) 
    #先寫[]再加索引的編號
grades[1] = 55 
    #把 55 更新放到列表中的第二個位置
print(grades)
print(grades[1:4]) 
    #取編號1-4,但不包含4
grades[1:4] = [] 
    #連續刪除列表中從編號1-編號4(不包含)的資料
print(grades)
grades = grades + [12, 33] #串接
print(grades)

length = len(grades)
print(length)
    #len(列表名稱) = 取得列表長度

data = [[3, 4, 5], [6, 7, 8]]
print(data[0][0])
    #巢狀列表；注意索引順序(由外往內)，中間無逗號
data[0][0:2] = [1, 1]
print(data[0])

### 有序「不可變動」列表 Tuple ()
x = (3, 4, 5)
print(x[2]) 
    #操作大致都和list一樣，除了下列語法
x[0] = 5
print(x)
    #Error: Tuple的資料不可以變動
