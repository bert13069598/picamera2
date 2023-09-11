#!/usr/bin/python3

# Capture a PNG while still running in the preview mode.

from datetime import datetime
import time

from picamera2 import Picamera2, Preview

current_time = datetime.now()
formatted_time = current_time.strftime("%y%m%d_%H:%M")

picam2 = Picamera2()
# picam2.start_preview(Preview.QTGL)

preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

picam2.capture_file(f"/home/bert/Pictures/{formatted_time}.png")