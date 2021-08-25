# katoengineer

- EyeTracking
- OpenCV
- Haarcascade

# EyeTracking

- El objetivo del proyecto es construir un algoritmo que realice el seguimiento de nuestro ojo utilizando las funciones basicas que nos entrega la liberia OpenCV.

# OpenCV

- Libreria open source de vision por computadora.
- El objetivo de la libreria es facilitar la visión por computadora en tiempo real y el procesamiento de imágenes.
- Funciones de la libreria :
  - VideoCapture()
  - flip(src, flipcode)
  - cvtColor(src, code)
  - threshold(src, thresh, maxval, type)
  - findContours(image, mode, method)
  - boundingRect(array)
- Mas informacion [[aqui](https://docs.opencv.org/4.5.2/index.html)]

# Haarcascade

- Haarcascade es un modelo que ha sido entrenado por OpenCV.
- Haarcascade tiene cerca de 20 años y se sigue utilizando en ciertos escenarios y situaciones, estos son super rápidos, requieren poco poder de harware, lo hace eficiente para utilizarlos en hardwares limitados como el RPI.
- La funcion .detectMultiScale nos retorna una lista de ubicaciones de un cuadro delimitador por cada deteccion en la imagen. Cada cuadro delimitador esta representado por 4 valores:
  - x: La coordenada x inicial del cuadro
  - y: La coordenada y inicial del cuadro
  - w: El ancho del cuadro
  - h: La altura del cuadro
