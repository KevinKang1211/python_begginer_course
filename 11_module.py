#載入內建的 sys 模組並取得資訊
import sys
print(sys.platform)
print(sys.maxsize)

#建立 geometry 模組，並載入使用
#import geometry
#result = geometry.distance(1,1,5,5)
#print(result)

#x = geometry.slope(1,2,5,6)
#print(x)

#調整搜尋模組的路徑
print(sys.path) #印出模組的搜尋路徑列表
print("------------------")
sys.path.append("module_bag")
    #重要:在模組的搜尋路徑列表中【新增路徑】 
    # 增加一個"module"的搜尋路徑，這樣才找得到被放到"module_bag"資料夾的模組
print(sys.path) 
print("------------------")

import geo
print(geo.distance(1,1,5,5))