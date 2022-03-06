import time
import mysql.connector
from datetime import datetime
from DataAcquisition import sub

db = mysql.connector.connect(
    host='uelrkl.cvquuhppqhkb.eu-central-1.rds.amazonaws.com',
    user='admin',
    passwd='uelrkl123456',
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE rkl_temperature")
