# auto_data_acq.py
import sys, os
sys.path.append(os.path.abspath("../"))
from testbench_PLC import surf_temp_calib
import paho.mqtt.client as mqtt
import time
from datetime import datetime


broker_address = "72bcebd3aeb4444586a7c1152291630d.s1.eu.hivemq.cloud"
broker_port = 8883

client = mqtt.Client(client_id="MBP_mxu", clean_session=True)
client.will_set("Rkl/testbench/launcher/status", payload="Status: OFF", retain=True)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected to MQTT server")
    else:
        print(f"connect failed with code {rc}")


def run():
    other_temp = 20
    targ_temp = 30
    client.on_connect = on_connect
    # enable TLS for secure connection
    client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
    # set username and password
    while True:
        try:
            client.username_pw_set("MBP_minsheng", "Hive001601027")
            client.connect(broker_address, broker_port, 7200)  # keep_alive must be greater than hold+write time?
            '''
            auto. publish plan:
                In every 50min:
                    1. adjust the supply temperature set of 1150, from 15°C to 45°C in step of 5 K
                    2. run the script surf_temp_calib.py (last about 10 min)
                After a cycle (15 - 45°C):
                    2. increase the supply temperature set of 10L1-3, 10X123, 1110-1140, 1160, 121A-125A by 15 K
            '''
            supply_temp_set_10L1 = other_temp
            supply_temp_set_10S123 = other_temp
            supply_temp_set_10L2 = other_temp
            supply_temp_set_10L3 = other_temp
            supply_temp_set_1110 = other_temp
            supply_temp_set_1120 = other_temp
            supply_temp_set_1130 = other_temp
            supply_temp_set_1140 = other_temp
            supply_temp_set_1150 = targ_temp
            supply_temp_set_1160 = other_temp
            supply_temp_set_121A = other_temp
            supply_temp_set_122A = other_temp
            supply_temp_set_123A = other_temp
            supply_temp_set_124A = other_temp
            supply_temp_set_125A = other_temp
            print(supply_temp_set_1150)
            client.publish("Rkl/WtrSup/zone11/panel_0/fSupTempSet", supply_temp_set_10L1, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_1/fSupTempSet", supply_temp_set_10S123, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_2/fSupTempSet", supply_temp_set_10L2, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_3/fSupTempSet", supply_temp_set_10L3, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_4/fSupTempSet", supply_temp_set_1110, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_5/fSupTempSet", supply_temp_set_1120, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_6/fSupTempSet", supply_temp_set_1130, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_7/fSupTempSet", supply_temp_set_1140, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_8/fSupTempSet", supply_temp_set_1150, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_9/fSupTempSet", supply_temp_set_1160, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_10/fSupTempSet", supply_temp_set_121A, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_11/fSupTempSet", supply_temp_set_122A, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_12/fSupTempSet", supply_temp_set_123A, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_13/fSupTempSet", supply_temp_set_124A, qos=0, retain=False)
            client.publish("Rkl/WtrSup/zone11/panel_14/fSupTempSet", supply_temp_set_125A, qos=0, retain=False)
            time.sleep(20 * 60)
            print("start writing data into .csv file")
            print(datetime.now())

            now = str(datetime.now().strftime("%m%d_%H%M"))
            print(now)
            file_name = "../Data/" + now + "_surf_temp_1150_rec.csv"
            stop_time = 10 * 60
            write_csv = surf_temp_calib.Write_to_csv(file_name, stop_time)
            write_csv.start_script()

            print("finish writing data into .csv file")
            targ_temp += 5
            print(targ_temp, supply_temp_set_1150)
            if supply_temp_set_1150 == 45:
                targ_temp = 15
                other_temp += 5
                if other_temp > 45:
                    other_temp = 15
            time.sleep(1 * 60)
            print("restart recording data")
        except Exception as e:
            print(repr(e))


if __name__ == '__main__':
    run()
