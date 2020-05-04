import nibabel as nib
import os
import numpy as np
from nilearn import plotting
import numpy as np

# plotting.view_img_on_surf(img, threshold='90%', surf_mesh='fsaverage').open_in_browser() 

from scipy import ndimage
import matplotlib.pyplot as plt

# plotting.plot_glass_brain(img, threshold=0.1)
# plotting.plot_glass_brain(img_shrinked, threshold=0.1)
# plotting.show()

import glob
for img_path in glob.glob("*relevant_*.nii"):
    img = nib.load(img_path)
    img_data = img.get_data()
    img_data_shrinked = ndimage.binary_erosion(img_data, iterations=2).astype(img_data.dtype)     
    img_shrinked = nib.Nifti1Image(img_data_shrinked, img.affine, img.header)
    new_img_name = "shrinked_imgs_2/" + img_path[:-4] + "shrinked2"
    nib.save(img_shrinked, new_img_name)
    

# keep normal size 
# 8, 4, 1, 11, 12, 13, 14
# shrink 
# 3, 5, 6, 7, 15, 2, 9, 10






