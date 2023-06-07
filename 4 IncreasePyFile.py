import os
def IncreaseDocxFile1(T_path,S_str,T_Filepath,T_str):
    '''
    获取T_path路径下包含S_str的文件名，在T_Filepath文件夹下新建包含T_str的文件
    :param T_path: 原文件夹
    :param S_str: 去掉的文件类型后缀
    :param T_Filepath:新建文件的文件夹
    :param T_str: 新增的文件类型后缀
    '''
    list_S = [f for f in os.listdir(T_path) if f.endswith('.'+S_str)]
    for i in list_S:
        T_FileName = i[:-(len(S_str)+1)] +'.'+ T_str
        with open(T_Filepath+T_FileName, 'w') as f:
            f.write('')


def IncreaseDocxFile2(T_path, S_str, T_Filepath, T_str):
    '''
    在T_path下一级创建一个文件夹存新建文件
    '''
    list_S = [f for f in os.listdir(T_path) if f.endswith('.' + S_str)]
    list_T = path.split('\\')
    os.makedirs(T_Filepath + list_T[-2])
    T_Filepath = T_Filepath + list_T[-2] + '\\'
    for i in list_S:
        T_FileName = i[:-(len(S_str) + 1)] + '.' + T_str
        with open(T_Filepath + T_FileName, 'w') as f:
            f.write('')

#1
path = "H:\\Project\\StockChange_CXYYJRYKJ2\\Pyqt5_pyqtgraph\\"
# S_str = 'py'
# T_str = 'docx'
# IncreaseDocxFile1(path,S_str,path,T_str)









































