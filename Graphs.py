import numpy as np
import cv2
from matplotlib import pyplot as plt

def square(start, width):
    '''Returns a simulated square wave image with width 600 (the same as our webcam feed images)'''
    l = []
    for i in range(0,600):
        if i >= start and i < start + width:
            l.append(255)
        else:
            l.append(0)

    return np.array(l)

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



padding = 10000 
width = 600     
extra = -200  
mid = 400      
zeros = np.array([0]*padding)
midzeros = np.array([0]*mid)

freq = square(200,12)

freq = np.concatenate((zeros,freq,zeros),0)


time = np.fft.ifft(freq)

time = np.real(np.fft.ifft(freq))[padding-extra:padding+width+extra]
plt.subplot(121),plt.plot(time)
plt.title("Unfiltered Waveform")

e = everyother(time)
plt.subplot(122),plt.plot(e)
plt.axis([0,100,-.0015,.0015])
plt.title("Everyother Value Filtered")

plt.show()

padding = 10000 
width = 600     
extra = -200  
mid = 400      
zeros = np.array([0]*padding)
midzeros = np.array([0]*mid)

l = []
for i in range(600):
    if i >= 150 and i < 200:
        l.append(255)
    elif i>= 400 and i< 425:
        l.append(130)
    else:
        l.append(0)




freq = np.array(l)


plt.subplot(121),plt.plot(freq)
plt.title("Original Frequency Content")

freq = np.concatenate((freq,midzeros,reverse(freq)),0)

plt.subplot(122),plt.plot(freq)
plt.title("After Pitch is Raised")

plt.show()

plt.clf()

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

# Convert to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

freq = gray[len(gray)/2]

plt.subplot(121),plt.plot(freq)
plt.title("Original Image Data")

freq = polarize(freq) 

plt.subplot(122),plt.plot(freq)
plt.title("Polarized Frequency Content")

plt.show()

cap.release()
cv2.destroyAllWindows()

freq = np.array(l)

plt.subplot(221),plt.plot(freq)
plt.title("Original Frequency Content")

time = np.fft.ifft(freq)
freq = np.concatenate((zeros,freq,zeros),0)


plt.subplot(222),plt.plot(freq)
plt.title("Padded Frequency Content")

plt.axis([0,20600,0,300])

plt.subplot(223),plt.plot(time)
plt.title("Short Sound Waveform")


time = np.fft.ifft(freq)
plt.subplot(224),plt.plot(time)
plt.title("Elongated Sound Waveform")
plt.axis([0,20600,-.8,.8])


plt.show()


