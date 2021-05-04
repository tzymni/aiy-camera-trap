#!/usr/bin/env python3

#
# Send email when camera detect any object.
# @author Tomasz Zymni <tomasz.zymni@gmail.com>
#
import time
import yaml
from aiy.vision.inference import CameraInference
from aiy.vision.models import object_detection
from picamera import PiCamera
from email_sender import EmailSender

# Load configuration from yaml file.
def LoadConfig():
    global config

    with open("config.yaml", "r") as yamlfile:
        config = yaml.load(yamlfile, Loader=yaml.FullLoader)


# Main function to detect object, make photo and send an email.
def main():

    LoadConfig()
    with PiCamera() as camera:
        # Configure camera
        camera.resolution = (1640, 922)  # Full Frame, 16:9 (Camera v2)
        camera.start_preview()

        # Do inference on VisionBonnet
        with CameraInference(object_detection.model()) as inference:
            for result in inference.run():
                if len(object_detection.get_objects(result)) >= 1:
                    camera.capture(config['aiy']['photo_title'])
                    obj = EmailSender()
                    print("Found object! Send email...")
                    obj.SendMail(config['aiy']['photo_title'])
                    time.sleep(config['aiy']['time_between_emails'])

        # Stop preview
        camera.stop_preview()


if __name__ == '__main__':
    main()
