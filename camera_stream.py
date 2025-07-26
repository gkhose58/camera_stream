import cv2

def start_camera_feed():
    # Create a VideoCapture object to access the default camera (index 0)
    # If you have multiple cameras, you might need to try other indices like 1, 2, etc.
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # If the frame was not read successfully, break the loop
        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the captured frame in a window named 'Camera Feed'
        cv2.imshow('Camera Feed', frame)

        # Wait for 1 millisecond and check for a key press
        # If 'q' is pressed, break the loop to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and destroy all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_camera_feed()