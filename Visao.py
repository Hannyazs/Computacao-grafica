import cv2
import easyocr

# Carrega a imagem do carro
img = cv2.imread("carros.png")

# Inicializa o leitor (português e inglês, por exemplo)
reader = easyocr.Reader(['en', 'pt'])

# Detecta e reconhece texto na imagem
resultados = reader.readtext(img)

# Mostra os resultados
for (bbox, texto, prob) in resultados:
    print(f"Texto: {texto} - Confiança: {prob:.2f}")
    # Desenha o retângulo ao redor do texto detectado
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

cv2.imwrite("saida.jpg", img)