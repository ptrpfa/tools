# Simple script to rename files in bulk
import os
import re

current_total = 640
regex = 'image(\d+)\.jpeg'
new_filepath = os.getcwd() + '/images'
old_filepath = os.getcwd() + '/images2'
files = os.listdir(old_filepath)

for file in files:
    new = 'image%s.jpeg' % (int(re.match(regex, file).group(1)) + current_total)
    os.rename('%s/%s' % (old_filepath, file),'%s/%s' % (new_filepath, new))