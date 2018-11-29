import numpy as np
import pandas as pd
class Perceptron:
  @classmethod
  def _step_function(cls, y):
    if y >= 0:
      return 1
    else:
      return 0
  @classmethod
  def _prediction(cls, X, W, b):
    return cls._step_function (np.matmul(X, W)+ b)
  
  @classmethod
  def _perceptron_alg(cls, X, y, W, b, learning_rate):
    for i in range (len (X)):
      y_hat = cls._prediction(X[i], W, b)
      if y[i] - y_hat == 1:
        W[0] += X[i][0] * learning_rate
        W[1] += X[i][1] * learning_rate
        b += learning_rate
        
      elif y[i] - y_hat == -1:
        W[0] -= X[i][0] * learning_rate
        W[1] -= X[i][1] * learning_rate
        b -= learning_rate   
        
    return W, b
  
  def __init__(self, learning_rate = 0.01, random_seed = 42):
    self.__random_seed = random_seed
    self.__alpha = learning_rate
    self.__weights = None
    self.__bias = None
    
  def fit (self, X, y, epochs = 30):
    e = epochs
    np.random.seed(self.__random_seed)
    weights= np.random. uniform (-1, 1, 2)
    bias = np.random.uniform(0, 2, 1)
    while epochs > 0:
      W, b = self._perceptron_alg (X, y, weights, bias, self.__alpha)
      weights = W
      bias = b
      print ( "Epoch {}: Weights = {}, Bias = {}". format (epochs, weights, 
                                                           bias))
      epochs -=1
    self.__weights = weights
    self.__bias = bias
    
  def predict(self, X):
    predictions = []
    for i in range(len(X)):
      predictions.append(self._prediction(X[i], self.__weights, self.__bias))
    return np.array (predictions) 
  data = pd.read_csv("data.txt", header = None)
  X = data.drop(2, axis= 1).values
  y = data.iloc[:, 2].values
  model = Perceptron(learning_rate = 0.01, random_seed = 42)
  model.fit(X, y, epochs = 30)
  
  pred = model.predict(X)
  print()
  print("Accuracy {}".format((sum(pred ==y))/len(y)))