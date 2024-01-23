import cv2
import numpy as np

def webcam_background_filter(background_path):
    # Load the pre-trained Haar cascade for face detection from OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Create a VideoCapture object to get the video stream from the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video device")
        return

    # Attempt to read the background image
    background = cv2.imread(background_path)
    if background is None:
        print(f"Error: Could not read background image from {background_path}")
        cap.release()
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break

        # Resize background to match frame size
        scaled_background = cv2.resize(background, (frame.shape[1], frame.shape[0]))

        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Create a mask where the faces are not
        mask = np.zeros_like(frame)
        for (x, y, w, h) in faces:
            mask[y:y+h, x:x+w] = frame[y:y+h, x:x+w]

        # Invert the mask to get the background mask
        inv_mask = cv2.bitwise_not(mask)

        # Use the masks to extract the relevant parts from the frame and the background
        foreground = cv2.bitwise_and(frame, mask)
        background_only = cv2.bitwise_and(scaled_background, inv_mask)

        # Combine the foreground and the background to get the final frame
        combined = cv2.add(foreground, background_only)

        # Display the resulting frame
        cv2.imshow('Webcam - Face not Filtered', combined)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# Make sure the background path is correct and the image is accessible
webcam_background_filter('photo.png')