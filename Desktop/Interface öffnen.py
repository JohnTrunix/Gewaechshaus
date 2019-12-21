#!/usr/bin/python3
import os

os.system("chromium-browser http://localhost --incognito --kiosk --noerrdialogs --disable-translate --no-first-run --fast --fast-start --disable-infobars --disable-features=TranslateUI --disk-cache-dir=/dev/null")