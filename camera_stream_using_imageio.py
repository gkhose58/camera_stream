import imageio as iio
import matplotlib.pyplot as plt
import time

def start_camera_feed():
    # Get the camera reader object for the default webcam
    # On some systems, you might need to specify a different device like "<video1>"
    camera = iio.get_reader("<video0>")

    # Get metadata to calculate frame delay for real-time streaming
    meta = camera.get_meta_data()
    delay = 1 / meta.get("fps", 30) # Default to 30 fps if not available

    print("Streaming from webcam. Press Ctrl+C to stop.")

    try:
        while True:
            # Read the next frame from the camera
            frame = camera.get_next_data()

            # Display the frame (you can replace this with your desired processing)
            plt.imshow(frame)
            plt.axis('off') # Hide axes for cleaner display
            plt.pause(delay) # Pause for the calculated delay to maintain approximate FPS
            plt.clf() # Clear the figure for the next frame

    except KeyboardInterrupt:
        print("Streaming stopped by user.")
    finally:
        # Close the camera reader when done
        camera.close()
        plt.close()
if __name__ == "__main__":
    start_camera_feed()