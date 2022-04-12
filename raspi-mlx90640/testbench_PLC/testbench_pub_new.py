# testbench_pub_new.py
import paho.mqtt.client as mqtt
import pyads
from queue import Queue

plc_address = "5.78.127.222.1.1"
plc_port = 851
broker_address = "broker.emqx.io"
broker_port = 1883

# var. names set
# 0-14=panel, 15=sec. cw, 16=sec. hw, 17=pri. hw, 18=pri. cw
# IR-Calibration
fPT_dic = {"fPT1": Queue(), "fPT2": Queue()}
# pri. side
pri_fMainSupTempAct_dic = {"CW": Queue(), "HW": Queue()}
pri_fMainRtnTempAct_dic = {"CW": Queue(), "HW": Queue()}
pri_fCircSupTempAct_dic = {"CW": Queue(), "HW": Queue()}
pri_fCircRtnTempAct_dic = {"CW": Queue(), "HW": Queue()}
# sec. side
sec_z11_fMainSupTempAct_dic = {"CW": Queue(), "HW": Queue()}
sec_z11_fMainRtnTempAct_dic = {"CW": Queue(), "HW": Queue()}
sec_z11_fCircSupTempAct_dic = {"CW": Queue(), "HW": Queue()}
sec_z11_fCircRtnTempAct_dic = {"CW": Queue(), "HW": Queue()}
# wall
panel_eCtrlState_dic = {}
panel_fSurfTempActMovAvg_dic = {}
panel_fSupTempAct_dic = {}
panel_fRtnTempAct_dic = {}
panel_fFlowrateAct_dic = {}
panel_f2WValveOpenSet_dic = {}
panel_b6WValveActivate_dic = {}
panel_bPumpActivate_dic = {}
panel_bCWSupReq_dic = {}
panel_bHWSupReq_dic = {}
for m in range(15):
    panel_eCtrlState_dic[f"eCtrlState_{m}"] = Queue()
    panel_fSurfTempActMovAvg_dic[f"fSurfTempActMovAvg_{m}"] = Queue()
    panel_fSupTempAct_dic[f"fSupTempAct_{m}"] = Queue()
    panel_fRtnTempAct_dic[f"fRtnTempAct_{m}"] = Queue()
    panel_fFlowrateAct_dic[f"fFlowrateAct_{m}"] = Queue()
    panel_f2WValveOpenSet_dic[f"f2WValveOpenSet_{m}"] = Queue()
    panel_b6WValveActivate_dic[f"b6WValveActivate_{m}"] = Queue()
    panel_bPumpActivate_dic[f"bPumpActivate_{m}"] = Queue()
    panel_bCWSupReq_dic[f"bCWSupReq_{m}"] = Queue()
    panel_bHWSupReq_dic[f"bHWSupReq_{m}"] = Queue()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connect Success")
    else:
        print(f"Connected with result code {rc}")


def plc_connect(address, port):
    plc = pyads.Connection(address, port)
    plc.open()
    return plc


