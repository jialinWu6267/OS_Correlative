# dir 需要复制、移动的文件
# dst_dir 目的地址
# 遍历dir下面的全部文件，将文件复制到dst_dir同一文件夹下面
import os
import shutil
from glob import glob
def get_files_from_dir(dir,dst_dir):
    if not os.path.exists(dir):
        return ''
    file_paths = []
    for root, directories, files in os.walk(dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    for i in file_paths:
        fpath, fname = os.path.split(i)  # 分离文件名和路径
        #可以加入筛选条件
        if not os.path.isfile(dst_dir + fname):
            shutil.move(i, dst_dir + fname)

dir = 'H:\图书\电脑相关图书\Python2\Python\\'                #A
dst_dir = 'H:\图书\电脑相关图书\Python2\python1\\'           #Copy 至   B

get_files_from_dir(dir,dst_dir)




