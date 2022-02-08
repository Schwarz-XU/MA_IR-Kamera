import pyads

plc = pyads.Connection('5.78.127.222.1.1', 851)
# plc = pyads.Connection("169.254.147.21", 851)
plc.open()
print(plc)

while True:
    try:
        # Panel data
        for i in range(0, 15):
            # plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].eCtrlMode".format(nPanelIndex=i), "E_CtrlMode.Manual", pyads.PLCTYPE_STRING)
            plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].fFlowrateAct".format(nPanelIndex=i), pyads.PLCTYPE_REAL)
    except:
        break