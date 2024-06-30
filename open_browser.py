#!/usr/bin/env python

import time
import datetime
import webbrowser
 # 1時間毎に任意のノートブックを開く

TARGET_URL="https://colab.research.google.com/drive/1Z3xI9CaOzpPO3lxNU-A4NRnhp8Ew94m3#scrollTo=Dkq5Z7ciiJDO"
for i in range(12):
    browse = webbrowser.get("chrome")
    browse.open(TARGET_URL)
    print(i, datetime.datetime.today())
    time.sleep(60*60)