import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.io.wavfile import read,write

music = read("DumbKid.wav")
print music