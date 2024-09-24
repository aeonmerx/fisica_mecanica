# Simulación de Movimiento Rectilíneo Uniformemente Acelerado (MRUA)

## Descripción del Proyecto

Este proyecto contiene una simulación sencilla del **Movimiento Rectilíneo Uniformemente Acelerado (MRUA)**, que describe el movimiento de un objeto que se desplaza en línea recta bajo la influencia de una aceleración constante. El código simula y grafica el desplazamiento de un objeto a lo largo del tiempo, utilizando las ecuaciones del MRUA.

## Ecuación Utilizada

La ecuación para calcular el desplazamiento en MRUA es:
$$
x = v_0 \cdot t + \frac{1}{2} \cdot a \cdot t^2
$$


$


\]


Donde:
- \( v_0 \) es la velocidad inicial del objeto (en m/s).
- \( a \) es la aceleración constante (en m/s²).
- \( t \) es el tiempo transcurrido (en segundos).
- \( x \) es el desplazamiento (en metros).

## Cómo Usar el Código

1. **Instalación**: Asegúrate de tener instaladas las librerías necesarias ejecutando:

```bash
!pip install nump


# Simulación de Movimientos en Física

Este proyecto tiene como objetivo simular y visualizar diferentes tipos de movimiento en física: Movimiento Armónico Simple (MAS), Movimiento Parabólico y Movimiento Circular Uniforme (MCU). Se utiliza Python junto con las bibliotecas NumPy y Matplotlib para realizar cálculos numéricos y crear gráficos que ayudan a entender los conceptos de movimiento de manera visual.

## Contenido

Introducción
Requisitos
Descripción de los Movimientos
Movimiento Armónico Simple (MAS)
Movimiento Parabólico
Movimiento Circular Uniforme (MCU)
Código Explicado
Ejecución
Conclusiones
Introducción

La física describe el movimiento de los objetos a través de diferentes modelos. Este proyecto proporciona una forma visual de entender esos modelos mediante simulaciones en Python. Utilizaremos gráficas para observar cómo varían las posiciones de los objetos en el tiempo según diferentes condiciones iniciales.

### Requisitos

Para ejecutar el código, necesitarás tener instalado Python y las siguientes bibliotecas:

- NumPy
- Matplotlib
- Puedes instalar las bibliotecas necesarias usando pip:

*pip install numpy matplotlib*

### Descripción de los Movimientos

#### Movimiento Armónico Simple (MAS)
El Movimiento Armónico Simple se describe por una oscilación periódica. La ecuación que define la posición en función del tiempo es:

*x(t) = A * cos(ωt)*

donde:

- A es la amplitud (máxima distancia desde la posición de equilibrio).
- ω es la frecuencia angular (en radianes por segundo), que se relaciona con la frecuencia f como ω = 2πf.
- t es el tiempo.
### Visualización: Se grafica la posición en función del tiempo, mostrando la oscilación del objeto.

#### Movimiento Parabólico
El Movimiento Parabólico describe la trayectoria de un objeto lanzado en el aire bajo la influencia de la gravedad. Las ecuaciones para calcular la posición son:

*x(t) = v0 * cos(θ) * t*

*y(t) = v0 * sin(θ) * t - (1/2) * g * t^2*

donde:

- v0 es la velocidad inicial.
- θ es el ángulo de lanzamiento.
- g es la aceleración debida a la gravedad.
### Visualización: Se grafica la trayectoria del objeto en un plano cartesiano.

#### Movimiento Circular Uniforme (MCU)
El Movimiento Circular Uniforme describe el movimiento de un objeto que se desplaza a lo largo de una trayectoria circular con velocidad constante. La posición en coordenadas polares se puede describir como:

*x(t) = R * cos(ωt)*

*y(t) = R * sin(ωt)*

donde:

- R es el radio de la trayectoria circular.
- ω es la velocidad angular.
### Visualización: Se grafica la trayectoria circular del objeto.
