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

    # ฟังก์ชันจำลองการดึงข้อมูลและแสดงผลลัพธ์
def fetch_weather_data(city):
    print(f"[{time.strftime('%H:%M:%S')}] ⏳ เริ่มดึงข้อมูลของ: {city}...")
    
    delay = simulate_network_delay()
    temp = random.randint(15, 35) # สุ่มอุณหภูมิ
    
    print(f"[{time.strftime('%H:%M:%S')}] ✅ {city}: อุณหภูมิ {temp}°C (ใช้เวลาโหลด {delay:.2f} วินาที)")