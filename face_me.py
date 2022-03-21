import cv2 as cv 
import mediapipe as mp 

mpdraw  = mp.solutions.drawing_utils
face_mesh = mp.solutions.face_mesh


capture = cv.VideoCapture(0)

while True:
	is_true, frame = capture.read()

	image = cv.cvtColor(cv.flip(frame, 1), cv.COLOR_BGR2RGB)
	image.flags.writeable = False
	results = face_mesh.process(image)    

	cv.imshow('frame', frame)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break 


capture.release()
cv.destroyAllWindows()