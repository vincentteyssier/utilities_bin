try:
    import Image
except ImportError:
    from PIL import Image

import os
import shutil

origin_path = r"C:\tmp\Face_dataset\ck+simplecropeddata\VideoGreaterThan8"
i = 0
for root, dirs, files in os.walk(origin_path):
    for file in files:
        if file.endswith('.png') or file.endswith('.PNG'):
            fullpath = os.path.join(root, file)
            im = Image.open(fullpath)
            rgb_im = im.convert('RGB')
            rgb_im.save(fullpath+'.jpg')
            print (i)
            i = i + 1