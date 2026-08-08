# import required libraries
import cv2
import numpy as np
from PIL import ImageGrab

# Screen recording will be saved here
file_name = "recording.mp4"

# Grab the dimensions of the full screen
screen = ImageGrab.grab()
width, height = screen.size

# Define the video codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

print("Recording started... Press 'q' to stop.")

while True:
    # Capture the screen as a PIL image
    img = ImageGrab.grab()

    # Convert the PIL image to a NumPy array (BGR format for OpenCV)
    frame = np.array(img)

    # OpenCV expects BGR, but PIL gives RGB, so convert the colors
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write the frame to the video file
    video.write(frame)

    # Show the live preview window
    cv2.imshow("Screen Recorder", frame)

    # Stop recording when the 'q' key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release everything and close all windows
video.release()
cv2.destroyAllWindows()

print(f"Recording saved as {file_name}")
