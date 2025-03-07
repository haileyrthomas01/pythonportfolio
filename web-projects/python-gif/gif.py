import imageio.v3 as iio
from PIL import Image
import numpy as np

# Load the images
filenames = ['mrfrog1.png', 'mrfrog2.png', 'mrfrog3.png']
images = []

# Set the desired size
desired_size = (500, 500)

# Resize all images to the desired size and convert to numpy arrays
for filename in filenames:
    img = Image.open(filename)
    img = img.resize(desired_size, Image.LANCZOS)
    images.append(np.asarray(img))

# Save the images as a GIF
iio.imwrite('mrfrog.gif', images, duration=500, loop=0)
