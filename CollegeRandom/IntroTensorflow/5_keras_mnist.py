from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, LeakyReLU
from tensorflow.keras.optimizers import RMSprop
from data_grabber import getData, shuffle, show
import numpy as np

#Passo 1: Pegar dados;
X,y = getData()
X,y = shuffle(X,y)

#Passo 2: Normalizar dados;
X = np.divide(X,255)

#Passo 3: Definindo modelo;
modelo = Sequential([Flatten(input_shape=X.shape[1:]),
					Dense(128),
					LeakyReLU(alpha=0.1),
					Dense(64),
					LeakyReLU(alpha=0.1),
					Dense(y.shape[1], activation='softmax')])

#Passo 4: Definir otimizador e compilar;
otimizador = RMSprop(lr=0.001)
modelo.compile(loss='categorical_crossentropy', optimizer=otimizador, metrics=['acc'])

#Passo 5: Treinar;
modelo.fit(X,y, batch_size = X.shape[0], epochs = 30,validation_split=0.2)

#Passo 6: Salvar;
modelo.save("modelo.h5")
