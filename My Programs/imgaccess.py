import cv2

image=input('Enter the image name with extension: ')
Imagename=image.split("\\")[len(image.split("\\"))-1]
name=Imagename.split(".")[0]
img = cv2.imread(image)
cv2.imshow(name, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
