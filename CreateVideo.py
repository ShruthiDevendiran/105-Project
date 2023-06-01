import os
import cv2

path = "/Images"
images = []

for file in os.listdir(path):
    file_name,ext = os.splitext(file)

    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path+"/"+file

    print(file_name)
    images.append(file_name)

count = len(images)
frame = cv2.imread(images[0])
width,height,channels = frame.shape
size = (width,height)
print(size)

out = cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0,count-1):
    image = cv2.imread(i)
    out.write(image)

print("Done")
