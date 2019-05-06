# Code stub taken from https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory

import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

base_dir = os.getcwd()
# I hate doing this but you need to actually change your working directory to the folder you need
# otherwise the zip will include subfolders for all folders between your current working directory
# and the directory you want to zip

os.chdir('layers/pandas')
zipf = zipfile.ZipFile('pandas_lambda.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('python/', zipf)
zipf.close()