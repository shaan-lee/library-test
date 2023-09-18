import json
from json import JSONEncoder
import numpy as np 
import cv2
import matplotlib.pyplot as plt

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

img_path = "./screenShotTest1.png"
def histogram():
    img1 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img_path)
    
    hist1 = cv2.calcHist([img1],[0],None, [256],[0,256])
    
    hist2, bins = np.histogram(img1.ravel(), 256,[0,256])
    
    hist3 = np.bincount(img1.ravel(), minlength=256)
    
    plt.hist(img1.ravel(), 256, [0,256])
    
    color = ("b","g","r")
    for i, col in enumerate(color):
        hist = cv2.calcHist([img2],[i],None,[256],[0,256])
        f = open('./hist.txt','w')
        f.write(json.dumps(hist,cls = NumpyArrayEncoder))
        f.close()
        plt.plot(hist,color=col)
        plt.xlim([0,260])
        
histogram()
plt.show()