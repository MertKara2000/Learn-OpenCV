import numpy as np
import cv2 

# img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# img[55,55] = [255,255,255]
# px = img[55,55]
# print(px)

# roi = img[100:150, 100:150] = [255,255,255]

# watch = img[147:221, 257:344]
# img[0:74, 0:87] = watch

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# === Image arithmetics and Logic  ===


img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')
img3 = cv2.imread('python.png')

img1 = cv2.resize(img1, (400, 400), interpolation=cv2.INTER_AREA) 
img2 = cv2.resize(img2, (400, 400), interpolation=cv2.INTER_AREA) 
img3 = cv2.resize(img3, (400, 400), interpolation=cv2.INTER_AREA) 

#add = img1 + img2
#add = cv2.add(img1,img2)
#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)


#cv2.imshow('add', add)
#cv2.imshow('weighted', weighted)



#  === Masking  ===

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

#cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img3_fg)
img1[0:rows,0:cols] = dst

# cv2.imshow('res', img1)
# cv2.imshow('mask_inv', mask_inv)
# cv2.imshow('img1_bg', img1_bg)
# cv2.imshow('img3_fg', img3_fg)
# cv2.imshow('dst', dst)




cv2.waitKey(0)
cv2.destroyAllWindows()
