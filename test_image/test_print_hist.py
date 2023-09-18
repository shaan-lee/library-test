import json
import numpy as np 
import cv2
import matplotlib.pyplot as plt

f = open('./hist.txt','r')
hist = f.read()
hist = json.loads(hist)
print(hist)
plt.plot(hist)
plt.xlim([0,260])
plt.show()