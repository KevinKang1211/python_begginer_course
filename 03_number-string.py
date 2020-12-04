#數字運算
x=3/6 #小數除法
print(x)
y=3//6 #整數除法
print(y)
z=7%3  #取餘數
print(z)

a=4
a+=1 # 相當於a=a+1 (等號後方先看)
#同理有a-=1; a*=1
print(a)

#字串運算
s="Hell\"o" #在雙引號前面打\，如同 \" ，表示「跳脫」，幫助區隔
print(s)

s2="Hello"+"World" #字串串接
print(s2)

s3="Hello\nWorld" # \n = 換行 (也可用三個單引號/雙引號，進行換行)
# """Hello World"""
print(s3)

###字串對內部字元編號(索引)，從"0"開始算
s4="Hello"
print(s4[2]) #使用中括號進行索引
print(s4[1:4])
print(s4[1:])
print(s4[:4])