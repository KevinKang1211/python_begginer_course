#集合的運算
s1 = {3, 4, 5}
print(3 in s1) 
print(10 not in s1)
    #in/not in來判斷是否在集合裡
s2 = {4, 5, 6, 7}
s3 = s1&s2 #交集: 兩個集合中，相同的資料
print(s3)
s4 = s1|s2 #聯集: 取兩集合中所有資料，但不重複取
print(s4)
s5 = s1-s2 #差集: 從S1中，減去和S2重疊的部分(差集順序有差)
print(s5)
s6 = s1^s2 #反交集: 取兩個集合中，「不重疊」的部分
print(s6)

s = set("Hello")
print(s) 
    #set(字串) : 把字串拆解成集合(無順序)
     
#字典的運算: key-value的配對
dic = {"apple":"蘋果", "bug":"蟲"}
print(dic["bug"])
    # 字典名稱[key] = value
dic["apple"] = "小蘋果"
print(dic["apple"])

print("apple" in dic) #判斷"key"是否存在
print("test" not in dic)

print(dic)
del dic["apple"] 
print(dic)
    #刪除字典中的鍵值對

dic2 = {x:x*2 for x in [3, 4, 5]}
print(dic2) 
    # **由列表的資料產生字典