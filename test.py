from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")
times = 0
mins_secs = ":00:00"

rijtje_1 = range(1, 13)
rijtje_2 = range(13, 25)

for i in rijtje_1:
    x = f"{i:02}"
    print(f"{x}{mins_secs} - {times}")
    if current_time == f"{x}{mins_secs}":
        times +=1

for i in rijtje_2:
    x = f"{i:02}"
    time_to_check = f"{x}{mins_secs}"
    print(f"{time_to_check} - {times}")
    if current_time == f"{x}{mins_secs}":
        times +=1

