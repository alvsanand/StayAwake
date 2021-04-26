from datetime import datetime, timedelta
from time import sleep

from pyautogui import press
from PyQt5.QtCore import QThread

from StayAwake import logger, set_keepawake, unset_keepawake


class PreventSleep(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.stopped = False

    # "Prevent sleep" method presses f24 key every 60 seconds to prevent sleep
    def run(self):
        logger.info("Init PreventSleep")

        try:
            set_keepawake()
            logger.info("Executed set_keepawake")

            last_press_time = datetime.now()
            while not self.stopped:
                current_time = datetime.now()

                if last_press_time + timedelta(minutes=1) < current_time:
                    press('f24')  # press f24 key to prevent sleep
                    logger.info("Press key")

                    last_press_time = current_time

                sleep(0.5)

            unset_keepawake()
            logger.info("Executed unset_keepawake")
        except:
            pass

        logger.info("Finish PreventSleep")

    def stop(self):
        self.stopped = True
