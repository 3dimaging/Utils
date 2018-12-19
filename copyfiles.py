# this is a pythons script to copy files in a list.
# author: Weizhe Li
# date: 12-18-2018
# aim: this script is made because sometimes not all the files were copied to the destination folder, there are certain uncopied file.


# first part is to generate a list to include the uncopied files



import os
import numpy as np
import shutil


hnm_patches = os.listdir(os.getcwd())
all_patches = np.load('/home/wli/hnm_all_patches.npy')
hnm_patches.sort()
all_patches.sort()
remained_patches_tocopy = [x for x in all_patches if x not in hnm_patches]
np.save('/home/wli/remained_patches_tocopy.npy', remained_patches_tocopy)
#remained_patches_tocopy
len(remained_patches_tocopy)

src = '/home/wli/Downloads/patchesfortraining/HNM/augtumor_hnm'
import numpy as np
cpatches = np.load('/home/wli/remained_patches_tocopy.npy')
dest = '/home/wli/Downloads/hnm_remain'
for file_name in cpatches:
	full_file_name = os.path.join(src, file_name)
	if (os.path.isfile(full_file_name)):
		shutil.copy(full_file_name, dest)
# save the command line of python in an interactive environment 
import readline
with open('history.txt', 'w') as f:
	for i in range(readline.get_current_history_length()):
		f.write(readline.get_history_item(i+1)+ "\n")
