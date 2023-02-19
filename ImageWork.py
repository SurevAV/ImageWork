import numpy as np
import cv2 as cv
import zlib
from array import array

img = cv.imread('image2.jpg')

encode_param = [int(cv.IMWRITE_JPEG_QUALITY), 90]
result, encimg = cv.imencode('.jpg', img, encode_param)
cv.imwrite('5.jpg', img)

step = 20
Z = img.reshape((-1,3))
Z = np.float32(Z)

shape = img.shape
print(shape)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4

options = str(step)+'|'+str(shape[0])+'|'+str(shape[1])+'|'+str(K)

colors = []
numbers_colors = []
for i in range(0,len(Z),step):
    ret,label,center=cv.kmeans(Z[i:i+step],K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)

    for j in center:
        for color in j:
            colors.append(int(round(color)))
   
    for j in label:
        numbers_colors.append(j[0])
        

with open("numbers_colors", "wb") as binary_file:
    binary_file.write(zlib.compress(bytes(numbers_colors)))

with open("colors", "wb") as binary_file:
    binary_file.write(zlib.compress(bytes(colors)))
    
with open("options", "wb") as binary_file:
    binary_file.write(zlib.compress(options.encode('utf-8')))

#---------------------------------------------------------------------------

colors = open("colors", 'rb').read()
colors = list(zlib.decompress(colors))

numbers_colors = open("numbers_colors", 'rb').read()
numbers_colors = list(zlib.decompress(numbers_colors))


options = open("options", 'rb').read()
options = zlib.decompress(options)
options = options.decode('utf-8').split("|")

step = int(options[0])
y = int(options[1])
x = int(options[2])
K = int(options[3])

list_colors = []
for i in range(0, len(colors),K*3):
    
    item = colors[i:i+K*3]
    palette = []
    for j in range(0, len(item),3):
        palette.append(item[j:j+3])
    list_colors.append(palette)


    
    
img = []
for i in range(0, len(numbers_colors), step):
    numbers_items = numbers_colors[i:i+step]
    colors_items = list_colors[int(i/step)]

    for j in numbers_items:
        img += colors_items[j]
    
img = np.array(img, dtype ='uint8')
##img = img.reshape(y, x)

shape = (y,x,3)
img = img.reshape((shape))

cv.imshow('res2',img)
cv.waitKey(0)
cv.destroyAllWindows()



