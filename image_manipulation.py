import cv2
from cv2 import imread
from cv2 import invert
from matplotlib import pyplot as plt

img_path = "gablec.jpg"
img = cv2.imread(img_path)

def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)

    height, width  = im_data.shape[:2]
    
    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()

#invert_image = cv2.bitwise_not(img)
#cv2.imwrite("tmp/inverted.jpg", invert_image)

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_image = grayscale(img)
cv2.imwrite("tmp/gray.jpg", gray_image)

thresh, im_bw = cv2.threshold(gray_image, 70, 255, cv2.THRESH_BINARY)
cv2.imwrite("tmp/bw.jpg", im_bw)

display("tmp/bw.jpg")


