import cv2

#Conecta a webcam
webcam = cv2.VideoCapture(0)

#verifica se a webcam esta conectada
if webcam.isOpened():
    validacao, frame = webcam.read() #retorna true/false, e o rgb dos pixels

    while validacao:
        validacao, frame = webcam.read() #lendo a imagem
        cv2.imshow("Video da WebCam", frame) #titulo da janela, e a imagem que eu quero mostrar

        key = cv2.waitKey(5) #define a quantidade de fps do video
        #se apertar ESC fecha a janela do video
        if key == 27:
            break
    
    cv2.imwrite("FotoFrame.png", frame) #tira print do ultimo frame do video

webcam.release() #finaliza a webcam
cv2.destroyAllWindows() #fecha as janelas que restarem abertas