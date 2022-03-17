# Simple script to compress images
import os
from PIL import Image 

old_filepath = os.getcwd() + '/images'
new_filepath = os.getcwd() + '/compress'
image_quality = 30 # Default is 75
files = os.listdir(old_filepath)

for file in files:
    print ('Compressing %s' % file)
    image = Image.open('%s/%s' % (old_filepath, file))
    image.convert('RGB').save ('%s/%s' % (new_filepath, file), format = 'JPEG', quality = image_quality, optimize = True)