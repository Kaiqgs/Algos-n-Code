from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import numpy as np

#Passo 0 - Parâmetros;
n_data = 300 #Número de dados;
coef_ang = 2 #Coeficiente angular;
coef_lin = 1 #Coeficiente linear;
passos_treino = 100

#Passo 1 - Gerar dados;
X = np.linspace(-1,1,n_data).reshape(-1,1).astype(np.float32) # X;
noise = np.random.normal(0,0.5, X.shape) # ruído;
y = (coef_ang * X - (coef_lin + noise)).astype(np.float32) # y;

#Passo 2 - Definir modelo;
modelo = Sequential()
modelo.add(Dense(1,input_dim=1))

#Passo 3 - Forma de otimizar;
otimizador = SGD(lr=0.1)

# Passo 4 - Treinar;
modelo.compile(loss='mean_squared_error', optimizer=otimizador, metrics=['mse'])
modelo.fit(X,y, batch_size = 300, epochs = 10)


# Passo 5 - Visualizar;
print(f"Coef angular = {coef_ang}, Coef linear = {coef_lin};")
print(f"Coef angular e linear encontrado = {modelo.get_weights()}")


