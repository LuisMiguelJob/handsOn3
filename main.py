import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def qlr_function(x, a, b, c):
    return a * np.exp(b * x) + c

# Muestra de datos
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1.2, 2.5, 4.7, 8.3, 14.5, 25.1])

# Ejecutar la curva de encaje con QLR
params, params_covariance = curve_fit(qlr_function, x_data, y_data)

# Extraer los parametros ajustados
a_fit, b_fit, c_fit = params

# Generar la curva ajustada
x_fit = np.linspace(0, 5, 100)
y_fit = qlr_function(x_fit, a_fit, b_fit, c_fit)

# Trazar los datos originales y la curva ajustada
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_fit, y_fit, color='red', label='Fitted curve')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curve Fitting with QLR')
plt.show()