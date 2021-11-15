from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
img_array = np.array(img)
height = len(img_array)
width = len(img_array[1])
i = 0
while i < height:
    j = 0
    while j < width:
        middle_brightness = 0
        for x in range(i, i + 10):
            for y in range(j, j + 10):
                red = img_array[x][y][0]
                green = img_array[x][y][1]
                blue = img_array[x][y][2]
                brightness = (int(red) + int(green) + int(blue))/3
                middle_brightness += brightness
        middle_brightness = int(middle_brightness // 100)
        for x in range(i, i + 10):
            for y in range(j, j + 10):
                img_array[x][y][0] = int(middle_brightness // 50) * 50
                img_array[x][y][1] = int(middle_brightness // 50) * 50
                img_array[x][y][2] = int(middle_brightness // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(img_array)
res.save('res.jpg')
