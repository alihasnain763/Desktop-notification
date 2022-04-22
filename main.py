from http.client import NOT_MODIFIED
import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water right Now........",
            message = """carrying nutrients and oxygen to your cells
                        flushing bacteria your bladder aiding digestion preventing 
                        constipation normalizing blood pressure stabilizing the heartbeat""",
            app_icon= "D:/python program desktop notification/icon.ico",
            timeout = 15)

        time.sleep(60*60)
