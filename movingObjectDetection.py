import cv2

# Create a background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

cap = cv2.VideoCapture(0)  # Use the default camera (usually index 0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Apply background subtraction to detect moving objects
    fgmask = fgbg.apply(frame)

    # Apply morphological operations to clean up the mask
    fgmask = cv2.erode(fgmask, None, iterations=2)
    fgmask = cv2.dilate(fgmask, None, iterations=2)

    # Find contours of the detected objects
    contours, _ = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around the detected objects
    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Adjust this threshold as needed
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with detected moving objects
    cv2.imshow('Moving Object Detection', frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
