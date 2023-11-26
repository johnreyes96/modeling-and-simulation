# -*- coding: utf-8 -*-
"""Probability.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/johnreyes96/modeling-and-simulation/blob/master/scripts/classes/Probability.ipynb

# Visualización con Matplotlib

Matplotlib es la librería fundamental de visualización en Python. Es una librería de bajo nivel, con muchísima
flexibilidad, de sintaxis compleja pero [documentada](https://matplotlib.org/users/index.html).

### 1. Gráficos de Líneas y Puntos
Vamos a graficar una función sinusoidal de tipo: $y = sen(2 \pi x) + 1$.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generamos dos vectores que nos daran las cordenadas por donde pasará la funciòn
x = np.arange(0.0, 2.0, 0.05)
y = 1 + np.sin(2 * np.pi * x)

# Le pedimos a la librería que dibuje una variable en funcion de la otra
# En el primer lugar va la variable horizontal y en el segundo la vertical
plt.plot(x, y)

"""Si queremos pasar este gráfico a uno de puntos:"""

plt.plot(x, y, 'o')

"""O de puntos y líneas:"""

plt.plot(x, y, 'o-')

"""Muy parecida es la función `plt.scatter()`, que sirve para hacer gráficos de dispersión. A diferencia de 
`plt.plot()`, esta función no permite gráficos de líneas."""

plt.scatter(x, y)

"""### 2. Agregando información al gráfico.

* Etiquetar correctamente los ejes. No olvidar sus unidades.
* Agregar un título.

"""

x = np.arange(0.0, 24, 0.5)
y = 20 + 5 * np.sin(2 * np.pi * (x - 8) / 24)

plt.plot(x, y, color='g', linewidth=2)

# Podemos agregarle etiquetas a los ejes y un titulo al gráfico
plt.xlabel('Tiempo (horas)')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura de un día')

plt.grid()  # Este comando activa la grilla
plt.show()  # Show muestra el gráfico.

"""**Leyendas**

En general, los gráficos suelen contener más de una curva. Para poder distinguirlas correctamente, usamos leyendas, 
que son cuadros que se agregan dentro del gráfico que nos brindan información sobre los distintos elementos.

