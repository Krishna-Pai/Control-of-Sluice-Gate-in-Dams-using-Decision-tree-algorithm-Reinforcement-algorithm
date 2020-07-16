from keras.models import Sequential
from keras.layers import Dense
import numpy
numpy.random.seed(7)
dataset = numpy.loadtxt('pima-indians-diabetes.data.csv',delimiter=",")
X = dataset[:,0:8]
Y = dataset[:,8]
model=Sequential()
model.add(Dense(units=12,input_dim=8,activation='relu'))
model.add(Dense(units=8,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X,Y,epochs=150,batch_size=10,verbose=1)
scores=model.evaluate(X,Y)
print(scores)

