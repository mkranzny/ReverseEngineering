import numpy as np
import cv2 as cv

img = cv.imread('BoltProfile.png', cv.IMREAD_GRAYSCALE)
# print(img.shape)
# Apply binary thresholding
ret, thresh1 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)

# Find contours
contours, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print(contours)
# Print the number of contours found
# print(f"Number of contours found: {len(contours)}")
# Draw all contours on a copy of the original image
img_with_contours = cv.cvtColor(img, cv.COLOR_GRAY2BGR) # Convert to BGR for drawing in color
cv.drawContours(img_with_contours, contours, -1, (0, 255, 0), 2) # Draw all contours in green with thickness 2

cnt = contours[0]

x,y,w,h = cv.boundingRect(cnt)
img_with_bounds = cv.cvtColor(img, cv.COLOR_GRAY2BGR) # Convert to BGR for drawing in color
cv.rectangle(img_with_bounds,(x,y),(x+w,y+h),(0,255,0),2)
# print(x,y,w,h)
cropped_img = thresh1[y:(y+w), x:(x+w)]
thread_img = thresh1[y:(y+w), (x+round(w/2.5)):(x+round(w/1.1))]


# Find contours
contours2, hierarchy2 = cv.findContours(thread_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print(contours)
# Print the number of contours found
# print(f"Number of contours found: {len(contours)}")
# Draw all contours on a copy of the original image
thread_with_contours = cv.cvtColor(thread_img, cv.COLOR_GRAY2BGR) # Convert to BGR for drawing in color
cv.drawContours(thread_with_contours, contours2, -1, (0, 255, 0), 2) # Draw all contours in green with thickness 2

cnt2 = contours2[0]

rect = cv.minAreaRect(cnt2)
box = cv.boxPoints(rect)
box = np.int0(box)
print(box)
thread_with_box = cv.cvtColor(thread_img, cv.COLOR_GRAY2BGR) # Convert to BGR for drawing in color
cv.drawContours(thread_with_box,[box],0,(0,0,255),2)


# Create image filled with zeros the same size of original image
blank = np.zeros(thread_img.shape[0:2], dtype=np.uint8)
# Copy bounding box contour into its own image and fill it with '1'
image1 = cv.drawContours(blank.copy(), [box], -1, color=(255, 255, 255), thickness=2)
# print(image1.shape, thread_img.shape)
# print(image1.dtype, thread_img.dtype)
image_anded = cv.bitwise_and(thread_img, image1)
threadLine = image_anded[181]
print(threadLine)
# print(len(threadLine))
onThread = 0
threadCount1 = 0
threadCount2 = 0
for i in range(len(threadLine)):
    if ((threadLine[i] > 127) and (onThread == 0)):
        onThread = 1
        threadCount1 = threadCount1 + 1
    if ((threadLine[i] < 127) and (onThread == 1)):
        onThread = 0
        threadCount2 = threadCount2 + 1
print("number of threads = ", threadCount2, "number of pixels = ", box[2,0])
    # print(threadLine[i])

# print(box)

# cv.imshow('test',img)
# cv.imshow('test',thresh1)
# cv.imshow('test',img_with_contours) 
# cv.imshow('test',img_with_bounds)
# cv.imshow('test',img_with_box)
# cv.imshow('test',cropped_img)
# cv.imshow('test',thread_img)
# cv.imshow('test',thread_with_contours)
# cv.imshow('test',thread_with_box)
# cv.imshow('test',image1)
cv.imshow('test',image_anded)

cv.waitKey(0)
cv.destroyAllWindows()