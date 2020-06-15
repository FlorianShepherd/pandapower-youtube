import numpy as np
# sgen_p, load_p, load_q
X_train = np.load("X_train.npy")
X_test = np.load("X_test.npy")
# line loading results
y_train = np.load("y_train.npy")
y_test = np.load("y_test.npy")

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
y_train = scaler.fit_transform(y_train)

from sklearn.neural_network import MLPRegressor
ann = MLPRegressor(verbose=1)
# 10% of power flow data
ann.fit(X_train, y_train)
# 90% of power flow data
y_predict = ann.predict(X_test)
y_predict = scaler.inverse_transform(y_predict)

import matplotlib.pyplot as plt
plt.plot(y_test[:96, 53], alpha=.5, linestyle="--", label="correct line loading values")
plt.plot(y_predict[:96, 53], alpha=.5, linestyle="-", label="predicted line loading values")
plt.legend()
plt.show()

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test,  y_predict)
print(f"the error is only {mse:.2f}%")

from time import  time
t0 = time()
y_predict = ann.predict(X_test)
t1 = time() - t0
print(f"ANN time: {t1:.2f}")
