# test
import queue
from queue import Queue

# var. names set
eCtrlMode_dic = {}
fSupTempSet_dic = {}
f2WValveOpenSetMan_dic = {}
b6WValveActivateMan_dic = {}
bPumpActivateMan_dic = {}

for i in range(0, 15):
    eCtrlMode_dic["eCtrlMode_" + str(i)] = Queue()
    fSupTempSet_dic["fSupTempSet_" + str(i)] = Queue()
    f2WValveOpenSetMan_dic["f2WValveOpenSetMan_" + str(i)] = Queue()
    b6WValveActivateMan_dic["b6WValveActivateMan_" + str(i)] = Queue()
    bPumpActivateMan_dic["bPumpActivateMan_" + str(i)] = Queue()

