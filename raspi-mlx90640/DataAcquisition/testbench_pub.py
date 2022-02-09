# testbench_pub.py
import paho.mqtt.client as mqtt
import pyads


# publisher
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


def plc_connect(address):
    plc = pyads.Connection(address, 851)
    plc.open()
    return plc


if __name__ == "__main__":
    plc_address = "5.78.127.222.1.1"
    plc = plc_connect(plc_address)
    while True:
        try:
            # establish connection
            client = mqtt.Client()
            client.on_connect = on_connect
            client.will_set("raspberry/test/status", b'{"status": "off"}', retain=True)  # Set will to find the status of publisher
            client.connect("broker.emqx.io", 1883, 60)  # TODO: free server right now, replace it with institute's server later

            # read data from plc via. pyads
            # Zone 11
            # Panel data
            for i in range(0, 15):
                eCtrlState = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].eCtrlState".format(nPanelIndex=i), pyads.PLCTYPE_INT))  # TODO:check
                fSupTempAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].fSupTempAct".format(nPanelIndex=i), pyads.PLCTYPE_REAL))
                fRntTempAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].fRntTempAct".format(nPanelIndex=i), pyads.PLCTYPE_REAL))
                fFlowrateAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].fFlowrateAct".format(nPanelIndex=i), pyads.PLCTYPE_REAL))

                f2WValveOpenSet = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].f2WValveOpenSet".format(nPanelIndex=i), pyads.PLCTYPE_REAL))
                b6WValveActivate = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].b6WValveActivate".format(nPanelIndex=i), pyads.PLCTYPE_BOOL))
                bPumpActivate = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].bPumpActivate".format(nPanelIndex=i), pyads.PLCTYPE_BOOL))

                bCWSupReq = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].bCWSupReq".format(nPanelIndex=i), pyads.PLCTYPE_BOOL))
                bHWSupReq = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].bHWSupReq".format(nPanelIndex=i), pyads.PLCTYPE_BOOL))

                client.publish('Rkl/WtrSup/zone11/panel/eCtrlState', payload=eCtrlState, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel/fSupTempAct', payload=fSupTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel/fRtnTempAct', payload=fRntTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel/fFlowrateAct', payload=fFlowrateAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel/f2WValveOpenSet', payload=f2WValveOpenSet, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel/b6WValveActivate', payload=b6WValveActivate, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel/bPumpActivate', payload=bPumpActivate, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel/bCWSupReq', payload=bCWSupReq, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel/bHWSupReq', payload=bHWSupReq, qos=0, retain=False)

            # Secondary side data
            for j in range(15, 17):
                fCircSupTempAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fCircSupTempAct".format(nSecSysIndex=j), pyads.PLCTYPE_REAL))
                fCircRtnTempAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fCircRtnTempAct".format(nSecSysIndex=j), pyads.PLCTYPE_REAL))
                fMainSupTempAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fMainSupTempAct".format(nSecSysIndex=j), pyads.PLCTYPE_REAL))
                fMainRtnTempAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fMainRtnTempAct".format(nSecSysIndex=j), pyads.PLCTYPE_REAL))

                fValveOpenSet = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fValveOpenSet".format(nSecSysIndex=j), pyads.PLCTYPE_REAL))
                fPumpPowerSet = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fPumpPowerSet".format(nSecSysIndex=j), pyads.PLCTYPE_REAL))

                bHeatingSystem = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].bHeatingSystem".format(nSecSysIndex=j), pyads.PLCTYPE_BOOL))

                client.publish('Rkl/WtrSup/zone11/secondary/fCircSupTempAct', payload=fCircSupTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/secondary/fCircRtnTempAct', payload=fCircRtnTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/secondary/fMainSupTempAct', payload=fMainSupTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/secondary/fMainRtnTempAct', payload=fMainRtnTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/secondary/fValveOpenSet', payload=fValveOpenSet, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/secondary/fPumpPowerSet', payload=fPumpPowerSet, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/secondary/bHeatingSystem', payload=bHeatingSystem, qos=0, retain=False)
        except:
            break