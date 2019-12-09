import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#def add_layer(inputs, in_size, out_size, activation_function=None):

#Passo 0 - Parâmetros;
n_data = 300 #Número de dados;
coef_ang = 2 #Coeficiente angular;
coef_lin = 1 #Coeficiente linear;
passos_treino = 100

#Passo 1 - Gerar dados;
X = np.linspace(-1,1,n_data).reshape(-1,1).astype(np.float32) # X;
noise = np.random.normal(0,0.5, X.shape) # ruído;
y = (coef_ang * X - (coef_lin + noise)).astype(np.float32) # y;


#Passo 2 - Instanciar variáveis;
X_ = tf.placeholder(tf.float32,shape=(None,1)) # Recipiente para X;
y_ = tf.placeholder(tf.float32,shape=(None,1)) # Recipiente para y;
theta = tf.Variable(tf.random_normal([1,1]))
bias = tf.Variable(tf.zeros([1,1]) + 0.1)


#Passo 3 - Realizar operações;
prediction = tf.math.add(tf.matmul(X_,theta),bias)
loss = tf.reduce_mean(tf.square(prediction-y_))
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#Passo 4 - Inicializar variáveis;
init = tf.initializers.global_variables()
sess = tf.Session()
sess.run(init)

#Passo 5 - Treinar;
for i in range(passos_treino):
	sess.run(train,feed_dict={X_:X,y_:y})
	print(f"erro = {sess.run(loss,feed_dict={X_:X,y_:y})}")


#Passo 6 - Visualização;

print(f"Coef angular = {coef_ang}, Coef linear = {coef_lin};")
print(f"Coef angular encontrado = {sess.run(theta)}, Coef linear = {sess.run(bias)}")
print(f"Formato de X = {X.shape}, formato de y = {y.shape}")

#Passo 6.1 - Visualização(Opcional);
line = sess.run(prediction,feed_dict={X_:X,y_:y})
plt.scatter(X, y,zorder=1)
plt.plot(X,line,zorder=2,color='red')
plt.show()