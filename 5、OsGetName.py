import  os
path = "H:\\Project\\StockChange_CXYYJRYKJ2\\Pyqt5_pyqtgraph\\"
list = os.listdir(path)
list_T = [i for i in list if i.endswith('.py')]
for i in list_T:
    print(i)











