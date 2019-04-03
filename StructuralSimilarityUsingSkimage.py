from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2 # conda install -c conda-forge opencv
# from PIL import Image # Not needed in this

# Mean Squared Error between two images
# Wont work if imageA and imageB dont have same dimension
def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err

def compare_images(imageA, imageB, title):
	m = mse(imageA, imageB) # for mean squared error
	s = ssim(imageA, imageB) # for structural similarity

	# setup the figure as subplots of imageA and imageB
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
	# show first image on left
	ax = fig.add_subplot(1, 2, 1) # Here ax is to prevent the return to print in notebook
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off") # to turn off the x and y axes
	# show the second image on the right
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
	# show the subplot
	plt.show()

# Load the images
original = cv2.imread("images/jp_gates_original.png")
contrast = cv2.imread("images/jp_gates_contrast.png")
shopped = cv2.imread("images/jp_gates_photoshopped.png")

# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

# Draw the three images side by side
# initialize the figure
fig = plt.figure("Images")
images = ("Original", original),("Contrast", contrast), ("Photoshopped", shopped)
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray) # without cmap set as gray, im getting cyan colortone
	plt.axis("off")
# show the figure
plt.show()

# compare the images
compare_images(original, original, "Original vs. Original")
compare_images(original, contrast, "Original vs. Contrast")
compare_images(original, shopped, "Original vs. Photoshopped")
