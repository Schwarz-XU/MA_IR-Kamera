# pub_pyads.py
import pyads
from DataAcquisition import sub

# PLC connection and port
plc = pyads.Connection('5.78.127.222.1.1', 851)
plc.open()

plc.read_by_name("GVL_WtrSupPri.fHWSupTempAct", pyads.PLCTYPE_REAL)

# initial temperature data
sub.run()
payload = sub.payload
print(payload)
for i in range(0, 15):
    plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].fSurfTempAct".format(nPanelIndex=i), payload, pyads.PLCTYPE_REAL)
'''
# real，浮点型
while True:
    plc.write_by_name('MAIN.test_real', 5.5, pyads.PLCTYPE_REAL)

# 也可以使用专有的读取指令 read_structure_by_name进行读取，使用这条指令读取，PLC中申明的结构体需要加上{attribute 'pack_mode' := '1'}
# 在python中线定义结构类型
structure_def=(('a', pyads.PLCTYPE_BOOL, 1),
               ('b', pyads.PLCTYPE_INT, 1),
               ('c', pyads.PLCTYPE_STRING, 1),
               ('d', pyads.PLCTYPE_REAL, 1))
structure_value3 = plc.read_structure_by_name('MAIN.test_structure', structure_def, 1, pyads.ads.size_of_structure(structure_def))
print(structure_value3)

# 非自带数据类型，string数组，对于string类型，pyads.PLCTYPE_STRING*3 这种方式是不能使用的，需要额外用循环
arr_string = ['\'string1\'', '\'string2\'', '\'string3\'']
arr_index = ['1', '2', '3']
arr_string2 = ['', '', '']
for i in range(3):
    # plc.write_by_name('MAIN.test_arr_string[1]', 'string1', pyads.PLCTYPE_STRING)
    str = 'plc.write_by_name(\'MAIN.test_arr_string[{}]\', {}, pyads.PLCTYPE_STRING)'.format(arr_index[i], arr_string[i])
    eval(str)
    str2 = 'plc.read_by_name(\'MAIN.test_arr_string[{}]\', pyads.PLCTYPE_STRING)'.format(arr_index[i])
    arr_string2[i] = eval(str2)
print(arr_string2)

# 关闭端口
plc.close()
'''
