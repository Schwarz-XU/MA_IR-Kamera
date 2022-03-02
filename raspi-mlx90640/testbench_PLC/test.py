import time
import paho.mqtt.client as mqtt
import pyads
from queue import Queue

# start = time.perf_counter()
[eCtrlState_dic, fSupTempAct_dic, fRtnTempAct_dic, fRtnTempAct_dic, fFlowrateAct_dic, f2WValveOpenSet_dic,
 bPumpActivated_dic, b6WValveActivated_dic, fCircSupTempAct_dic, fCircRtnTempAct_dic, fMainSupTempAct_dic,
 fMainRtnTempAct_dic, fPumpPowerSet_dic, fValveOpenSet_dic] = [dict(), dict(), dict(), dict(), dict(), dict(), dict(),
                                                               dict(), dict(), dict(), dict(), dict(), dict(), dict()]

for i in range(15):
    eCtrlState_dic[f"eCtrlState_{i}"] = [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].eCtrlState",
                                         f"Rkl/WtrSup/zone11/panel_{i}/eCtrlState",
                                         pyads.PLCTYPE_INT, Queue()]
    fSupTempAct_dic[f"fSupTempAct_{i}"] = [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].fSupTempAct",
                                           f"Rkl/WtrSup/zone11/panel_{i}/fSupTempAct",
                                           pyads.PLCTYPE_REAL, Queue()]
    fRtnTempAct_dic[f"fRtnTempAct_{i}"] = [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].fRtnTempAct",
                                           f"Rkl/WtrSup/zone11/panel_{i}/fRtnTempAct",
                                           pyads.PLCTYPE_REAL, Queue()]
    fFlowrateAct_dic[f"fFlowrateAct_{i}"] = [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].fFlowrateAct",
                                             f"Rkl/WtrSup/zone11/panel_{i}/fFlowrateAct",
                                             pyads.PLCTYPE_REAL, Queue()]
    f2WValveOpenSet_dic[f"f2WValveOpenSet_{i}"] = [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].f2WValveOpenSet",
                                                   f"Rkl/WtrSup/zone11/panel_{i}/f2WValveOpenSet",
                                                   pyads.PLCTYPE_REAL, Queue()]
    bPumpActivated_dic[f"bPumpActivated_{i}"] = [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].bPumpActivated",
                                                 f"Rkl/WtrSup/zone11/panel_{i}/bPumpActivated",
                                                 pyads.PLCTYPE_BOOL, Queue()]
    b6WValveActivated_dic[f"bPumpActivated_{i}"] = [f"GVL_WtrSupCC.stZone11_PanelSup[{i}].bPumpActivated",
                                                    f"Rkl/WtrSup/zone11/panel_{i}/b6WValveActivated",
                                                    pyads.PLCTYPE_BOOL, Queue()]
for j in range(15, 19):
    fCircSupTempAct_dic[f"fCircSupTempAct_{i}"] = [f"GVL_WtrSupCC.stZone11_SecSup[{j}].fCircSupTempAct",
                                                   f"Rkl/WtrSup/zone11/sec_{j}/fCircSupTempAct",
                                                   pyads.PLCTYPE_REAL, Queue()]
    fCircRtnTempAct_dic[f"fCircRtnTempAct_{i}"] = [f"GVL_WtrSupCC.stZone11_SecSup[{j}].fCircRtnTempAct",
                                                   f"Rkl/WtrSup/zone11/sec_{j}/fCircRtnTempAct",
                                                   pyads.PLCTYPE_REAL, Queue()]
    fMainSupTempAct_dic[f"fMainSupTempAct_{i}"] = [f"GVL_WtrSupCC.stZone11_SecSup[{j}].fMainSupTempAct",
                                                   f"Rkl/WtrSup/zone11/sec_{j}/fMainSupTempAct",
                                                   pyads.PLCTYPE_REAL, Queue()]
    fMainRtnTempAct_dic[f"fMainRtnTempAct_{i}"] = [f"GVL_WtrSupCC.stZone11_SecSup[{j}].fMainRtnTempAct",
                                                   f"Rkl/WtrSup/zone11/sec_{j}/fMainRtnTempAct",
                                                   pyads.PLCTYPE_REAL, Queue()]
    fPumpPowerSet_dic[f"fPumpPowerSet_{i}"] = [f"GVL_WtrSupCC.stZone11_SecSup[{j}].fPumpPowerSet",
                                               f"Rkl/WtrSup/zone11/sec_{j}/fPumpPowerSet",
                                               pyads.PLCTYPE_REAL, Queue()]
    fValveOpenSet_dic[f"fValveOpenSet_{i}"] = [f"GVL_WtrSupCC.stZone11_SecSup[{j}].fValveOpenSet",
                                               f"Rkl/WtrSup/zone11/sec_{j}/fValveOpenSet",
                                               pyads.PLCTYPE_REAL, Queue()]

panel_vars_list = [eCtrlState_dic, fSupTempAct_dic, fRtnTempAct_dic, fFlowrateAct_dic, f2WValveOpenSet_dic, 
                   bPumpActivated_dic, b6WValveActivated_dic]
sup_vars_list = [fCircSupTempAct_dic, fCircSupTempAct_dic, fCircRtnTempAct_dic, fMainSupTempAct_dic, fMainRtnTempAct_dic,
                 fPumpPowerSet_dic, fValveOpenSet_dic]
panel_names_list = ["eCtrlState_", "fSupTempAct_", "fRtnTempAct_", "fFlowrateAct_", "f2WValveOpenSet_",
                    "bPumpActivated_", "bPumpActivated_"]
sup_names_list = ["fCircSupTempAct_", "fCircRtnTempAct_", "fMainSupTempAct_", "fMainRtnTempAct_", "fPumpPowerSet_",
                  "fValveOpenSet_"]

connected = False
message_received = False
broker_address = "broker.emqx.io"
broker_port = 1883
# plc_address = "5.78.127.222.1.1"
# plc_port = 851


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        global connected
        connected = True
    else:
        print(f"failed with code {rc}")


client = mqtt.Client()
client.connect(broker_address, broker_port, 80)
client.on_connect = on_connect
# plc = pyads.Connection(plc_address, plc_port)
# plc.open()

while not connected:
    time.sleep(0.05)

# panel data published

for ii in range(7):
    for jj in range(15):
        panel_vars_list[ii][panel_names_list[ii] + f"{jj}"][3].put(1
        #     # plc.read_by_name(panel_vars_list[ii][panel_names_list[ii] + f"{jj}"][0],
        #     #                  panel_vars_list[ii][panel_names_list[ii] + f"{jj}"][1])
        )
        client.publish(panel_vars_list[ii][panel_names_list[ii] + f"{jj}"][1],
                       panel_vars_list[ii][panel_names_list[ii] + f"{jj}"][3].get())
# end = time.perf_counter()
#
# print(end - start)
