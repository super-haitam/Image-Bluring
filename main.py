from PIL import Image
import numpy as np

print("Type the path of the image to blur as in C:/Users/Folder1/ImageName.jpg:")
imagePath = input()
im = Image.open(imagePath)

meansDict = {}

def getMean(y: int, x: int, arr: np.ndarray, step: int, size: int):
    global meansDict
    if meansDict.get(str(y) + " " + str(x)):
        return meansDict[str(y) + " " + str(x)]

    rList, gList, bList = [], [], []
    for j in range(y, y+step):
        for i in range(x, x+step):
            if j < size[0] and i < size[1]:
                rList.append(arr[j][i][0])
                gList.append(arr[j][i][1])
                bList.append(arr[j][i][2])

    r = sum(rList) / len(rList)
    g = sum(gList) / len(gList)
    b = sum(bList) / len(bList)

    meansDict[str(y) + " " + str(x)] = [r, g, b]
    return [r, g, b]


arr = np.array(im)
copyArr = np.array(im)

print("Type the size of each pixel after the bluring, it should be greater than 1.4% of max(width, height) to see a difference: ")
step: int = int(input())
print("It might take a little time but it's worth it !")

for j in range(im.height):
    for i in range(im.width):
        arr[j][i] = getMean(j-j%step, i-i%step, copyArr, step, (im.height, im.width))
print("DONE!")

print("Type the path of the blured image as in C:/Users/Folder1/Folder2/newImageName.jpg;")
newImPath = input()

newIm = Image.fromarray(arr, "RGB")
newIm.save(newImPath)
