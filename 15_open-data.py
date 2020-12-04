#網路連線
# import urllib.request as request
# src = "http://www.ntu.edu.tw/"
# with request.urlopen(src) as response: #用response取得回應
#         #可複習第十三課的內容
#     data = response.read().decode("utf-8") 
#         #取得台大網站的原始碼(HTML, CSS, JS)
#         #可用utf-8進行解碼
# print(data)

#串接、擷取公開資料(本次示範使用API連結，格式為JSON)
import urllib.request as request
import json
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response) #利用json模組處理json的資料格式

###取得「公司名稱」，並列表出來
clist = data["result"]["results"]
    #JSON格式要搞懂→字典 裡面的 字典 裡面的 列表 裡面的 字典
with open("data_ch15.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")
    #回顧dictionary找value寫法；觀察可發現最內層有"公司名稱"的key
    #檔案寫入公司的名稱，一行一行表示(因為有換行符號)