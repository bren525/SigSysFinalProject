import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import read,write
from wave import open as waveOpen

img = cv2.imread('singlebarcos.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

f = np.fft.ifft2(gray
)#fshift = np.fft.fftshift(f)
#magnitude_spectrum = 20*np.log(np.abs(fshift))

time = f[len(f)/2]

plt.subplot(121),plt.plot(time)

freq = np.fft.fft(time)

plt.subplot(122),plt.plot(freq)


someSound = np.real(time)
print someSound
for i in range(0,len(f)):
	time = f[i]
	someSound = np.concatenate((someSound,np.real(time)),0)

write("closecos.wav",44000,someSound);
