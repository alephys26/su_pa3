import shutil
import os
def combine(directory):
    for subdir in os.listdir(directory):
        for file in os.listdir(directory+'/'+subdir):
            shutil.copy(directory+'/'+subdir+'/'+file, directory+'/combined/'+subdir+'_'+file)

combine('/home/yash26/SU/PA3/data/for-2sec/for-2seconds/testing')
combine('/home/yash26/SU/PA3/data/for-2sec/for-2seconds/validation')
combine('/home/yash26/SU/PA3/data/for-2sec/for-2seconds/training')
