import cv2


# to transform generated bmp file into png
# for a better post-processing in Photoshop
image_path = 'Y0023.BMP'
image = cv2.imread(image_path)
cv2.imwrite('{}_modified.png'.format(image_path[:-4]), image)