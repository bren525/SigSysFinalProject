import numpy as np
import cv2
from matplotlib import pyplot as plt
import pyaudio
import wave
import sys
from scipy.io.wavfile import read,write

cap = cv2.VideoCapture(0)
plt.ion()
while(1):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    freq = gray[len(gray)/2]

    plt.subplot(121),plt.plot(freq)

    time = np.fft.ifft(freq)

    plt.subplot(122),plt.plot(time)
    plt.draw()


    someSound = np.real(time)
    print someSound
    for i in range(0,len(gray)):
    	#freq = f[i]
    	#time = np.fft.ifft(freq)
    	someSound = np.concatenate((someSound,np.real(time)),0)

    write("cam.wav",4410,someSound);

    wf = wave.open("cam.wav", 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(1),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()

plt.close()
cap.release()
cv2.destroyAllWindows()
# When everything done, release the capture
