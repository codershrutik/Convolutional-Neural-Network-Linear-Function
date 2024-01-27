import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
(X_train,y_train),(X_test,y_test) = datasets.cifar10.load_data()
X_test.shape
X_train.shape
y_train[:5]
y_train = y_train.reshape(-1,)
y_train[:5]
y_test = y_test.reshape(-1,)
classes = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck'] def plot_sample(X,y,index):
plt.figure(figsize=(15,2)) plt.imshow(X[index]) plt.xlabel(classes[y[index]])
plot_sample(X_train,y_train,5) plot_sample(X_train,y_train,501) X_train = X_train/255.0
X_test = X_test/255.0
ann = models.Sequential([ layers.Flatten(input_shape = (32,32,3)), layers.Dense(3000,activation = 'relu'), layers.Dense(3000,activation = 'relu'), layers.Dense(10,activation = 'softmax')
])
ann.compile(optimizer='SGD',
loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
ann.fit(X_train,y_train,epochs = 5)
from sklearn.metrics import confusion_matrix, classification_report
y_pred = ann.predict(X_test)
y_pred_classes = [np.argmax(element) for element in y_pred]
print('Classification report: \n',classification_report(y_test,y_pred_classes)) import seaborn as sns
plt.figure(figsize = (14,7))
sns.heatmap(y_pred,annot = True)
plt.ylabel('Truth') plt.xlabel('Prediction') plt.title('Confusion Matrix') plt.show()
cnn = models.Sequential([ layers.Conv2D(filters =
'relu',input_shape=(32,32,3)), layers.MaxPooling2D((2,2)),
32,kernel_size =
(3,3),activation =
layers.Conv2D(filters = 64,kernel_size = (3,3),activation = 'relu'), layers.MaxPooling2D((2,2)),
layers.Flatten(), layers.Dense(64,activation = 'relu'), layers.Dense(10,activation = 'softmax')
])
cnn.compile(optimizer='adam',loss = 'sparse_categorical_crossentropy',metrics = ['accuracy'])
cnn.fit(X_train,y_train,epochs=10)
cnn.evaluate(X_test,y_test)
y_pred = cnn.predict(X_test)
y_pred[:5]
y_classes = [np.argmax(element) for element in y_pred] y_classes[:5]
y_test[:5]
plot_sample(X_test,y_test, 60) plot_sample(X_test,y_test,100)
classes[y_classes[60]]
