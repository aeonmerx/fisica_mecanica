#!/usr/bin/env python
# coding: utf-8

# <img src="https://th.bing.com/th/id/OIP.JfPzn_OAPGtSynbtGOI6XgAAAA?rs=1&pid=ImgDetMain" width="22%">
# <br>
# <a href="http://aeonmerx.eastus.cloudapp.azure.com:8080/consultar">Inicio </a>

# # Simulación de Movimiento Rectilíneo Uniformemente Acelerado (MRUA)
# 
# ## Descripción del Proyecto
# 
# Este proyecto contiene una simulación sencilla del **Movimiento Rectilíneo Uniformemente Acelerado (MRUA)**, que describe el movimiento de un objeto que se desplaza en línea recta bajo la influencia de una aceleración constante. El código simula y grafica el desplazamiento de un objeto a lo largo del tiempo, utilizando las ecuaciones del MRUA.
# 
# ## Ecuación Utilizada
# 
# La ecuación para calcular el desplazamiento en MRUA es:
# $$
# x = v_0 \cdot t + \frac{1}{2} \cdot a \cdot t^2
# $$
# 
# 
# $
# 
# 
# \]
# 
# 
# Donde:
# - \( v_0 \) es la velocidad inicial del objeto (en m/s).
# - \( a \) es la aceleración constante (en m/s²).
# - \( t \) es el tiempo transcurrido (en segundos).
# - \( x \) es el desplazamiento (en metros).
# 
# ## Cómo Usar el Código
# 
# 1. **Instalación**: Asegúrate de tener instaladas las librerías necesarias ejecutando:
# 
# ```bash
# !pip install numpy matplotlib
# 

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# Función que calcula el desplazamiento en MRUA
def calcular_desplazamiento(v0, a, t):
    """
    Calcula el desplazamiento de un objeto en movimiento rectilíneo uniformemente acelerado (MRUA).
    
    Parámetros:
    v0 (float): Velocidad inicial (m/s).
    a (float): Aceleración constante (m/s^2).
    t (float): Tiempo (s).
    
    Retorna:
    x (float): Desplazamiento (m).
    """
    return v0 * t + 0.5 * a * t**2

# Parámetros de la simulación
velocidad_inicial = 5  # m/s
aceleracion = 2        # m/s^2
tiempo_total = 10      # s

# Generar una lista de tiempos (de 0 a tiempo_total)
tiempos = np.linspace(0, tiempo_total, 100)

# Calcular desplazamientos para cada instante de tiempo
desplazamientos = [calcular_desplazamiento(velocidad_inicial, aceleracion, t) for t in tiempos]

# Graficar los resultados
plt.figure(figsize=(8, 6))
plt.plot(tiempos, desplazamientos, label="Desplazamiento", color="blue")
plt.title("Movimiento Rectilíneo Uniformemente Acelerado (MRUA)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Desplazamiento (m)")
plt.grid(True)
plt.legend()
plt.show()


# # Simulación de Movimientos en Física
# 
# Este proyecto tiene como objetivo simular y visualizar diferentes tipos de movimiento en física: Movimiento Armónico Simple (MAS), Movimiento Parabólico y Movimiento Circular Uniforme (MCU). Se utiliza Python junto con las bibliotecas NumPy y Matplotlib para realizar cálculos numéricos y crear gráficos que ayudan a entender los conceptos de movimiento de manera visual.
# 
# ## Contenido
# 
# Introducción
# Requisitos
# Descripción de los Movimientos
# Movimiento Armónico Simple (MAS)
# Movimiento Parabólico
# Movimiento Circular Uniforme (MCU)
# Código Explicado
# Ejecución
# Conclusiones
# Introducción
# 
# La física describe el movimiento de los objetos a través de diferentes modelos. Este proyecto proporciona una forma visual de entender esos modelos mediante simulaciones en Python. Utilizaremos gráficas para observar cómo varían las posiciones de los objetos en el tiempo según diferentes condiciones iniciales.
# 
# ### Requisitos
# 
# Para ejecutar el código, necesitarás tener instalado Python y las siguientes bibliotecas:
# 
# - NumPy
# - Matplotlib
# - Puedes instalar las bibliotecas necesarias usando pip:
# 
# *pip install numpy matplotlib*
# 
# ### Descripción de los Movimientos
# 
# #### Movimiento Armónico Simple (MAS)
# El Movimiento Armónico Simple se describe por una oscilación periódica. La ecuación que define la posición en función del tiempo es:
# 
# *x(t) = A * cos(ωt)*
# 
# donde:
# 
# - A es la amplitud (máxima distancia desde la posición de equilibrio).
# - ω es la frecuencia angular (en radianes por segundo), que se relaciona con la frecuencia f como ω = 2πf.
# - t es el tiempo.
# ### Visualización: Se grafica la posición en función del tiempo, mostrando la oscilación del objeto.
# 
# #### Movimiento Parabólico
# El Movimiento Parabólico describe la trayectoria de un objeto lanzado en el aire bajo la influencia de la gravedad. Las ecuaciones para calcular la posición son:
# 
# *x(t) = v0 * cos(θ) * t*
# 
# *y(t) = v0 * sin(θ) * t - (1/2) * g * t^2*
# 
# donde:
# 
# - v0 es la velocidad inicial.
# - θ es el ángulo de lanzamiento.
# - g es la aceleración debida a la gravedad.
# ### Visualización: Se grafica la trayectoria del objeto en un plano cartesiano.
# 
# #### Movimiento Circular Uniforme (MCU)
# El Movimiento Circular Uniforme describe el movimiento de un objeto que se desplaza a lo largo de una trayectoria circular con velocidad constante. La posición en coordenadas polares se puede describir como:
# 
# *x(t) = R * cos(ωt)*
# 
# *y(t) = R * sin(ωt)*
# 
# donde:
# 
# - R es el radio de la trayectoria circular.
# - ω es la velocidad angular.
# ### Visualización: Se grafica la trayectoria circular del objeto.

