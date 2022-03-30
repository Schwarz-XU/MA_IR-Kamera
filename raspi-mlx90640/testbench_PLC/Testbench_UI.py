# Testbench_UI.py
import sys
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
import paho.mqtt.client as mqtt
import paho

# broker_address = "broker.emqx.io"
# broker_port = 1883
broker_address = "72bcebd3aeb4444586a7c1152291630d.s1.eu.hivemq.cloud"
broker_port = 8883
# control_mode = [1, 2, 10, 20]

client = mqtt.Client(clean_session=True)
client.will_set("Rkl/testbench/launcher/status", payload="Status: OFF", retain=True)
app = QtWidgets.QApplication(sys.argv)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected to MQTT server")
    else:
        print(f"connect failed with code {rc}")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Rkl_testbench_launcher")

        # initial values
        self.ui.STset_1110.setValue(25)
        self.ui.STset_1120.setValue(25)
        self.ui.STset_1130.setValue(25)
        self.ui.STset_1140.setValue(25)
        self.ui.STset_1150.setValue(25)
        self.ui.STset_1160.setValue(25)
        self.ui.STset_121A.setValue(25)
        self.ui.STset_122A.setValue(25)
        self.ui.STset_123A.setValue(25)
        self.ui.STset_124A.setValue(25)
        self.ui.STset_125A.setValue(25)
        self.ui.STset_10L1.setValue(25)
        self.ui.STset_10S123.setValue(25)
        self.ui.STset_10L2.setValue(25)
        self.ui.STset_10L3.setValue(25)

        # click button action
        self.ui.bt_write_frontwall.clicked.connect(self.set_supply_temp_frontwall)
        self.ui.bt_write_frontwall.clicked.connect(self.set_control_mode_frontwall)

        self.ui.bt_write_sidewall.clicked.connect(self.set_supply_temp_sidewall)
        self.ui.bt_write_sidewall.clicked.connect(self.set_control_mode_sidewall)

        self.ui.bt_write_floor.clicked.connect(self.set_supply_temp_floor)
        self.ui.bt_write_floor.clicked.connect(self.set_control_mode_floor)
        # combobox action
        self.ui.CM_10X1.activated.connect(self.wall_control)
        self.ui.CM_11XX.activated.connect(self.wall_control)
        self.ui.CM_12XA.activated.connect(self.wall_control)

    def wall_control(self):
        #if (self.ui.CM_11XX.currentIndex() == i for i in control_mode):
        if self.ui.CM_11XX.currentIndex() != 3:
            self.ui.CM_1110.setCurrentIndex(self.ui.CM_11XX.currentIndex())
            self.ui.CM_1120.setCurrentIndex(self.ui.CM_11XX.currentIndex())
            self.ui.CM_1130.setCurrentIndex(self.ui.CM_11XX.currentIndex())
            self.ui.CM_1140.setCurrentIndex(self.ui.CM_11XX.currentIndex())
            self.ui.CM_1150.setCurrentIndex(self.ui.CM_11XX.currentIndex())
            self.ui.CM_1160.setCurrentIndex(self.ui.CM_11XX.currentIndex())
        else:
            self.ui.CM_1110.setCurrentIndex(self.ui.CM_1110.currentIndex())
            self.ui.CM_1120.setCurrentIndex(self.ui.CM_1120.currentIndex())
            self.ui.CM_1130.setCurrentIndex(self.ui.CM_1130.currentIndex())
            self.ui.CM_1140.setCurrentIndex(self.ui.CM_1140.currentIndex())
            self.ui.CM_1150.setCurrentIndex(self.ui.CM_1150.currentIndex())
            self.ui.CM_1160.setCurrentIndex(self.ui.CM_1160.currentIndex())
        if self.ui.CM_10X1.currentIndex() != 3:
            self.ui.CM_10L1.setCurrentIndex(self.ui.CM_10X1.currentIndex())
            self.ui.CM_10S123.setCurrentIndex(self.ui.CM_10X1.currentIndex())
            self.ui.CM_10L2.setCurrentIndex(self.ui.CM_10X1.currentIndex())
            self.ui.CM_10L3.setCurrentIndex(self.ui.CM_10X1.currentIndex())
        else:
            self.ui.CM_10L1.setCurrentIndex(self.ui.CM_10L1.currentIndex())
            self.ui.CM_10S123.setCurrentIndex(self.ui.CM_10S123.currentIndex())
            self.ui.CM_10L2.setCurrentIndex(self.ui.CM_10L2.currentIndex())
            self.ui.CM_10L3.setCurrentIndex(self.ui.CM_10L3.currentIndex())
        if self.ui.CM_12XA.currentIndex() != 3:
            self.ui.CM_121A.setCurrentIndex(self.ui.CM_12XA.currentIndex())
            self.ui.CM_122A.setCurrentIndex(self.ui.CM_12XA.currentIndex())
            self.ui.CM_123A.setCurrentIndex(self.ui.CM_12XA.currentIndex())
            self.ui.CM_124A.setCurrentIndex(self.ui.CM_12XA.currentIndex())
            self.ui.CM_125A.setCurrentIndex(self.ui.CM_12XA.currentIndex())
        else:
            self.ui.CM_121A.setCurrentIndex(self.ui.CM_121A.currentIndex())
            self.ui.CM_122A.setCurrentIndex(self.ui.CM_122A.currentIndex())
            self.ui.CM_123A.setCurrentIndex(self.ui.CM_123A.currentIndex())
            self.ui.CM_124A.setCurrentIndex(self.ui.CM_124A.currentIndex())
            self.ui.CM_125A.setCurrentIndex(self.ui.CM_125A.currentIndex())

    def set_control_mode_frontwall(self):
        control_mode_11xx = self.ui.CM_11XX.currentIndex()
        control_mode_1110 = self.ui.CM_1110.currentIndex()
        control_mode_1120 = self.ui.CM_1120.currentIndex()
        control_mode_1130 = self.ui.CM_1130.currentIndex()
        control_mode_1140 = self.ui.CM_1140.currentIndex()
        control_mode_1150 = self.ui.CM_1150.currentIndex()
        control_mode_1160 = self.ui.CM_1160.currentIndex()

        client.publish("Rkl/WtrSup/zone11/wall_11XX/eCtrlMode", control_mode_11xx, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_4/eCtrlMode", control_mode_1110, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_5/eCtrlMode", control_mode_1120, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_6/eCtrlMode", control_mode_1130, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_7/eCtrlMode", control_mode_1140, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_8/eCtrlMode", control_mode_1150, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_9/eCtrlMode", control_mode_1160, qos=0, retain=False)

    def set_control_mode_sidewall(self):
        control_mode_12xA = self.ui.CM_12XA.currentIndex()
        control_mode_121A = self.ui.CM_121A.currentIndex()
        control_mode_122A = self.ui.CM_122A.currentIndex()
        control_mode_123A = self.ui.CM_123A.currentIndex()
        control_mode_124A = self.ui.CM_124A.currentIndex()
        control_mode_125A = self.ui.CM_125A.currentIndex()

        client.publish("Rkl/WtrSup/zone11/wall_12XA/eCtrlMode", control_mode_12xA, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_10/eCtrlMode", control_mode_121A, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_11/eCtrlMode", control_mode_122A, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_12/eCtrlMode", control_mode_123A, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_13/eCtrlMode", control_mode_124A, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_14/eCtrlMode", control_mode_125A, qos=0, retain=False)

    def set_control_mode_floor(self):
        control_mode_10X1 = self.ui.CM_10X1.currentIndex()
        control_mode_10L1 = self.ui.CM_10L1.currentIndex()
        control_mode_10S123 = self.ui.CM_10S123.currentIndex()
        control_mode_10L2 = self.ui.CM_10L2.currentIndex()
        control_mode_10L3 = self.ui.CM_10L3.currentIndex()

        client.publish("Rkl/WtrSup/zone11/wall_10XX/eCtrlMode", control_mode_10X1, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_0/eCtrlMode", control_mode_10L1, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_1/eCtrlMode", control_mode_10S123, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_2/eCtrlMode", control_mode_10L2, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_3/eCtrlMode", control_mode_10L3, qos=0, retain=False)

    def set_supply_temp_frontwall(self):
        supply_temp_set_1110 = self.ui.STset_1110.value()
        supply_temp_set_1120 = self.ui.STset_1120.value()
        supply_temp_set_1130 = self.ui.STset_1130.value()
        supply_temp_set_1140 = self.ui.STset_1140.value()
        supply_temp_set_1150 = self.ui.STset_1150.value()
        supply_temp_set_1160 = self.ui.STset_1160.value()
        client.publish("Rkl/WtrSup/zone11/panel_4/fSupTempSet", supply_temp_set_1110, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_5/fSupTempSet", supply_temp_set_1120, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_6/fSupTempSet", supply_temp_set_1130, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_7/fSupTempSet", supply_temp_set_1140, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_8/fSupTempSet", supply_temp_set_1150, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_9/fSupTempSet", supply_temp_set_1160, qos=0, retain=False)

    def set_supply_temp_sidewall(self):
        supply_temp_set_121A = self.ui.STset_121A.value()
        supply_temp_set_122A = self.ui.STset_122A.value()
        supply_temp_set_123A = self.ui.STset_123A.value()
        supply_temp_set_124A = self.ui.STset_124A.value()
        supply_temp_set_125A = self.ui.STset_125A.value()
        client.publish("Rkl/WtrSup/zone11/panel_10/fSupTempSet", supply_temp_set_121A, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_11/fSupTempSet", supply_temp_set_122A, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_12/fSupTempSet", supply_temp_set_123A, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_13/fSupTempSet", supply_temp_set_124A, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_14/fSupTempSet", supply_temp_set_125A, qos=0, retain=False)

    def set_supply_temp_floor(self):
        supply_temp_set_10L1 = self.ui.STset_10L1.value()
        supply_temp_set_10S123 = self.ui.STset_10S123.value()
        supply_temp_set_10L2 = self.ui.STset_10L2.value()
        supply_temp_set_10L3 = self.ui.STset_10L3.value()
        client.publish("Rkl/WtrSup/zone11/panel_0/fSupTempSet", supply_temp_set_10L1, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_1/fSupTempSet", supply_temp_set_10S123, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_2/fSupTempSet", supply_temp_set_10L2, qos=0, retain=False)
        client.publish("Rkl/WtrSup/zone11/panel_3/fSupTempSet", supply_temp_set_10L3, qos=0, retain=False)


def run():
    client.on_connect = on_connect
    # enable TLS for secure connection
    client.tls_set(tls_version=paho.mqtt.client.ssl.PROTOCOL_TLS)
    # set username and password
    client.username_pw_set("MBP_minsheng", "Hive001601027")
    client.connect(broker_address, broker_port, 60)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    run()
