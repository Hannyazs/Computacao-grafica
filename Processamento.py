import cv2

img = cv2.imread("ruido.png")

gauss = cv2.GaussianBlur(img, (5, 5), 0)

mediana = cv2.medianBlur(img, 5)

cv2.imshow("Original com Ruido", img)
cv2.imshow("Filtro Gaussiano", gauss)
cv2.imshow("Filtro Mediana", mediana)

cv2.waitKey(0)
cv2.destroyAllWindows()