# In[13]:


import numpy as np
import matplotlib.pyplot as plt

def movimiento_armonico_simple(A, w, t):
    """Calcula la posición en Movimiento Armónico Simple (MAS)."""
    return A * np.cos(w * t)

def movimiento_parabólico(v0, angulo, t):
    """Calcula la posición de un objeto en Movimiento Parabólico."""
    g = 9.81  # Aceleración debida a la gravedad (m/s^2)
    angulo_rad = np.radians(angulo)  # Convertir a radianes
    x = v0 * np.cos(angulo_rad) * t  # Posición horizontal (m)
    y = v0 * np.sin(angulo_rad) * t - 0.5 * g * t ** 2  # Posición vertical (m)
    return x, y

def movimiento_circular_uniforme(r, w, t):
    """Calcula la posición de un objeto en Movimiento Circular Uniforme (MCU)."""
    theta = w * t  # Ángulo en radianes
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

# Parámetros para el Movimiento Armónico Simple (MAS)
A = 2  # Amplitud (m)
w = 2 * np.pi  # Frecuencia angular (rad/s)
t_mas = np.linspace(0, 4, 100)  # Tiempo (s)
posiciones_mas = movimiento_armonico_simple(A, w, t_mas)

# Parámetros para el Movimiento Parabólico
v0 = 20  # Velocidad inicial (m/s)
angulo = 45  # Ángulo de lanzamiento (grados)
t_parabolico = np.linspace(0, 2.5, 100)  # Tiempo (s)
x_parabolico, y_parabolico = movimiento_parabólico(v0, angulo, t_parabolico)

# Parámetros para el Movimiento Circular Uniforme (MCU)
r = 5  # Radio de la trayectoria (m)
w_mcu = np.radians(30)  # Velocidad angular (rad/s)
t_circular = np.linspace(0, 10, 100)  # Tiempo (s)
x_circular, y_circular = movimiento_circular_uniforme(r, w_mcu, t_circular)

# Configuración de la figura y los ejes
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Gráfico de Movimiento Armónico Simple (MAS)
axs[0].plot(t_mas, posiciones_mas, label='Posición en MAS', color='blue')
axs[0].set_title('Movimiento Armónico Simple (MAS)')
axs[0].set_xlabel('Tiempo (s)')
axs[0].set_ylabel('Posición (m)')
axs[0].grid()
axs[0].legend()

# Gráfico de Movimiento Parabólico
axs[1].plot(x_parabolico, y_parabolico, label='Trayectoria en Movimiento Parabólico', color='green')
axs[1].set_title('Movimiento Parabólico')
axs[1].set_xlabel('Posición X (m)')
axs[1].set_ylabel('Posición Y (m)')
axs[1].grid()
axs[1].legend()

# Gráfico de Movimiento Circular Uniforme (MCU)
axs[2].plot(x_circular, y_circular, label='Trayectoria en MCU', color='red')
axs[2].set_title('Movimiento Circular Uniforme (MCU)')
axs[2].set_xlabel('Posición X (m)')
axs[2].set_ylabel('Posición Y (m)')
axs[2].axis('equal')  # Mantener la proporción
axs[2].grid()
axs[2].legend()

# Mostrar la figura
plt.tight_layout()
plt.show()


# <code>AEON MERX 2024</code>
