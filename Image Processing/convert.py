# Simple script to convert HEIC images to compressed JPG
import os
import re
from PIL import Image
from pillow_heif import register_heif_opener

current_total = 953
regex = '(.+).heic'
new_filepath = os.getcwd() + '/converted'
old_filepath = os.getcwd() + '/heic'
image_quality = 30 # Default is 75
files = os.listdir (old_filepath)

register_heif_opener()
for file in files:
    print ('Converting %s' % file)
    new = 'image%s.jpeg' % (int(re.match(regex, file).group(1)) + current_total)
    image = Image.open('%s/%s' % (old_filepath, file))
    image.convert('RGB').save ('%s/%s' % (new_filepath, new), format = 'JPEG', quality = image_quality, optimize = True)