import os

def traverse_dir(path):
    List_root = []
    List_dirs = []
    List_files =[]
    for root, dirs, files in os.walk(path):
        List_root.append(root)
        List_dirs.append(List_dirs)
        List_files.append(List_files)

    print(List_root[0])     #当前目录
    print(List_dirs)      #子目录列表
    print(List_files)     #文件列表
    return  List_root[1:]


def IncreaseSerialNumber(filepath):
    for num,file in enumerate(os.listdir(filepath)):
        num = num +1
        if num<10:
            index = "0"+str(num)
        elif num <100:
            index = str(num)
        else:
            index = str(num)
        print(index, file)
        os.rename(os.path.join(filepath,file),os.path.join(filepath,index+"、"+file))

file_path = "H:\\Project\\2、PyQt\\pyqt5-1\\15SpiderCsdn\\m0_37967652 - 副本\\"

List = traverse_dir(file_path)
for i in List:
    IncreaseSerialNumber(i)











