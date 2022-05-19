import os

if not os.path.exists('./data'):
    os.mkdir('./data')
    
with open('./data/f.txt','w') as f_obj:
    f_obj.write('hello~~World')
    
print(os.path.basename('./data/f.txt'))#取得檔案名稱

print(os.path.basename('./data/f.txt/.txt'))


    
