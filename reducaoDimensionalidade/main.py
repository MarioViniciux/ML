import cv2

try:
    img_colorida = cv2.imread('imagem_colorida.jpg')

    if img_colorida is None:
        raise FileNotFoundError

    img_cinza = cv2.cvtColor(img_colorida, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('imagem_cinza_cv.jpg', img_cinza)

    cv2.imshow('Imagem em Tons de Cinza', img_cinza)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Imagem convertida para tons de cinza com sucesso usando OpenCV!")

except FileNotFoundError:
    print("Erro: O arquivo 'imagem_colorida.jpg' não foi encontrado.")

try:
    img_para_binarizar = cv2.imread('imagem_cinza_cv.jpg', cv2.IMREAD_GRAYSCALE)

    if img_para_binarizar is None:
        raise FileNotFoundError

    limiar = 127
    valor_maximo = 255
    ret, img_preto_e_branco = cv2.threshold(img_para_binarizar, limiar, valor_maximo, cv2.THRESH_BINARY)

    cv2.imwrite('imagem_preto_e_branco_cv.jpg', img_preto_e_branco)

    cv2.imshow('Imagem em Preto e Branco', img_preto_e_branco)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Imagem convertida para preto e branco com sucesso usando OpenCV!")

    ret_otsu, img_otsu = cv2.threshold(img_para_binarizar, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite('imagem_otsu_cv.jpg', img_otsu)
    print(f"Limiar ótimo encontrado pelo método de Otsu: {ret_otsu}")


except FileNotFoundError:
    print("Erro: O arquivo 'imagem_cinza_cv.jpg' não foi encontrado para binarizar.")