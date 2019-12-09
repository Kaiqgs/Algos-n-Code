from tensorflow.keras.models import load_model
import cv2
import numpy as np

#Passo 0:
im = cv2.imread("input.png",0)/255
im = im.reshape((1,)+im.shape)

# Passo 1: Carregar modelo;
modelo = load_model("modelo.h5")
modelo.summary()

# Passo 2: Fazer a previsão;
print(modelo.predict(im))
print(np.argmax(modelo.predict(im)))

