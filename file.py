#儲存(寫入)檔案
#1.開啟
file = open("data.txt", mode="w", encoding="utf-8")
    #檔案物件: 有個檔案物件來操作檔案(後續課程會再提)
    #mode(模式): w=寫入, r=讀取, r+ = 讀寫
    #encoding(編碼): 在開啟檔案時設定(utf-8為使用中文最常見)
#2.操作
file.write("5\n3") 
#3.關閉
file.close()

###【最佳實務】寫法(不須手動寫關閉，功能和上面一樣):
with open("test.txt", mode="w", encoding="utf-8") as file:
    file.write("hello testing\nSecond Line\n測試中文")

#讀取檔案(讀取已存在的檔案)
#Task: 把檔案中的數字資料，「一行一行」讀取出來，並計算總合
sum=0
with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file:  #一行一行讀取→讀到"5"、放進line
        sum+=int(line) #原本是字串形式
print(sum)

###使用JSON格式讀取、複寫檔案(*搭配JavaScript課程的JSON介紹)
import json

#從檔案中讀取 json 資料，放入變數json_test裡面
with open("config.json", mode="r", encoding="utf-8") as file:
    json_test = json.load(file)
    #讀取到的資料 = json.load(檔案物件)
print(json_test) # json_test是一個「字典」型態的資料

#用python字典的讀取方法: 讀key得到value
print("Name: ", json_test["Name"])
print("Version: ", json_test["Version"])
json_test["Name"]="New Name" #修改變數中的資料

#把更新的資料「複寫」回檔案中
with open("config.json", mode="w", encoding="utf-8") as file:
    json.dump(json_test, file)

#json.load() / json.dump(要寫入的資料,檔案物件)