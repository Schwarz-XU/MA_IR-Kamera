# testbench_pub.py
import paho.mqtt.client as mqtt
import pyads

plc_address = "5.78.127.222.1.1"
plc_port = 851
broker_address = "mqtt.eclipseprojects.io"
broker_port = 1883


# publisher
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connect success")
    else:
        print(f"Connected with result code {rc}")


def plc_connect(address, port):
    plc = pyads.Connection(address, port)
    plc.open()
    return plc


def publish(plc_address, plc_port):
    plc = plc_connect(plc_address, plc_port)
    while True:
        try:
            # establish connection
            client = mqtt.Client()
            client.on_connect = on_connect
            client.will_set("Rkl/testbench_pub/status",
                            b'{"status": "off"}',
                            retain=True)  # Set will to find the status of publisher
            client.connect(broker_address, broker_port, 60)
            # read data from plc via. pyads, publish to the MQTT broker
            # Zone 11
            # Panel data
            for i in range(0, 15):
                eCtrlState = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].eCtrlState"
                                                  .format(nPanelIndex=i), pyads.PLCTYPE_INT))  # TODO:check
                fSupTempAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].fSupTempAct"
                                                   .format(nPanelIndex=i), pyads.PLCTYPE_REAL))
                fRntTempAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].fRntTempAct"
                                                   .format(nPanelIndex=i), pyads.PLCTYPE_REAL))
                fFlowrateAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].fFlowrateAct"
                                                    .format(nPanelIndex=i), pyads.PLCTYPE_REAL))

                f2WValveOpenSet = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].f2WValveOpenSet"
                                                       .format(nPanelIndex=i), pyads.PLCTYPE_REAL))
                b6WValveActivate = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].b6WValveActivate"
                                                        .format(nPanelIndex=i), pyads.PLCTYPE_BOOL))
                bPumpActivate = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].bPumpActivate"
                                                     .format(nPanelIndex=i), pyads.PLCTYPE_BOOL))

                bCWSupReq = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].bCWSupReq"
                                                 .format(nPanelIndex=i), pyads.PLCTYPE_BOOL))
                bHWSupReq = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].bHWSupReq"
                                                 .format(nPanelIndex=i), pyads.PLCTYPE_BOOL))

                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/eCtrlState'.format(nPanelIndex=i),
                               payload=eCtrlState, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/fSupTempAct'.format(nPanelIndex=i),
                               payload=fSupTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/fRtnTempAct'.format(nPanelIndex=i),
                               payload=fRntTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/fFlowrateAct'.format(nPanelIndex=i),
                               payload=fFlowrateAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/f2WValveOpenSet'.format(nPanelIndex=i),
                               payload=f2WValveOpenSet, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/b6WValveActivate'.format(nPanelIndex=i),
                               payload=b6WValveActivate, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/bPumpActivate'.format(nPanelIndex=i),
                               payload=bPumpActivate, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/bCWSupReq'.format(nPanelIndex=i),
                               payload=bCWSupReq, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/panel_{nPanelIndex}/bHWSupReq'.format(nPanelIndex=i),
                               payload=bHWSupReq, qos=0, retain=False)

            # Secondary side data
            # get data
            for j in range(15, 17):
                fSecCircSupTempAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fCircSupTempAct"
                                                          .format(nSecSysIndex=j), pyads.PLCTYPE_REAL))
                fSecCircRtnTempAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fCircRtnTempAct"
                                                          .format(nSecSysIndex=j), pyads.PLCTYPE_REAL))
                fSecMainSupTempAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fMainSupTempAct"
                                                          .format(nSecSysIndex=j), pyads.PLCTYPE_REAL))
                fSecMainRtnTempAct = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fMainRtnTempAct"
                                                          .format(nSecSysIndex=j), pyads.PLCTYPE_REAL))

                fSecValveOpenSet = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fValveOpenSet"
                                                        .format(nSecSysIndex=j), pyads.PLCTYPE_REAL))
                fSecPumpPowerSet = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].fPumpPowerSet"
                                                        .format(nSecSysIndex=j), pyads.PLCTYPE_REAL))

                bSecHeatingSystem = str(plc.read_by_name("GVL_WtrSupCC.stZone11_SecSup[{nSecSysIndex}].bHeatingSystem"
                                                         .format(nSecSysIndex=j), pyads.PLCTYPE_BOOL))
                # publish data to broker
                if j == 15:
                    sec_name = "CW"
                else:
                    sec_name = "HW"

                client.publish('Rkl/WtrSup/zone11/sec_{nSecSysIndex}/fCircSupTempAct'.format(nSecSysIndex=sec_name),
                               payload=fSecCircSupTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/sec_{nSecSysIndex}/fCircRtnTempAct'.format(nSecSysIndex=sec_name),
                               payload=fSecCircRtnTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/sec_{nSecSysIndex}/fMainSupTempAct'.format(nSecSysIndex=sec_name),
                               payload=fSecMainSupTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/sec_{nSecSysIndex}/fMainRtnTempAct'.format(nSecSysIndex=sec_name),
                               payload=fSecMainRtnTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/sec_{nSecSysIndex}/fValveOpenSet'.format(nSecSysIndex=sec_name),
                               payload=fSecValveOpenSet, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/sec_{nSecSysIndex}/fPumpPowerSet'.format(nSecSysIndex=sec_name),
                               payload=fSecPumpPowerSet, qos=0, retain=False)
                client.publish('Rkl/WtrSup/zone11/sec_{nSecSysIndex}/bHeatingSystem'.format(nSecSysIndex=sec_name),
                               payload=bSecHeatingSystem, qos=0, retain=False)

            # Primary side data
            # get data
            for k in range(0, 2):
                fPriCircSupTempAct = str(plc.read_by_name("GVL_WtrSupPri.stWtrPriSup[{nPriSysIndex}].fCircSupTempAct"
                                                          .format(nPriSysIndex=k), pyads.PLCTYPE_REAL))
                fPriCircRtnTempAct = str(plc.read_by_name("GVL_WtrSupPri.stWtrPriSup[{nPriSysIndex}].fCircRtnTempAct"
                                                          .format(nPriSysIndex=k), pyads.PLCTYPE_REAL))
                fPriMainSupTempAct = str(plc.read_by_name("GVL_WtrSupPri.stWtrPriSup[{nPriSysIndex}].fMainSupTempAct"
                                                          .format(nPriSysIndex=k), pyads.PLCTYPE_REAL))
                fPriMainRtnTempAct = str(plc.read_by_name("GVL_WtrSupPri.stWtrPriSup[{nPriSysIndex}].fMainRtnTempAct"
                                                          .format(nPriSysIndex=k), pyads.PLCTYPE_REAL))
                fPriValveOpenSet = str(plc.read_by_name("GVL_WtrSupPri.stWtrPriSup[{nPriSysIndex}].fValveOpenSet"
                                                        .format(nPriSysIndex=k), pyads.PLCTYPE_REAL))
                fPriPumpPowerSet = str(plc.read_by_name("GVL_WtrSupPri.stWtrPriSup[{nPriSysIndex}].fPumpPowerSet"
                                                        .format(nPriSysIndex=k), pyads.PLCTYPE_REAL))
                # publish data to broker
                if k == 0:
                    pri_name = "CW"
                else:
                    pri_name = "HW"

                client.publish('Rkl/WtrSup/pri_{nPriSysIndex}/fCircSupTempAct'.format(nPriSysIndex=pri_name),
                               payload=fPriCircSupTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/pri_{nPriSysIndex}/fCircRtnTempAct'.format(nPriSysIndex=pri_name),
                               payload=fPriCircRtnTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/pri_{nPriSysIndex}/fMainSupTempAct'.format(nPriSysIndex=pri_name),
                               payload=fPriMainSupTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/pri_{nPriSysIndex}/fMainRtnTempAct'.format(nPriSysIndex=pri_name),
                               payload=fPriMainRtnTempAct, qos=0, retain=False)
                client.publish('Rkl/WtrSup/pri_{nPriSysIndex}/fValveOpenSet'.format(nPriSysIndex=pri_name),
                               payload=fPriValveOpenSet, qos=0, retain=False)
                client.publish('Rkl/WtrSup/pri_{nPriSysIndex}/fPumpPowerSet'.format(nPriSysIndex=pri_name),
                               payload=fPriPumpPowerSet, qos=0, retain=False)
        except Exception as e:
            print(repr(e))
        else:
            print("Publish system is running")


if __name__ == "__main__":
    publish(plc_address, plc_port)
