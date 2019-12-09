import glob
import cv2
import numpy as np
import random

data_folder = "mnist_dados/"

def getData():
	X = []
	y = []
	for folder in glob.glob(data_folder + "*"):
		y_ = np.zeros((10))
		y_[(int(folder[len(folder)-1]))] = 1
		for image in glob.glob(folder + "//*.png"):
			X.append(cv2.imread(image,0))
			y.append(y_.copy())
		
	return np.array(X), np.array(y)

#https://stackoverflow.com/questions/13343347/randomizing-two-lists-and-maintaining-order-in-python
def shuffle(a,b):
	combined = list(zip(a,b))
	random.shuffle(combined)
	a[:], b[:] = zip(*combined)
	return a,b

def show(im,txt=True):
	if txt:
		for row in im:
			for val in row:
				print('0' if val>1 else '-' ,end=' ')
			print('')
if __name__ == '__main__':
	print(getData())