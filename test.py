from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")
times = 0
mins_secs = ":00:00"

pm_times = range(1, 13)
am_times = range(13, 25)

for i in pm_times:
    hour = f"{i:02}"
    print(f"{hour}{mins_secs} - {times}")
    if current_time == f"{hour}{mins_secs}":
        times +=1

for i in am_times:
    hour = f"{i:02}"
    print(f"{hour}{mins_secs} - {times}")
    if current_time == f"{hour}{mins_secs}":
        times +=1
