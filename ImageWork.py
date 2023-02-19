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

##count = 0
##print(len(list_colors))
##for i in range(len(list_colors)):
##    for j in range(len(list_colors)):
##        if i !=j and list_colors[i] == list_colors[j]:
##            print(count)
##            count+=1

    
    
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
##print(options)
##string = ''
##for i in center:
##    string = string + str(round(i[0],1)) +'-'+str(round(i[1],1)) +'-'+  str(round(i[2],1)) +'|'
##string = string + '#'
##
##
##label2 = []
##for i in label:
##    string = string + str(i[0])
##    label2.append(i[0])
##
##print(label)
##
##label2 = bytes(label2)
##
##
##
##with open("image.c10", "wb") as binary_file:
##   
##    # Write bytes to file
##    binary_file.write(zlib.compress(string.encode('utf-8')))
##
##with open("label2.c10", "wb") as binary_file:
##   
##    # Write bytes to file
##    binary_file.write(zlib.compress(label2))
##
##    
##center = np.uint8(center)
##
##res = center[label.flatten()]
##res2 = res.reshape((img.shape))
##cv.imshow('res2',res2)
##cv.waitKey(0)
##cv.destroyAllWindows()
##
##
##
###-------------------------------------------------
##
##str_object1 = open("image.c10", 'rb').read()
##str_object2 = zlib.decompress(str_object1)
##
##image = str_object2.decode('utf-8').split("#")
##
##center = []
##for item in image[0].split("|")[:-1]:
##    center.append((item.split("-")))
##
##center = np.array(center,dtype = "float32")
##
##label= []
##for i in image[1]:
##    label.append(int(i))
##
##label = np.array(label,dtype = "int32")
##
##
##center = np.uint8(center)
##
##res = center[label]
##res2 = res.reshape((img.shape))
##cv.imshow('res2',res2)
##cv.waitKey(0)
##cv.destroyAllWindows()


