import cv2

image = cv2.imread("nisekoi_chitoge.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray image", gray_image)
cv2.imshow("image", image)
#when displaying picture it will wait for a key before close
cv2.waitKey(0)
cv2.destroyAllWindows()

#save picture
cv2.imwrite("gray_chitoge.jpg", gray_image)
