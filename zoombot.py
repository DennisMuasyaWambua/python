import webbrowser
import schedule
import time

def hci():
    print("Fetching...................")

schedule.every(5).seconds.do(hci);

while True:
    schedule.run_pending()
    time.sleep(1)
