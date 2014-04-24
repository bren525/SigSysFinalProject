import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('color.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

f = np.fft.fft2(gray)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

freq = magnitude_spectrum[len(magnitude_spectrum)/2]

plt.plot(freq)
plt.show()

time = np.fft.ffti(freq)

plt.plot(time)
plt.show()



#cv2.imshow('img',img)
#cv2.waitKey(5000)