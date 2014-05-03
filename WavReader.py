import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import read,write
import subprocess
from matplotlib import pyplot as plt

music = read("DumbKid.wav")


sound = []
for i in range(len(music[1])):
    sound.append(music[1][i][0])

freq = np.fft.fft(sound)

plt.clf()
plt.subplot(122),plt.plot(freq)


plt.subplot(121),plt.plot(sound)
plt.show()

sound = np.array(sound)

write("DumbCopy.wav",44100,sound)

subprocess.call(["aplay","DumbCopy.wav"])