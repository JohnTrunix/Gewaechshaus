#!/usr/bin/python3
import os

os.system("sudo rm -rf /var/www/html")
os.system("sudo cp -R /media/pi/SOFTWARE/interface/html /var/www")

os.system("sudo chown -R www-data:www-data /var/www")
os.system("sudo chmod -R 777 /var/www")


os.system("sudo rm /etc/gewaechshaus/*")
os.system("sudo cp -R /media/pi/SOFTWARE/scripts/* /etc/gewaechshaus/")

os.system("sudo chown -R pi:pi /etc/gewaechshaus")
os.system("sudo chmod +x /etc/gewaechshaus/*")