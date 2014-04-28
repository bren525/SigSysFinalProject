import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import read,write


img = cv2.imread('thickv.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

f = np.fft.fft2(gray)
#fshift = np.fft.fftshift(f)
#magnitude_spectrum = 20*np.log(np.abs(fshift))

freq = f[len(f)/2]

plt.subplot(121),plt.plot(freq)

time = np.fft.ifft(freq)

plt.subplot(122),plt.plot(time)


someSound = np.real(time)
print someSound
for i in range(0,len(f)):
	freq = f[i]
	time = np.fft.ifft(freq)
	someSound = np.concatenate((someSound,np.real(time)),0)

write("colorMusic.wav",44000,someSound);

music = read("colorMusic.wav")
print music
plt.show()

#cv2.imshow('img',img)
#cv2.waitKey(5000)