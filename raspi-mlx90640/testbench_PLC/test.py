# test.py
from datetime import datetime

# var. names set
# 0-14 = panel, 15=sec. cw, 16=sec. hw, 17=pri. hw, 18=pri. cw
now1 = datetime.now()
for i in range(15):
    eCtrlState_dic = {f"eCtrlMode_{i}": [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].eCtrlState",
                                         f"Rkl/WtrSup/zone11/panel_{i}/eCtrlState"]}
    fSupTempAct_dic = {f"fSupTempAct_{i}": [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].fSupTempAct",
                                            f"Rkl/WtrSup/zone11/panel_{i}/fSupTempAct"]}
    fRtnTempAct_dic = {f"fRtnTempAct_{i}": [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].fRtnTempAct",
                                            f"Rkl/WtrSup/zone11/panel_{i}/fRtnTempAct"]}
    fFlowrateAct_dic = {f"fFlowrateAct_{i}": [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].fFlowrateAct",
                                              f"Rkl/WtrSup/zone11/panel_{i}/fFlowrateAct"]}
    f2WValveOpenSet_dic = {f"f2WValveOpenSet_{i}": [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].f2WValveOpenSet",
                                                    f"Rkl/WtrSup/zone11/panel_{i}/f2WValveOpenSet"]}
    bPumpActivated_dic = {f"bPumpActivated_{i}": [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].bPumpActivated",
                                                  f"Rkl/WtrSup/zone11/panel_{i}/bPumpActivated"]}
    b6WValveActivated_dic = {f"bPumpActivated_{i}": [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].bPumpActivated",
                                                     f"Rkl/WtrSup/zone11/panel_{i}/b6WValveActivated"]}
for j in range(15, 19):
    fCircSupTempAct_dic = {f"fCircSupTempAct_{i}": [f"GVL_WtrSupCC.stZone11_SecSup[{j}].fCircSupTempAct",
                                                    f"Rkl/WtrSup/zone11/sec_{j}/fCircSupTempAct"]}
    fCircRtnTempAct_dic = {f"fCircRtnTempAct_{i}": [f"GVL_WtrSupCC.stZone11_SecSup[{j}].fCircRtnTempAct",
                                                    f"Rkl/WtrSup/zone11/sec_{j}/fCircRtnTempAct"]}
    fMainSupTempAct_dic = {f"fMainSupTempAct_{i}": [f"GVL_WtrSupCC.stZone11_SecSup[{j}].fMainSupTempAct",
                                                    f"Rkl/WtrSup/zone11/sec_{j}/fMainSupTempAct"]}
    fMainRtnTempAct_dic = {f"fMainRtnTempAct_{i}": [f"GVL_WtrSupCC.stZone11_SecSup[{j}].fMainRtnTempAct",
                                                    f"Rkl/WtrSup/zone11/sec_{j}/fMainRtnTempAct"]}
    fPumpPowerSet_dic = {f"fPumpPowerSet_{i}": [f"GVL_WtrSupCC.stZone11_SecSup[{j}].fPumpPowerSet",
                                                f"Rkl/WtrSup/zone11/sec_{j}/fPumpPowerSet"]}
    fValveOpenSet_dic = {f"fValveOpenSet_{i}": [f"GVL_WtrSupCC.stZone11_SecSup[{j}].fValveOpenSet",
                                                f"Rkl/WtrSup/zone11/sec_{j}/fValveOpenSet"]}
now2 = datetime.now()
print(now2 - now1)