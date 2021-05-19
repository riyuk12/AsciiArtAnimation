# AsciiArtAnimation
opencv python code to convert animations (or irl videos) to real time ascii art animation

to use-
get the code 
download a video and type video path in VideoCaptur()
or write VideoCapture(0) to use webcam


Steps -
code gets video 
scales down pixel count as per ratio(keep in mind ascii chr are longer than wide therefore change value as per need)
converts to grayscale (reduces bgr value to pixel intensity value (easier to use))
traverses every pixel and specify a ascii chr based on intensity
(add the ascii chr list in decending order of intensity)
(chr chosen by pixel intensity value/(max intensity/no of element in ascii list))
make string of all pixel value in a row
add "/n" (newline) per row
print string when frame is done
repeat
(to record it create txt file (do not use with open("abc.txt","w") as f as it wont work))

i made this for fun and dont know what to actually use it for .... :|
