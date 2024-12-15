<<<<<<< HEAD
import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Define gesture recognition
def recognize_gesture(landmarks):
    # Gesture for Thumbs Up
    # Thumb is extended upwards, other fingers curled inwards
    if landmarks[4].y < landmarks[3].y and \
       landmarks[8].y > landmarks[6].y and \
       landmarks[12].y > landmarks[10].y and \
       landmarks[16].y > landmarks[14].y and \
       landmarks[20].y > landmarks[18].y:
        return "Thumbs Up"

    # Gesture for Peace Sign
    # Index and middle fingers extended, other fingers curled
    elif landmarks[4].y < landmarks[3].y and  \
         landmarks[8].y < landmarks[6].y and \
         landmarks[12].y < landmarks[10].y and \
         landmarks[16].y < landmarks[14].y and \
         landmarks[20].y < landmarks[18].y:
         return "Peace Sign"

    # If no known gesture, return None
    return None

# Map gestures to contacts
def map_gesture_to_contact(gesture):
    gesture_map = {
        "Thumbs Up": "Rakesh",
        "Peace Sign": "John"
    }
    return gesture_map.get(gesture, None)

# Mock function for video call initiation
def initiate_video_call(contact_name):
    print(f"Initiating video call to {contact_name}...")
    # Integrate WebRTC API to actually start the call
    # e.g., webRTC_api.start_call(contact_name)

# Start webcam feed
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    contact_to_call = None
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            gesture = recognize_gesture(hand_landmarks.landmark)
            if gesture:
                contact_to_call = map_gesture_to_contact(gesture)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if contact_to_call:
        # Show "Calling: {contact_name}" if a recognized gesture is detected
        cv2.putText(frame, f"Calling: {contact_to_call}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        initiate_video_call(contact_to_call)
    else:
        # If no gesture or an unrecognized gesture is detected, don't show anything
        cv2.putText(frame, "", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
=======
import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Define gesture recognition
def recognize_gesture(landmarks):
    # Gesture for Thumbs Up
    # Thumb is extended upwards, other fingers curled inwards
    if landmarks[4].y < landmarks[3].y and \
       landmarks[8].y > landmarks[6].y and \
       landmarks[12].y > landmarks[10].y and \
       landmarks[16].y > landmarks[14].y and \
       landmarks[20].y > landmarks[18].y:
        return "Thumbs Up"

    # Gesture for Peace Sign
    # Index and middle fingers extended, other fingers curled
    elif landmarks[4].y < landmarks[3].y and  \
         landmarks[8].y < landmarks[6].y and \
         landmarks[12].y < landmarks[10].y and \
         landmarks[16].y < landmarks[14].y and \
         landmarks[20].y < landmarks[18].y:
         return "Peace Sign"

    # If no known gesture, return None
    return None

# Map gestures to contacts
def map_gesture_to_contact(gesture):
    gesture_map = {
        "Thumbs Up": "Rakesh",
        "Peace Sign": "John"
    }
    return gesture_map.get(gesture, None)

# Mock function for video call initiation
def initiate_video_call(contact_name):
    print(f"Initiating video call to {contact_name}...")
    # Integrate WebRTC API to actually start the call
    # e.g., webRTC_api.start_call(contact_name)

# Start webcam feed
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    contact_to_call = None
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            gesture = recognize_gesture(hand_landmarks.landmark)
            if gesture:
                contact_to_call = map_gesture_to_contact(gesture)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if contact_to_call:
        # Show "Calling: {contact_name}" if a recognized gesture is detected
        cv2.putText(frame, f"Calling: {contact_to_call}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        initiate_video_call(contact_to_call)
    else:
        # If no gesture or an unrecognized gesture is detected, don't show anything
        cv2.putText(frame, "", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
>>>>>>> a339932 (Initial commit)
