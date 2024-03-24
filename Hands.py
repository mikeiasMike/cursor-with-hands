import cv2

def main():
    # Inicia a captura de vídeo da câmera
    cap = cv2.VideoCapture(0)

    # Verifica se a captura foi iniciada corretamente
    if not cap.isOpened():
        print("Erro ao abrir a câmera!")
        return

    while True:
        # Captura frame por frame
        ret, frame = cap.read()

        # Verifica se o frame foi capturado corretamente
        if not ret:
            print("Erro ao capturar o frame!")
            break

        # Mostra o frame em uma janela
        cv2.imshow('Teste OpenCV', frame)

        # Aguarda por 1ms e verifica se a tecla 'q' foi pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera o objeto de captura e fecha todas as janelas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
