from datetime import datetime
import time

for _ in range(5):
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)