import cv2
import matplotlib.pyplot as plt

# -------------------- HISTOGRAM EQUALIZATION ------------------------------------

img = cv2.imread("city.png",cv2.IMREAD_COLOR)           # read image

ycrcb  = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)         # convert to YCrCb 

y, cr, cb = cv2.split(ycrcb)                            # isolate Y channel

y_eq = cv2.equalizeHist(y)                              # equalize the Y channel

img_eq = cv2.merge([y_eq, cr, cb])                      # merge equalized Y channel with the Cr and Cb channels

img_eq_rgb = cv2.cvtColor(img_eq, cv2.COLOR_YCrCb2RGB)  # convert eqaulized image to rgb

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)          # convert original image to rgb


# plot the original image and equalized image
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(img_eq_rgb)
plt.title("Equalized Image")
plt.axis('off')

plt.show()

# -------------------- MORPHOLOGICAL OPERATIONS ---------------------------------------

img_gray = cv2.cvtColor(img_eq_rgb, cv2.COLOR_RGB2GRAY)                 # convert equalized image to grayscale

_, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)       # convert grayscale to binary

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))              # initialize structuring element as a 3x3 cross

# perform the morphological operations
erosion = cv2.erode(img_bin, kernel, iterations=1)                      
dilation = cv2.dilate(img_bin, kernel, iterations=1)
opening = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel)

# plot output of each operation
titles = ['Grayscale', 'Binary', 'Erosion', 'Dilation', 'Opening', 'Closing']
images = [img_gray, img_bin, erosion, dilation, opening, closing]
plt.figure(figsize=(12,6))
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()



