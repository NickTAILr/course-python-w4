#f_obj = open("./file_io.txt","r+",encoding='utf-8')
#con = f_obj.read()
#f_obj.close()
#print(con)

with open("./file_io.txt","r+",encoding='utf-8') as f_obj:
    con = f_obj.read()
print(con)

#f_obj = open('f.txt','r+')
#f_obj.write('abcdefg')
#f_obj.close()

#f_obj = open('f.txt',"r+")
#con = f_obj.read()
#f_obj.close()
#print(con)

with open('f.txt',"r+") as f_obj:#跳出with自動關閉
    con = f_obj.read()
print(con)

#con = f_obj.read()
#con = f_obj.readline()讀一行
#con = f_obj.readlines()讀全部，輸出用list 區分的原因為「記憶體的使用量」
#例如:檔案的大小過大 會造成讀取時間過久

#絕對路徑 C:\\3A717087\\file_io.txt windows(\) Linux(/) 統一用正斜線(/)

#mod = "r" 讀取 "W"寫入 "r+"讀寫 "a+"可讀可寫可創建檔案

#fileObject.write("\naaaa")



    