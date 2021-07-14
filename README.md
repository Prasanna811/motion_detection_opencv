# motion_detection_opencv

Here I've implemented a motion detector using OpenCv. We have took the concept of contour for motion detection.

Steps performed:

1. Calculate difference between frames (i.e. present frame and next frame after that).
2. Convert RBG image to gray, since contour will work well with gray scale images.
3. Blur an image using a Gaussian filter.
4. Apply thresholding and dilation on the image.
5. Find contours after that.
6. Draw rectangle using cv2.rectangle with the contours found.
