# Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    # 定義實體方法:
    def show(self):
        print(self.x, self.y) 
    def distance(self, targetX, targetY):
        return(((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
        
p = Point(3, 4) 
    #3放到x, 4放到y
p.show() #呼叫實體方法 (本質上是函式，呼叫方法一樣)
result = p.distance(0,0) 
    # 0放到targetX, 0放到targetY
    # 功能: 計算座標(3,4)和座標(0,0)之間的距離
print(result)


### File 實體物件的設計: 包裝檔案讀取的程式
class File:
    #初始化函式
    def __init__(self, name):
        self.name = name
        self.file = None #尚未開啟檔案: 初期是 None
        #建立兩個實體屬性: 第一個name從參數來，另一個屬性file，一開始是None
    #實體方法(共兩個)
    def open(self): 
        self.file = open(self.name, mode="r", encoding="utf-8")
        #第一個open是檔案方法的open(自己建立的) / 第二個open是python內建函式，之前學過的open
        #開啟一個檔案後，開啟後把這個檔案物件放進實體屬性file裡面→原本是NONE，現在會變成一個檔案物件
    def read(self):
        return self.file.read()
        #讀取出來並回傳

# 讀取第一個檔案
f1 = File("data_ch181.txt") #建立一個檔案的實體物件放進變數f1
f1.open()        #呼叫實體方法
data = f1.read() #呼叫第二個方法: 讀取並回傳資料丟進data
print(data)

# 讀取第二個檔案
f2 = f1 = File("data_ch182.txt")
f2.open()
data2 = f2.read()
print(data2)

###這樣包裝是一個簡化的概念，不用一直重複寫複雜的code