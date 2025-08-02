from ultralytics import YOLO
import cv2
from IPython.display import display, Image
import PIL.Image

model = YOLO("yolov8n.pt")  # ou yolov8m.pt, yolov8s.pt etc.

# Fazer a predição
results = model("pessoas.jpg")

# Mostrar imagem com anotações no Colab
results[0].save(filename="saida.jpg")
display(PIL.Image.open("saida.jpg"))

results = model("bicicleta.jpg")
results[0].save("saida1.jpg")
display(PIL.Image.open("saida1.jpg"))

results = model("pessoas.jpg")
results[0].save("saida2.jpg")
display(PIL.Image.open("saida2.jpg"))