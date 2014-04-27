import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import read,write


cap = cv2.VideoCapture(0)
plt.ion()
i = 0
while(i < 3):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    f = np.fft.fft2(gray)
    freq(i) = f[len(f)/2]
    time(i) = np.fft.ifft(freq(i))


    plt.subplot(121),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(gray, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.draw()
    '''
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    '''

    i=i+1

plt.close()
cap.release()
cv2.destroyAllWindows()

#fshift = np.fft.fftshift(f)
#magnitude_spectrum = 20*np.log(np.abs(fshift))

freq1 = freq(4)-freq(3)
time1 = time(4)-time(3)


someSound = np.real(time1)
print someSound
for i in range(0,len(f)):
	freq = f[i]
	time = np.fft.ifft(freq1)
	someSound = np.concatenate((someSound,np.real(time)),0)

write("colorMusic.wav",44100,someSound);

music = read("colorMusic.wav")
print music
plt.show()

#cv2.imshow('img',img)
#cv2.waitKey(5000)