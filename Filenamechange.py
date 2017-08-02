import os
import glob

fPath = r'D:\황성훈_공부자료\A_Python\A1_Python Books\Python_중급\\'
fFile = r'D:\황성훈_공부자료\A_Python\A1_Python Books\Python_중급\*.jpg'

i = 1
for path in glob.glob(fFile):
    if path[-3:] == 'jpg':
        os.rename(path,fPath + 'Python_' + str(i) + '.jpg')
        i += 2 