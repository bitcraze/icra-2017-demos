# E-stop button
Description

## Setting up UDEV rules
In order to get the permissions to access the Crazyradio PA a UDEV rule is used. Create the file ```/etc/udev/rules.d/99-crazyradio.rules``` with the following contents:
```
SUBSYSTEM=="usb", ATTRS{idVendor}=="1915", ATTRS{idProduct}=="7777", MODE=="0664", GROUP="plugdev"
```

## Autostart at boot
To autostart the script at startup you need to execute the following:
```
sudo cp estop /etc/init.d
sudo chmod 755 /etc/init.d
sudo update-rc.d estop defaults
```
