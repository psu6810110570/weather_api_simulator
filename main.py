import threading
import time
import random

    # ฟังก์ชันคืนค่ารายชื่อเมืองที่ต้องการดึงข้อมูลสภาพอากาศ
def get_cities():
    return ["Bangkok", "Tokyo", "London", "New York", "Paris"]

def simulate_network_delay():
    # จำลองระยะเวลาการรอข้อมูลจาก Server (สุ่ม 1-3 วินาที)
    sleep_time = random.uniform(1, 3)
    time.sleep(sleep_time)
    return sleep_time