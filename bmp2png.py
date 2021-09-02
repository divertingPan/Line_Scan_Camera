# --- v0.1 ---
# to transform generated bmp file into png
# for a better post-processing in Photoshop

# --- v0.2 ---
# transform images from a whole folder
# the folder should only contain .bmp files

import os
import cv2


folder = r'LCAM3'
images = os.listdir(folder)
if not os.path.exists('{}_modified'.format(folder)):
    os.makedirs('{}_modified'.format(folder))

for image_path in images:
    # image_path = 'Y0023.BMP'
    image = cv2.imread('{}/{}'.format(folder, image_path))
    cv2.imwrite('{}_modified/{}_modified.png'.format(folder, image_path[:-4]), image)
    print('{} saved!'.format(image_path))
