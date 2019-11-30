# my_example.py
import argparse
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
