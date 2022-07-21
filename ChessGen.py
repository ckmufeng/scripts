import cv2
import numpy as np

height = 4096
width = 2360
length = 400
chess_height = 5
chess_width = 9
xoffset = 200
yoffset = 300

image = np.zeros((width,height),dtype = np.uint8)
image[:] = 255
print(image.shape[0],image.shape[1])

for i in range(chess_height):
    for j in range(chess_width):
        if((i+j)%2==1): continue
        for x in range(i*length, (i+1)*length):
            for y in range(j*length, (j+1)*length):
                nx = xoffset+x
                ny = yoffset+y
                if nx < width and ny < height:
                    image[nx,ny] = 0;

cv2.imwrite("chess.jpg",image)
cv2.imshow("chess",image)
cv2.waitKey(0)
