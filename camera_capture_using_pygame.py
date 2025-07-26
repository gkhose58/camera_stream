import pygame
import pygame.camera
from pygame.locals import *

def start_camera_feed():
    pygame.init()
    pygame.camera.init()

    # Get a list of available cameras
    camlist = pygame.camera.list_cameras()

    if camlist:
        # Select the first available camera (usually the default webcam)
        cam = pygame.camera.Camera(camlist[0], (640, 480)) # Specify resolution

        cam.start() # Start the camera feed

        # Capture a single image
        image = cam.get_image()

        # Save the image (optional)
        pygame.image.save(image, "webcam_capture.jpg")

        cam.stop() # Stop the camera feed
        print("Image captured and saved as webcam_capture.jpg")
    else:
        print("No cameras found.")

if __name__ == "__main__":
    start_camera_feed()