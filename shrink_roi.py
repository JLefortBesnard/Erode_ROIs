"""
Erode the nifti ROIs
2020
Author:    
        Jeremy Lefort-Besnard   jlefortbesnard (at) tuta (dot) io
"""

import nibabel as nib
from scipy import ndimage
import glob

n_ite = 2
for img_path in glob.glob("*.nii"):
    # load the original nifti image
    img = nib.load(img_path)
    # extract data
    img_data = img.get_data()
    # shrinked the ROI twice
    img_data_shrinked = ndimage.binary_erosion(img_data, iterations=n_ite).astype(img_data.dtype)     
    # build the nifti image of the new shape
    img_shrinked = nib.Nifti1Image(img_data_shrinked, img.affine, img.header)
    # save the file
    new_img_name = img_path[:-4] + "shrink_2ite"
    nib.save(img_shrinked, new_img_name)
    
