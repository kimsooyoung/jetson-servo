#!/bin/bash
# Exit if we encounter an error
set -e
# Set permissions for us to access GPIO and I2C from user space
sudo ./scripts/setPermissions.sh $USER
# Then install servokit
sudo apt-get install python3-pip -y

sudo -H pip3 install adafruit-circuitpython-servokit
sudo -H pip3 install pip install pyserial
sudo -H pip3 install pip install asyncio
sudo -H pip3 install pip install inputs
echo ""
echo "Adafruit CircuitPython ServoKit installed."
echo "Please logoff/logon or reboot in order for I2C permissions to take effect."
echo ""
