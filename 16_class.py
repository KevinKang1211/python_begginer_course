#類別: 用來封裝變數或函式
    #封裝的變數或函式，統稱為類別的【屬性】 attribute
    #步驟: 定義→使用

#定義「類別」與「類別屬性」(i.e., 封裝在類別中的變數和函式)
#定義一個類別IO，有兩個屬性:supportedSrcs <變數> 和 read <函式>
class IO:
    supportedSrcs=["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported")
        else:
            print("Read from", src)
#使用類別

print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")