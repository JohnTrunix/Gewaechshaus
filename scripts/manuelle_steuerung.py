# my_example.py
import argparse
import os
import time
from ansteuerung_pwm_shield import grundstellung
parser = argparse.ArgumentParser(description='Manuelle Ansteuerung')
parser.add_argument(
    '--stop',
    default=0,
    help='Wenn 1 -> System wird gestoppt und in Grundstellung positioniert.'
)
parser.add_argument(
    '--start',
    default=0,
    help='Wenn 1 -> System wird gestartet.'
)
parser.add_argument(
    '--herunterfahren',
    default=0,
    help='Wenn 1 -> System wird in gestoppt, in Grundstellung gebracht und heruntergefahren.'
)
arguments = parser.parse_args()
print(arguments.stop)
print(arguments.start)
print(arguments.herunterfahren)

if arguments.stop == 1:
    grundstellung()
    time.sleep(2)
    os.system("sudo service gewaechshaus stop")
elif arguments.start == 1:
    os.system("sudo service gewaechshaus stop")
    time.sleep(2)
    os.system("sudo service gewaechshaus start")
elif arguments.herunterfahren == 1:
    os.system("sudo service gewaechshaus stop")
    time.sleep(2)
    grundstellung()
    time.sleep(10)
    os.system("sudo shutdown -h now")
else:
    pass
