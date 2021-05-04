# aiy-camera-trap
Camera trap with the possibility to send a photo by email each time when object will be detected by using AIY Google Vision Pack.

### Instructions


```
# stop joy_detection_demo (default application in AIY Google Vision Pack)
sudo systemctl stop joy_detection_demo
# copy config in project directory and fill empty places
cd aiy-camera-trap
cp config.copy.yaml config.yaml
vim config.yaml
# start application
./aiy_camera_trap.py 
```

### Links

Free SMTP server:
- https://www.sendinblue.com/

AIY Google Vision Pack documentation:
- https://aiyprojects.withgoogle.com/vision
