import torch
import numpy as np
import os 
import matplotlib.pyplot as plt

for root, dirs, files in os.walk("test"):
    for name in files:
        model_path = os.path.join(root, name)
        weights = torch.load(model_path, map_location=torch.device('cpu'))
        weights_list = {}

        # energy compaction
        weights_list['f_r'] = (1 / np.max(weights['f_r'].numpy())) * weights['f_r'].numpy()
        weights_list['f_i'] = (1 / np.max(weights['f_i'].numpy())) * weights['f_i'].numpy()

        save_root = '/figs'

        for w_name,weight in weights_list.items():
            fig,ax=plt.subplots()
            im=ax.imshow(weight, cmap='plasma_r')
            fig.colorbar(im,pad=0.03)
            plt.savefig(os.path.join(save_root,w_name + '.pdf'),dpi=500)
            plt.close()
 