import cv2
import numpy as np

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    icon=cv2.imread('rock.png')
    icon=cv2.resize(icon,(400,400))
	 frame[100:500, 800:1200]=icon

	cv2.imshow("Rock Paper Scissors", frame)

	k = cv2.waitKey(10)
	if k == ord('q'):
	    break

cap.release()
cv2.destroyAllWindows