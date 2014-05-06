import numpy as np
import cv2
from matplotlib import pyplot as plt
import pyaudio
import wave
import sys
import subprocess
from scipy.io.wavfile import read,write

def square(start, width):
    '''Returns a simulated square wave image with width 600 (the same as our webcam feed images)'''
    l = []
    for i in range(0,600):
        if i >= start and i < start + width:
            l.append(255)
        else:
            l.append(0)

    return np.array(l)

def polarize(a):
    '''Polarizes image to be black and white rather than grayscale
        allowing our frequency content to be cleaner'''
    array = np.copy(a)
    for i in range(len(array)):
        if array[i] >110:
            array[i] = 0
        else:
            array[i] = 255
    return array

def everyother(a):
    '''Selects every other value from a numpy array and returns
    a new array'''
    l = []
    for i in range(len(a)):
        if i%2==0:
            l.append(a[i])
    return np.array(l)

def reverse(a):
    '''Returns a new array containing the exact reversed contents
    of a numpy array'''
    l = []
    for i in range(len(a)):
        l.insert(0,a[i])
    return np.array(l)


CHUNK = 1024
cap = cv2.VideoCapture(0)
plt.ion()
j = 0
while(1):
    # Capture each frame from our webcam
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Polarize the middle row as our frequency content
    freq = polarize(gray[len(gray)/2]) 

    padding = 10000 # The number of padded zeros
    width = 600     # The width of our image (experimented with changing the expected width)
    extra = 6000    # The amount of "extra" we will keep from our padded waveform
                    # (padding - extra) represents the amount of the waveform cut off at the edges
    mid = 400       # The number of zeros between our frequency content and its reflection


    zeros = np.array([0]*padding)
    midzeros = np.array([0]*mid)

    #Test code to move a generated square wave across the screen
    #freq = square(j,1)
    #j = ((j+20) % 600)
    #print("j: "+str(j))

    freq = np.concatenate((zeros,freq,midzeros,reverse(freq),zeros),0)
    plt.clf()
    plt.subplot(121),plt.plot(freq[padding:padding+2*width+mid])

    # Select and "filter" our waveform
    time = np.fft.ifft(freq)
    time = time[padding-extra:padding+width+extra]
    time = everyother(time)


    plt.subplot(122),plt.plot(time)
    plt.draw()

    cv2.imshow('frame',gray)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    someSound = np.real(time)

    write("cam.wav",0,someSound)
    f = open("cam.wav","rb+")
    f.seek(0)

    #The Hexcode of the header to allow aplay to play our wav
    f.write(b'\x52\x49\x46\x46\x20\x4D\xF2\x00\x57\x41\x56\x45\x66\x6D\x74\x20 \
        \x10\x00\x00\x00\x01\x00\x01\x00\xFF\xFF\x00\x00\x10\xB1\x02\x00\x04 \
                                         #Rate AC44 = 44100 \
        \x00\x10\x00\x64\x61\x74\x61\xFC\x4C\xF2\x00')
    f.close()
    #aplay plays our wav file
    subprocess.call(["aplay","cam.wav"])
    
cap.release()
plt.close()
cv2.destroyAllWindows()
# When everything done, release the capture
