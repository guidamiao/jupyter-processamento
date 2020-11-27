# -*- coding: utf-8 -*-
"""Processamento_de_Imagem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VKpdbckOCM41PurSOK7BXiW4RxQqGhIG

# **Importando os módulos necessários**
"""

# Commented out IPython magic to ensure Python compatibility.
import cv2
import matplotlib.pyplot as plt 
import numpy as np 
from google.colab.patches import cv2_imshow as imshow
# %matplotlib inline

"""# **Prompt para carregar o arquivo de imagem do usuário**"""

from google.colab import files
# upload da imagem 
uploaded = files.upload()
# upload da imagem 
filename = list(uploaded.keys())[0]



"""# **Abrindo a imagem e mostrando-a**"""

# abre a imagem 
image = cv2.imread(filename) 
# mostra a imagem usada 
imshow(image)

"""# **Espelhamento da imagem**"""

# espelha a imagem 
espelhada = cv2.flip(image,1)
imshow(espelhada)

"""# **Converter imagem para tom de cinza**"""

# converet a imagem para tons de cinza
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
imshow(gray)



"""# **Quantização da imagem**"""

N = 4
qimg = np.round(image*(N/255))*(255/N)
imshow(qimg)

"""# **Calculando o histograma de uma imagem em escala de cinza**"""

histograma = np.histogram(gray.ravel(),256,[0,255])
plt.figure(figsize=(20,10))
plt.title("Histograma da Imagem em escala de cinza")
plt.xlabel('Nível do bit')
plt.ylabel('Densidade do bit')
plt.hist(gray.ravel(),255,[0,255],density=True);

"""# **Ajustando nível de brilho da imagem**"""

brilho = -150
# ajusta o brilho da imagem 
imagem_ajustada = np.clip(image+brilho,0,255)
# mostra a imagem 
imshow(imagem_ajustada)



"""# **Ajustando contraste da imagem**"""

# define o contraste 
contraste = 255
# ajusta o contraste
imagem_contraste = np.clip(image*contraste,0,255)
# mostra a imagem
imshow(imagem_contraste)

"""# **Calculando o negativo de uma imagem**"""

# calcula o negativo
negativo = 255 - image
# mostra a imagem
imshow(negativo)

"""# **Equalizando o histograma de uma imagem em escala de cinza**"""

equalizada = cv2.equalizeHist(gray)
# mostra a imagem 
imshow(equalizada)

"""# **Utilizando o histograma adaptativo**"""

clahe = cv2.createCLAHE(clipLimit=2)
eq2 = clahe.apply(gray)
# mostra a imagem
imshow(eq2)

"""# **Normalização com imagem colorida**"""

yuv = cv2.cvtColor(image,cv2.COLOR_BGR2YUV)
yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])
color = cv2.cvtColor(yuv,cv2.COLOR_YUV2BGR)

imshow(image)
imshow(color)