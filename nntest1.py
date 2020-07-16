from keras.models import Sequential
from keras.layers import Dense
import numpy
import pandas as pd
numpy.random.seed(7)
dataset=pd.read_csv('dam-dataset.csv')
param_data=dataset.iloc[:,1:5]
storage_cap=dataset.iloc[:,5]
model=Sequential()
model.add(Dense(units=32,input_shape=(4,),activation='relu'))
model.add(Dense(units=4,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(param_data,storage_cap,epochs=200,batch_size=100,verbose=1)
score=model.evaluate(param_data,storage_cap)
print(score)