Cómo graficar más de una curva con sus correspondientes etiquetas (`label`) y cómo crear la leyenda.
"""

x = np.arange(0.0, 24, 0.5)
y1 = 20 + 5 * np.sin(2 * np.pi * (x - 8) / 24)
y2 = 5 + 5 * np.sin(2 * np.pi * (x - 6) / 24)

# Ploteamos las dos lineas, dandole un nombre a cada una mediante el parámetro 'label'.
# Notar que para agregar una curva, simplemente debemos poner una debajo de la otra
plt.plot(x, y1, label='Agosto')
plt.plot(x, y2, label='Octubre')

plt.xlabel('Tiempo (horas)')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura diaria promedio')

plt.grid()

# Agregamos la leyenda al gráfico
plt.legend()  # loc='upper center', shadow=True, fontsize='x-large')plt.show()

"""### 3. Otra manera de gráficar
*Usando* la función `plt.subplot()`.
"""

x = np.linspace(0, 10, 50)
y = np.sin(x)

plt.figure(figsize=(6.4 * 3, 4.8))
plt.subplot(1, 3, 1)
plt.scatter(x, y)

plt.subplot(1, 3, 2)
plt.plot(x, y)

plt.subplot(1, 3, 3)
plt.plot(x, y, 'o-')

plt.tight_layout()
# plt.savefig('Ejemplos_puntos_y_lineas.png', dpi = 300)
plt.show()

x = np.linspace(0, 10, 200) + 0.15 * np.random.randn(200)
y = np.sin(x) + 0.15 * np.random.randn(200)

plt.figure(figsize=(6.4 * 2, 4.8))
plt.subplot(1, 2, 1)
plt.scatter(x, y)

plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.tight_layout()
# plt.savefig('Ejemplos_puntos_y_lineas_malo.png', dpi = 300)
plt.show()

muestras = np.random.normal(50, 15, 5000)

plt.figure(figsize=(6.4 * 2, 4.8))
plt.subplot(1, 2, 1)
plt.hist(muestras, bins=range(0, 101, 10), alpha=0.75, edgecolor='black', linewidth=1.2)

plt.subplot(1, 2, 2)
plt.hist(muestras, bins=range(0, 101, 10), alpha=0.75, edgecolor='black', linewidth=1.2,
         weights=np.ones_like(muestras) / len(muestras))

plt.tight_layout()
# plt.savefig('Ejemplos_histograma.png', dpi = 300)
plt.show()

muestras = np.random.normal(50, 15, 200)

plt.figure(figsize=(6.4 * 3, 4.8))
plt.subplot(1, 3, 1)
plt.hist(muestras, bins=np.linspace(0, 100, 6), alpha=0.75, edgecolor='black', linewidth=1.2)

plt.subplot(1, 3, 2)
plt.hist(muestras, bins=np.linspace(0, 100, 21), alpha=0.75, edgecolor='black', linewidth=1.2)

plt.subplot(1, 3, 3)
plt.hist(muestras, bins=np.linspace(0, 100, 101), alpha=0.75, edgecolor='black', linewidth=1.2)

plt.tight_layout()
# plt.savefig('Ejemplos_histograma_muchos_bines.png', dpi = 300)
plt.show()

"""Gráficos usando los elementos `fig` y `ax`."""

# Generamos las dos curvas
x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)

x2 = np.arange(0.0, 2.0, 0.01)
y2 = x2

# Generamos la figura y los ejes
fig = plt.figure()
ax = plt.axes()

# Ploteamos las dos lineas
ax.plot(x, y)
ax.plot(x2, y2)

"""En la siguiente pagina pueden encontrar mas ejemplos de como utilizar Matplotlib [tutorial](
https://matplotlib.org/3.1.3/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py).

#Probabilidad y Estadística

## 1. Distribuciones de probabilidad El concepto de distribución de probabilidad es un concepto central en 
probabilidad y estadística y, por lo tanto, hay mucho para decir. Nos limitamos acá a los puntos más importantes.

### 1.1. Distrubución Uniforme Discreta Comencemos por un ejemplo: un dado de seis caras. La probabilidad de que al 
tirar el dado salga una cara es  1/6 . Si graficamos la probabilidad para cada resultado posible de tirar un dado, 
obtendríamos un gráfico como el siguiente:"""

valores = np.arange(1, 7)
probas = np.zeros(6) + 1 / 6
plt.bar(valores, probas)
plt.title('Distribución de probabilidad uniforme: lanzamiento de un dado')
# plt.savefig('distribucion_dado.png', dpi = 400)
plt.show()

"""En este caso, decimos que la distribución de probabilidad es *uniforme discreta*, ya que le asigna la misma 
probabilidad a los seis valores que pueden salir al tirar el dado. Si el dado estuviera cargado, ya no sería uniforme.

**Algunos detalles**:
1. El resultado de tirar un dado es un ejemplo de una *variable aleatoria*.
2. En caso del dado, la variable aleatoria puede tomar valores *discretos* y *acotados* (limitados): 1, 2, 3, 4, 5 y 6
3. Existen variables aleatorias donde los posibles valores que puede tomar son continuos y no acotados.

### 1.2 Distribución Normal o Gaussiana

La distribución normal o gaussiana debe ser la distribución más famosa dentro de las distribuciones. Es una 
distribución de variable continua y aparece en una infinidad de ámbitos de la ciencia. Muchas variables asociadas a 
fenómenos naturales siguen una distribución gaussiana; un ejemplo típico es la estatura de las personas. La forma que 
tiene esta distribución está dada por la siguiente fórmula:

$$f(x|\mu, \sigma^2)=\frac{1}{\sqrt{2 \pi \sigma^2}}e^{\frac{-(x - \mu)^2}{2\sigma^2}}$$

Es importante resaltar que tiene sólo dos parámetros: su valor medio $\mu$ y su desviacíon estándar $\sigma$. Estos 
valores son *teóricos*, es decir, son propios de la distribución de probabilidad.

**Distribución Normal en NumPy**

NumPy nos provee de herramientas para generar valores aleatorios de distribuciones. A continuación generamos, 
usando `np.random.normal()`, muestras de dos distribuciones normales, con el mismo valor medio pero distinta 
desviación estándar."""

mu = 2.0
sigma_1 = 5.0
sigma_2 = 2.0
muestras_1 = np.random.normal(loc=mu, scale=sigma_1, size=400)
muestras_2 = np.random.normal(loc=mu, scale=sigma_2, size=400)
print(muestras_1, muestras_2)

"""Para visualizar los datos anteriores lo mejor es utilizar un histograma y lo que hace es tomar un número 
determinado de intervalos (bins = 20) y contar cuántas muestras caen en cada intervalo."""

plt.hist(muestras_1, bins=20, alpha=0.5, label='Histrograma Muestra 1')
plt.hist(muestras_2, bins=20, alpha=0.5, label='Histrograma Muestra 2')
plt.legend()
plt.grid()
plt.show()

"""### 1.3 Relación entre Probabilidad y Estadística

**Promedio y desviación estándar en una distribución Normal**

En una distribución normal, el promedio de las muestras obtenidas *tiende* al valor medio $\mu$ de la distribución, 
y la desviación estándar *tiende* a la desviacíon estándar $\sigma$ de la distribución. Notar, entonces, que existen 
valores calculados (promedio, desviación estándar) y valores teóricos ($\mu$ y $\sigma$). Confundirlos entre sí es un 
error común.

"""

mu = 8.5
sigma = 3.0
muestras = np.random.normal(loc=mu, scale=sigma, size=100)

"""Calculamos su promedio y desviación estándar, y comparamos con $\mu$ y $\sigma$."""

print('Valor medio teorico:', mu, '. Valor medio calculado:', muestras.mean())
print('Desviacion estandar teorica:', sigma, '. Desviacion estandar calculada:', muestras.std())

"""Comparemos el histograma de las muestras y la distribución teórica, que graficaremos haciendo uso de la librería 
`SciPy`:"""

from scipy.stats import norm

plt.hist(muestras, bins=20, density=True, alpha=0.6, color='g')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, sigma)
plt.plot(x, p, 'k', linewidth=2, label='Distribución Teórica')

title = "Muestras obtenidas de una distribución normal con mu = %.2f,  sigma = %.2f" % (mu, sigma)

plt.title(title)
plt.legend()
plt.show()

"""## 2. Correlación

Tenemos dos variables aleatorias $X$ e $Y$, de las cuales tenemos $n$ muestras de cada una, $x_1,x_2,..., 
x_n$ e $y_1,y_2,..., y_n$. Sus valores medios son $\bar{x}$ e $\bar{y}$, respectivamente. Definimos la Covarianza como

$$Cov(X,Y) = \sum_{i=1}^{n} \frac{(x_i - \bar{x})(y_i - \bar{y})}{n}$$

A veces verás que, en lugar de dividir por $n$, se divide por $n - 1$ ó $n - 2$, pero eso no es importante ahora. La 
covarianza es un valor que indica el grado de variación conjunta de dos variables aleatorias respecto a sus medias. 
Es el dato básico para determinar si existe una dependencia entre ambas variables y además es el dato necesario para 
estimar otros parámetros básicos, como el coeficiente de correlación lineal o la recta de regresión.

Empezamos generandos muestras al azar de dos variables aleatorias no relacionadas entre sí.
"""

n = 1000
sigma_1 = 2
sigma_2 = 20
x = np.random.normal(size=n, scale=sigma_1)
y = np.random.normal(size=n, scale=sigma_2)

# Graficamos
plt.scatter(x, y)
plt.grid()
plt.xlim([-60, 60])
plt.ylim([-60, 60])
plt.show()

"""¿Hay alguna relación entre ellos? Por relación nos referimos a "variación conjunta". Y por "variación conjunta" 
podemos imaginarnos que si una de las variables aumenta, la otra también lo hace. Y si una variable disminuye su 
valor, la otra también lo hace. La covarianza intenta cuantificar esa relación."""

cov = np.sum((x - x.mean()) * (y - y.mean())) / x.size
print(cov)

"""La covarianza, sin embargo, tiene un pequeño problema: depende de la escala de nuestros datos. Entonces, 
para deshacernos de la escala, se puede definir la Correlación, que no es otra cosa que la covarianza dividida la 
desviación estándar de cada variable aletaria.

$$Corr(X,Y) = \frac{Cov(X,Y)}{\sigma_X \sigma_Y}$$
"""

corr = cov / (x.std() * y.std())
print(corr)

"""Y con eso nos deshacemos de la escala. Un valor cercano a cero nos indica que no existe una relación (¿lineal?) 
entre las variables.

**Probar** con distintas escalas (modificando `sigma_1` y `sigma_2`) y verán que `cov` tomará valores en un rango muy 
amplio, mientras que `corr` se mantendrá cercana a cero.

### 2.1 Relación lineal

Veamos otro ejemplo: sabemos que existe una relación lineal entre $X$ e $Y$, es decir, podemos aproximar $Y =aX+b$, 
donde $a$ y $b$ son la pendiente y la ordenada al origen."""

n = 100
x = np.linspace(-1, 1, n) + 0.25 * np.random.normal(size=n)
y = 4.5 * x + 0.25 * np.random.normal(size=n)

# Graficamos
plt.scatter(x, y)
plt.grid()
plt.show()

"""La covarianza y la correlación"""

cov = np.sum((x - x.mean()) * (y - y.mean())) / x.size
print(cov)

corr = cov / (x.std() * y.std())
print(corr)

"""#### Conclusiones

1. La covarianza es una medida de la variación conjunta de dos variables. Pero tiene un problema: depende de la 
escala. 2. Para "deshacernos" de la escala, definimos la correlación, que es simplemente la covarianza dividida por 
el producto de la desviación estándar de cada variable. 3. La correlación es un valor entre -1 y 1. La correlación 
toma un valor cercano a uno cuando hay una relación lineal creciente entre las variables, cero cuando no hay relación 
y -1 cuando hay una relación lineal decreciente.

### 2.2 Covarianza y Correlación con NumPy

NumPy ya tiene incorporadas funciones que calculan la covarianza y la correlación entre dos variables. La única 
diferencia es que, en lugar de devolver un único valor, devuelve cuatro valores, que corresponden a la 
covarianza/correlación entre $X$ con $X$, $X$ con $Y$, $Y$ con $X$, e $Y$ con $Y$. ¿Por qué, en la correlación, 
algunos valores son exactamente uno (1.)?"""

np.cov([x, y])

np.corrcoef([x, y])

"""### 2.3 Relación No-Lineal entre variables

¿Qué ocurre cuando la relación no es lineal entre las variables? Aqui un ejemplo.

"""

n = 1000
x = np.linspace(-5, 5, n) + 0.25 * np.random.normal(size=n)
y = x ** 2 + 0.25 * np.random.normal(size=n)

# Graficamos
plt.scatter(x, y)
plt.grid()
plt.show()

"""La covarianza y la correlación"""

cov = np.sum((x - x.mean()) * (y - y.mean())) / x.size
print(cov)

corr = cov / (x.std() * y.std())
print(corr)

"""Notar que la correlación de un valor alrededor de cero, indicando que no hay una correlación entre ambas 
variables. Pero esto NO indica que no hay una *relación* entre esas variables, solamente nos dice que no es lineal. 
Por eso es muy importante graficar.

### 3. Correlación en Pandas

Para eso, volvemos a usar el Iris Dataset.
"""

data = pd.read_csv('../../data/Iris.csv')
data.drop(columns=['Id', 'Species'], inplace=True)
print(data.head())

"""Para obtener las correlaciones entre las distintas variables, simplemente tenemos que hacer:"""

print(data.corr())