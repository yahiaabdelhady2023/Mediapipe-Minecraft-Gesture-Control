import cv2

list_of_cameras = [0, 1]  # 0 for laptop webcam, 1 for external webcam
webcam = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not webcam.isOpened():
    print("Error: Could not open camera")
    exit()

while True:
    status, frame = webcam.read()

    if status:
        cv2.imshow("Camera Screen", frame)
        key = cv2.waitKey(1)  # Wait 1 millisecond

        if key == ord("q"):
            break
    else:
        print("Failed to grab frame")
        break

webcam.release() # release webcam object
cv2.destroyAllWindows()  # destroy window