def publish(p_add, p_port, b_add, b_port):
    plc = plc_connect(p_add, p_port)
    while True:
        try:
            # establish connection
            client = mqtt.Client()
            client.on_connect = on_connect
            client.will_set("Rkl/testbench_pub/status", b'{"status": "off"}',
                            retain=True)  # Set will to find the status of publisher
            client.connect(b_add, b_port, 60)
            # read data from plc via. pyads, publish to MQTT broker
            # IR-Sensor calibration test
            fPT_dic["fPT1"].put(str(plc.read_by_name("PRG_WtrSupCC_Zone11.fCalibPT1", pyads.PLCTYPE_REAL)))
            fPT_dic["fPT2"].put(str(plc.read_by_name("PRG_WtrSupCC_Zone11.fCalibPT2", pyads.PLCTYPE_REAL)))
            client.publish('Rkl/WtrSup/zone11/test/pt1', payload=fPT_dic["fPT1"].get(), qos=0, retain=False)
            client.publish('Rkl/WtrSup/zone11/test/pt2', payload=fPT_dic["fPT2"].get(), qos=0, retain=False)
            # pri. side publisher
            # get data
            # 17=HW, 18=CW
            for k in range(17, 19):
                if k == 17:
                    pri_name = "HW"
                else:
                    pri_name = "CW"
                pri_fMainSupTempAct_dic[pri_name].put(
                    str(plc.read_by_name(
                        "GVL_WtrSupPri.stWtrSupPri[{nPriSysIndex}].fMainSupTempAct".format(nPriSysIndex=k),
                        pyads.PLCTYPE_REAL)))
                pri_fMainRtnTempAct_dic[pri_name].put(
                    str(plc.read_by_name(
                        "GVL_WtrSupPri.stWtrSupPri[{nPriSysIndex}].fMainRtnTempAct".format(nPriSysIndex=k),
                        pyads.PLCTYPE_REAL)))
                pri_fCircSupTempAct_dic[pri_name].put(
                    str(plc.read_by_name(
                        "GVL_WtrSupPri.stWtrSupPri[{nPriSysIndex}].fCircSupTempAct".format(nPriSysIndex=k),
                        pyads.PLCTYPE_REAL)))
                pri_fCircRtnTempAct_dic[pri_name].put(
                    str(plc.read_by_name(
                        "GVL_WtrSupPri.stWtrSupPri[{nPriSysIndex}].fCircRtnTempAct".format(nPriSysIndex=k),
                        pyads.PLCTYPE_REAL)))

                client.publish('Rkl/WtrSup/pri_{nPriSysIndex}/fMainSupTempAct'.format(nPriSysIndex=pri_name),
                               payload=pri_fMainSupTempAct_dic[pri_name].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/pri_{nPriSysIndex}/fMainRtnTempAct'.format(nPriSysIndex=pri_name),
                               payload=pri_fMainRtnTempAct_dic[pri_name].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/pri_{nPriSysIndex}/fCircSupTempAct'.format(nPriSysIndex=pri_name),
                               payload=pri_fCircSupTempAct_dic[pri_name].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/pri_{nPriSysIndex}/fCircRtnTempAct'.format(nPriSysIndex=pri_name),
                               payload=pri_fCircRtnTempAct_dic[pri_name].get(), qos=0, retain=False)

            # sec. side publisher
            # 15=CW, 16=HW
            for j in range(15, 17):
                if j == 15:
                    sec_name = "CW"
                else:
                    sec_name = "HW"
                sec_z11_fMainSupTempAct_dic[sec_name].put(
                    str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fMainSupTempAct".
                                         format(nSecSysIndex=j), pyads.PLCTYPE_REAL)))
                sec_z11_fMainRtnTempAct_dic[sec_name].put(
                    str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fMainRtnTempAct".
                                         format(nSecSysIndex=j), pyads.PLCTYPE_REAL)))
                sec_z11_fCircSupTempAct_dic[sec_name].put(
                    str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fCircSupTempAct".
                                         format(nSecSysIndex=j), pyads.PLCTYPE_REAL)))
                sec_z11_fCircRtnTempAct_dic[sec_name].put(
                    str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fCircRtnTempAct".
                                         format(nSecSysIndex=j), pyads.PLCTYPE_REAL)))

                client.publish('Rkl/WtrSup/zone11/sec_{nSecSysIndex}/fCircSupTempAct'.format(nSecSysIndex=sec_name),
                               payload=sec_z11_fCircSupTempAct_dic[sec_name].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/sec_{nSecSysIndex}/fCircRtnTempAct'.format(nSecSysIndex=sec_name),
                               payload=sec_z11_fCircRtnTempAct_dic[sec_name].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/sec_{nSecSysIndex}/fMainSupTempAct'.format(nSecSysIndex=sec_name),
                               payload=sec_z11_fMainSupTempAct_dic[sec_name].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/sec_{nSecSysIndex}/fMainRtnTempAct'.format(nSecSysIndex=sec_name),
                               payload=sec_z11_fMainRtnTempAct_dic[sec_name].get(), qos=0, retain=False)
            # wall publisher

            for i in range(0, 15):
                panel_eCtrlState_dic[f"eCtrlState_{i}"].put(str(plc.read_by_name(
                    "GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].eCtrlState".format(nPanelIndex=i),
                    pyads.PLCTYPE_INT)))
                panel_fSupTempAct_dic[f"fSupTempAct_{i}"].put(str(plc.read_by_name(
                    "GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].fSupTempAct".format(nPanelIndex=i),
                    pyads.PLCTYPE_REAL)))
                panel_fRtnTempAct_dic[f"fRtnTempAct_{i}"].put(str(plc.read_by_name(
                    "GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].fRtnTempAct".format(nPanelIndex=i),
                    pyads.PLCTYPE_REAL)))
                panel_fFlowrateAct_dic[f"fFlowrateAct_{i}"].put(str(plc.read_by_name(
                    "GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].fFlowrateAct".format(nPanelIndex=i),
                    pyads.PLCTYPE_REAL)))
                panel_f2WValveOpenSet_dic[f"f2WValveOpenSet_{i}"].put(str(plc.read_by_name(
                    "GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].f2WValveOpenSet".format(nPanelIndex=i),
                    pyads.PLCTYPE_REAL)))
                panel_b6WValveActivate_dic[f"b6WValveActivate_{i}"].put(str(plc.read_by_name(
                    "GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].b6WValveActivate".format(nPanelIndex=i),
                    pyads.PLCTYPE_BOOL)))
                panel_bPumpActivate_dic[f"bPumpActivate_{i}"].put(str(plc.read_by_name(
                    "GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].bPumpActivate".format(nPanelIndex=i),
                    pyads.PLCTYPE_BOOL)))
                panel_bCWSupReq_dic[f"bCWSupReq_{i}"].put(str(plc.read_by_name(
                    "GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].bCWSupReq".format(nPanelIndex=i),
                    pyads.PLCTYPE_BOOL)))
                panel_bHWSupReq_dic[f"bHWSupReq_{i}"].put(str(plc.read_by_name(
                    "GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].bHWSupReq".format(nPanelIndex=i),
                    pyads.PLCTYPE_BOOL)))

                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/eCtrlState'.format(nPanelIndex=i),
                               payload=panel_eCtrlState_dic[f"eCtrlState_{i}"].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/fSupTempAct'.format(nPanelIndex=i),
                               payload=panel_fSupTempAct_dic[f"fSupTempAct_{i}"].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/fRtnTempAct'.format(nPanelIndex=i),
                               payload=panel_fRtnTempAct_dic[f"fRtnTempAct_{i}"].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/fFlowrateAct'.format(nPanelIndex=i),
                               payload=panel_fFlowrateAct_dic[f"fFlowrateAct_{i}"].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/f2WValveOpenSet'.format(nPanelIndex=i),
                               payload=panel_f2WValveOpenSet_dic[f"f2WValveOpenSet_{i}"].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/b6WValveActivate'.format(nPanelIndex=i),
                               payload=panel_b6WValveActivate_dic[f"b6WValveActivate_{i}"].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/bPumpActivate'.format(nPanelIndex=i),
                               payload=panel_bPumpActivate_dic[f"bPumpActivate_{i}"].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/bCWSupReq'.format(nPanelIndex=i),
                               payload=panel_bCWSupReq_dic[f"bCWSupReq_{i}"].get(), qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/bHWSupReq'.format(nPanelIndex=i),
                               payload=panel_bHWSupReq_dic[f"bHWSupReq_{i}"].get(), qos=0, retain=False)
        except Exception as e:
            print(repr(e))


if __name__ == '__main__':
    publish(plc_address, plc_port, broker_address, broker_port)
