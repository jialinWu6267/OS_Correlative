import os


def IncreaseSerialNumber(filepath):
    '''
    三位数的序列 每个文件夹上添加序号
    :param path: filepath
    '''
    for num,file in enumerate(os.listdir(filepath)):
        num = num +1
        if num<10:
            index = "0"+str(num)
        elif num <100:
            index = "" + str(num)
        else:
            index = str(num)
        print(index, file)
        os.rename(os.path.join(filepath,file),os.path.join(filepath,index+"、"+file))


def DeleteSerialNumber(filepath,N):
    '''
    删除文件夹下的文件序列
    :param N: 删除前面4位
    :param path:
    :return:
    '''
    for file in os.listdir(filepath):
        print(file)
        os.rename(os.path.join(filepath,file),os.path.join(filepath,file[N:]))
# filepath  = "H:\\Project\\2、PyQt\\pyqt5-1\\15SpiderCsdn\\m0_37967652 - 副本\\"
# DeleteSerialNumber(filpath,4)
# path = "H:\\Project\\15 SpiderCsdn\\m0_37967652 - 副本\\时间轴\\"

# DeleteSerialNumber(path,3)
# IncreaseSerialNumber(path)
#批量生成py文件
# import os
# filePrefix='Test'
# fileSuffix='.py'
# fileNum=7 #文件个数
# for i in range(0,fileNum):
#     filename=filePrefix+str(i)+fileSuffix
#     with open(filename,'w') as f:
#         f.write('')

def CreatePyFileName(PrimaryPath,CreateNewPath):

    list = os.listdir(PrimaryPath)
    list2 = [filename[:-4] for filename in list if ".pdf" in filename]
    print(list2)

    fileSuffix='.py'

    for i in list2:
        filename=CreateNewPath+str(i)+fileSuffix
        with open(filename,'w') as f:
            f.write('')

# PrimaryPath = "H:\\Project\\15 SpiderCsdn\\m0_37967652 - 副本\\Pyqt\\"
# CreateNewPath = "H:\\Project\\StockChange_CXYYJRYKJ\\Pyqt5\\"
# CreatePyFileName(PrimaryPath,CreateNewPath)

# path = "H:\\Project\\StockChange_CXYYJRYKJ\\Pyqt5\\k_recognition_strategy\\"
# DeleteSerialNumber(path,2)






