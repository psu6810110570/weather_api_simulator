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

    # รันแบบปกติ (ทำงานทีละเมือง)
def run_sequential(cities):
    print("\n--- 🐢 เริ่มการทำงานแบบปกติ (Sequential) ---")
    start_time = time.time()
    
    for city in cities:
        fetch_weather_data(city)
        
    print(f"--- 🐢 จบแบบปกติ ใช้เวลาทั้งหมด: {time.time() - start_time:.2f} วินาที ---\n")

    # รันแบบ Threading (ทำงานพร้อมกัน)
def run_threading(cities):
    print("--- 🚀 เริ่มการทำงานแบบ Threading ---")
    start_time = time.time()
    threads = []
    
    # สร้างและเริ่ม Thread ให้แต่ละเมือง
    for city in cities:
        t = threading.Thread(target=fetch_weather_data, args=(city,))
        threads.append(t)
        t.start()
        
    # รอให้ทุก Thread ทำงานเสร็จสมบูรณ์
    for t in threads:
        t.join()
        
    print(f"--- 🚀 จบแบบ Threading ใช้เวลาทั้งหมด: {time.time() - start_time:.2f} วินาที ---\n")

if __name__ == "__main__":
    target_cities = get_cities()
    
    run_sequential(target_cities)
    run_threading(target_cities)