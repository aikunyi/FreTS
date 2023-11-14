#Frequency-domain MLPs are More Effective Learners in Time Series Forecasting

This repo is the official Pytorch implementation of ["Frequency-domain MLPs are More Effective Learners in Time Series Forecasting"](https://arxiv.org/pdf/2311.06184.pdf).

### Running the code
- forecasting

`python run_longExp.py`

- draw the visualization

`python weight_plot.py`

put the corresponding checkpoint file into the test directory, and select the corresponding weights (e.g., w) to visualize


## Citation

If you find this repo useful, please cite our paper. 

```
@inproceedings{yi2023frequencydomain,
title={Frequency-domain {MLP}s are More Effective Learners in Time Series Forecasting},
author={Kun Yi and Qi Zhang and Wei Fan and Shoujin Wang and Pengyang Wang and Hui He and Ning An and Defu Lian and Longbing Cao and Zhendong Niu},
booktitle={Thirty-seventh Conference on Neural Information Processing Systems},
year={2023}
}
```

## Acknowledgement

We appreciate the following github repos a lot for their valuable code base or datasets:

1. Informer: https://github.com/zhouhaoyi/Informer2020
2. Autoformer: https://github.com/thuml/Autoformer
3. FEDformer: https://github.com/MAZiqing/FEDformer
4. LTSF-Linear: https://github.com/cure-lab/LTSF-Linear
5. PatchTST: https://github.com/PatchTST