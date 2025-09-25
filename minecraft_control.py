import mediapipe as mp
import os
import cv2



# os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMATIONS"]="0"



#Setting up Mediapipe

mp_drawings=mp.solutions.drawing_utils #draw lines connecting landmarks/vertices
mp_hands=mp.solutions.hands
hands = mp_hands.Hands()


list_of_cameras = [0, 1]  # 0 for laptop webcam, 1 for external webcam
webcam = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not webcam.isOpened():
    print("Error: Could not open camera")
    exit()

while True:
    status, frame = webcam.read() #frame is given in BGR not RGB
    if status:
        #Flipping image to convert mirror image into selfie image
        frame=cv2.cvtColor(cv2.flip(frame,1),cv2.COLOR_BGR2RGB) #Mediapipe expects RGB instead of BGR
        
        results=hands.process(frame)

        if results.multi_hand_landmarks: #check if it has any landmarks
            for hand_landmarks in results.multi_hand_landmarks:
                print(hand_landmarks.landmark)
                mp_drawings.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )
        frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR) #convert back to BGR so it be displayed via Cv2
        frame = cv2.imshow("Camera Screen", frame)
        key = cv2.waitKey(1)  # Wait 1 millisecond

        if key == ord("q"):
            break
    else:
        print("Failed to grab frame")
        break

webcam.release() # release webcam object
cv2.destroyAllWindows()  # destroy window