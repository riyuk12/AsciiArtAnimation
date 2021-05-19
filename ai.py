import cv2 as cv
import time

asc=["@","$","*","^","-","."," "]
cam=cv.VideoCapture("zhongli.mp4")

while True:
	suc,frame=cam.read()

	gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

	scale=12

	width_percent=(12/19)*scale
	height_percent=(7/19)*scale

	width=int(gray.shape[1]*width_percent/100)
	height=int(gray.shape[0]*height_percent/100)
	smolgray=cv.resize(gray,(width,height))

	x="\n".join(["".join([asc[smolgray[y,x]//38] for x in range(0,width)]) for y in range(0,height)])
	print(x)

	if cv.waitKey(1)==ord("x"):
		break
	
cam.release()
cv.destroyAllWindows()