from PIL import Image
import glob

counter = 0
path = "D:/test/original/"
path_save = "D:/test/after/"

for image in glob.glob(path +"*.png"):
    counter = counter + 1
    img = Image.open(image)
    img1 = img.convert('RGB')
    img1.save(path_save + 'new_image'+ str(counter) +'.jpg','jpeg')
