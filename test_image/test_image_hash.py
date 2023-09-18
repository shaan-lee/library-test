from PIL import Image
import imagehash

img1 = Image.open('./i.png')
img1_hash = imagehash.average_hash(img1)
print(img1_hash)

img2 = Image.open('./matchTest1.png')
img2_hash = imagehash.average_hash(img2)
print(img2_hash)

similarity = img1_hash - img2_hash
print(similarity)