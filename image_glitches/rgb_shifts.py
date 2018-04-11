import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import skimage.io, skimage.color
import time
import random
import datetime
import imageio


def smoothRGBTransition(image, frames):


    # Number of frames for each switch (6 total switches)
    frame_n = int((frames-1) / 6)

    frame_arr = []
    y = 2
    for r in range(0,6):

        # Get new frames for switch
        image,new_frames = smoothSwap(image, frame_n, 1, y)
        frame_arr += new_frames

        # Alternate switch index
        if (y == 2):
            y = 0
        else:
            y = 2

    return frame_arr



def smoothSwap(image, frame_num, a, b):

    # Calculate the final image
    final = np.copy(image)
    final[:,:,a] = image[:,:,b]
    final[:,:,b] = image[:,:,a]

    frames = []
    for r in range(0,frame_num):

        # Get ratio of before image to after image
        f_ratio = float((r)/frame_num)
        o_ratio = float(1 - f_ratio)

        # Calculate frame
        frame = o_ratio*image + f_ratio*final

        # Add to frame array
        im = plt.imshow(frame, animated=True)
        frames.append([im])

    return final,frames





# Get image
image = skimage.io.imread("FILE PATH TO IMAGE")/255.0

fig = plt.figure()

# Get animation frames
images = smoothRGBTransition(image, 100)

# Display
ani = animation.ArtistAnimation(fig, images, blit=True, repeat_delay=0, interval=10)
plt.show()
