# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Alumnos: Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)

    # Graficar la función utilizando "scatter"
    # utilizando "x" e "y"

    # Colocar la leyenda y el label con el nombre de la función

    # Elegir un marker a elección

    # Crear acá su gráfico
    fig = plt.figure()
    fig.suptitle('Funcion TANH', fontsize=20)
    ax = fig.add_subplot()  
    ax.scatter(x, y, c='darkred', marker='^', label=' y = np.tanh(x)')
    ax.legend()
    plt.show()

    print("terminamos")