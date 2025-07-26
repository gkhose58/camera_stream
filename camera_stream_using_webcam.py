from webcam import Webcam
import cv2

def start_webcam_stream():
    # Initialize webcam (src=0 for default camera, w=640 for width)
    cam = Webcam(src=0, w=640)

    for frame in cam:
        # Display in OpenCV window (convert RGB to BGR for correct colors)
        cv2.imshow('Webcam Feed', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_webcam_stream()
