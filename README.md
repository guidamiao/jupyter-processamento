# Processamento de Imagem # 

## Trabalho de Implementação ## 

**Introdução**

O software desenvolvido possui as seguintes especificações:

> - Ler e gravar arquivos de imagens
> - Exibir o conteúdo de um arquivo de imagem
> - Converter uma imagem colorida em uma imagem em tons de cinza
> - Aplicar um esquema simples para quantização de janelas
> - Usar um sistema de gerenciamento de janelas

>**Continue o trabalho anterior implementando as seguintes operações:**
>- Calcular e exibir o histograma de uma imagem em tons de cinza (8 bits por pixel). Caso a imagem informada como entrada seja colorida, converta-a para tons de cinza (luminância) e então calcule seu histograma. Exiba o histograma em uma janela de 256x256 pixels, onde cada coluna da imagem representa um tom de cinza. Normalize a altura das colunas para obter uma representação apropriada.
>- Ajustar o brilho de uma imagem (e exibi-la), somando ao valor de cada pixel um escalar no intervalo [-255, 255]. Certifique-se que o resultado da operação aplicado a cada pixel encontra-se na faixa [0,255], ajustando-o para zero ou 255 quando necessário. No caso de imagens coloridas, aplique o algoritmo para cada um dos canais (R,G,B) independentemente.
>- Ajustar o contraste de uma imagem (e exibi-la), multiplicando cada pixel por um escalar no intervalo (0, 255]. Certifique-se que o resultado da operação aplicado a cada pixel encontra-se na faixa [0,255], ajustando-o para 255 quando necessário. No caso de imagens coloridas, aplique o algoritmo para cada um dos canais (R,G,B) independentemente ._
>- Calcular e exibir o negativo de uma imagem, calculando o novo valor de cada pixel como: < novo valor > = 255 - < antigo valor>. No caso de imagens coloridas, aplique o algoritmo para cada um dos canais (R,G,B) independentemente_
>- Equalizar o histograma de uma imagem e exibir tanto a imagem como os histogramas antes e depois da equalização. No caso de imagens coloridas, aplique o algoritmo para cada um dos canais (R,G,B), utilizando o histograma cumulativo obtido a partir da imagem de luminância .

Neste sistema foi utilizado a plataforma do _Google Colab_ e o _Jupyter Notebook_, onde rodou duas linguagens, sendo elas _Python_ e _OpenCV_.

O _Google Colaboratory_ — também conhecido como *Google Colab* — é uma **ferramenta em nuvem que permite criar e executar códigos na linguagem Python**. Com ele, você pode rodar os programas diretamente do seu navegador, de forma simples e rápida e já conta com as bibliotecas pré-instaladas.

Sobre os arquivos _Notebooks_ é **um documento virtual que permite a execução de códigos de uma linguagem de programação** juntamente com ferramentas para edição de textos comuns; ou seja, além das rotinas usuais de programação, o usuário pode documentar todo o processo de produção do código. Dessa forma, o notebook permite uma maneira interativa de programar.

Para resolver as aplicações citadas no começo, iremos então utilizar o _Python_ e _OpenCV_.
Primeiro iremos importar as bibliotecas, das quais já estão pré-instaladas no _Google_ _Colaboratory:_

## ***Importando os módulos necessários (bibliotecas)*** 

    import cv2
    import matplotlib.pyplot as plt 
    import numpy as np 
    from google.colab.patches import cv2_imshow as imshow
    %matplotlib inline

## *Prompt para carregar o arquivo de imagem do usuário**

    from google.colab import files
    # upload da imagem 
    uploaded = files.upload() 
    # upload da imagem 
    filename = list(uploaded.keys())[0]

## **Abrindo a imagem e mostrando-a**
    # abre a imagem 
    image = cv2.imread(filename) 
    # mostra a imagem usada 
    imshow(image)

## **Espelhamento da imagem**

    # espelha a imagem 
    espelhada = cv2.flip(image,1)
    imshow(espelhada)

## **Converter imagem para tom de cinza**

    # converet a imagem para tons de cinza
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    imshow(gray)
## **Quantização da imagem**

    N = 4
    qimg = np.round(image*(N/255))*(255/N)
    imshow(qimg)

## **Calculando o histograma de uma imagem em escala de cinza**

    histograma = np.histogram(gray.ravel(),256,[0,255])
    plt.figure(figsize=(20,10))
    plt.title("Histograma da Imagem em escala de cinza")
    plt.xlabel('Nível do bit')
    plt.ylabel('Densidade do bit')
    plt.hist(gray.ravel(),255,[0,255],density=True);

## **Ajustando nível de brilho da imagem**

    brilho = -150
    # ajusta o brilho da imagem 
    imagem_ajustada = np.clip(image+brilho,0,255)
    # mostra a imagem 
    imshow(imagem_ajustada)
## **Ajustando contraste da imagem**

    # define o contraste 
    contraste = 255
    # ajusta o contraste
    imagem_contraste = np.clip(image*contraste,0,255)
    # mostra a imagem
    imshow(imagem_contraste)

## **Calculando o negativo de uma imagem**

    # calcula o negativo
    negativo = 255 - image
    # mostra a imagem
    imshow(negativo)
## **Equalizando o histograma de uma imagem em escala de cinza**

    equalizada = cv2.equalizeHist(gray)
    # mostra a imagem 
    imshow(equalizada)
## **Utilizando o histograma adaptativo**

    clahe = cv2.createCLAHE(clipLimit=2)
    eq2 = clahe.apply(gray)
    # mostra a imagem
    imshow(eq2)
## **Normalização com imagem colorida**

    yuv = cv2.cvtColor(image,cv2.COLOR_BGR2YUV)
    yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])
    color = cv2.cvtColor(yuv,cv2.COLOR_YUV2BGR)
    
    imshow(image)
    imshow(color)

## **Links do Projeto**

Upload feito no _GitHub_ e desenvolvido na plataforma do _Google Colab_.

**_Google Colab_** - [Google Colab](https://colab.research.google.com/drive/1VKpdbckOCM41PurSOK7BXiW4RxQqGhIG)

**_GitHub_** - [github.com/guidamiao/jupyter-processamento](https://github.com/guidamiao/jupyter-processamento)

Outra opção de visualização caso o *GitHub* não execute o projeto.

**_NbViewer_** - [github/guidamiao/jupyter-processamento](https://nbviewer.jupyter.org/github/guidamiao/jupyter-processamento/blob/main/Processamento_de_Imagem.ipynb)

## **Referências**

**Documentações:**

[Welcome to OpenCV-Python Tutorials’s documentation! — OpenCV-Python Tutorials 1 documentation (opencv-python-tutroals.readthedocs.io)](https://opencv-python-tutroals.readthedocs.io/en/latest/index.html)

[Python & OpenCV: Tutoriais e Documentação - Docsity](https://www.docsity.com/pt/python-opencv-tutoriais-e-documentacao/5175445/)

[Livro-Introdução-a-Visão-Computacional-com-Python-e-OpenCV-3.pdf (ifc.edu.br)](http://professor.luzerna.ifc.edu.br/ricardo-antonello/wp-content/uploads/sites/8/2017/02/Livro-Introdu%C3%A7%C3%A3o-a-Vis%C3%A3o-Computacional-com-Python-e-OpenCV-3.pdf)

[3.8.6 Documentation (python.org)](https://docs.python.org/3.8/)

[The Jupyter Notebook — Jupyter Notebook 6.1.5 documentation (jupyter-notebook.readthedocs.io)](https://jupyter-notebook.readthedocs.io/en/stable/)
