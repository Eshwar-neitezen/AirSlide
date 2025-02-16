import cv2
import mediapipe as mp
import pyautogui


#initializing the model
#Using the 'Hand Module'

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode = False,
    model_complexity = 1,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5,
    max_num_hands = 1,
)

mp_drawing = mp.solutions.drawing_utils


#Capturing the video
cap = cv2.VideoCapture(0)

#To make the program work only for palm and not for back of the hand
def is_palm_facing_camera(hand_landmarks):
    wrist_z = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z
    middle_knuckle_z = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z
    fingertips_z = [
        hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].z,
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z,
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z,
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].z,
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].z,
    ]

    fingers_facing_camera = all(fingertip_z < wrist_z for fingertip_z in fingertips_z)

    knuckle_position = middle_knuckle_z > wrist_z

    return fingers_facing_camera and knuckle_position


while cap.isOpened():
    success, frame = cap.read()
    if not success:
       break


    frame = cv2.flip(frame, 1)  #Flip the video

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Convert the frame to rgb

    results = hands.process(frame_rgb)

   #Makes the program execute only for right hand
    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):

            hand_label = results.multi_handedness[idx].classification[0].label
            if hand_label == "Right" and is_palm_facing_camera(hand_landmarks):
                if results.multi_hand_landmarks:
                    print("Hand detected")
                else:
                    print("No hand detected");

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            if thumb_tip.y < index_tip.y:
                pyautogui.scroll(50)
            elif thumb_tip.y > index_tip.y:
                pyautogui.scroll(-50)

    cv2.imshow("Hand gesture scrolling", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


