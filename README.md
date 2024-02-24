## Installation

See [installation instructions](INSTALL.md).

## Data Preparation
See [Preparing Datasets for OVFormer](./datasets/README.md).

##  Getting Started
We firstly train the OVFormer model on LVIS dataset:
```bash
python train_net.py --num-gpus 8 \
  --config-file configs/lvis/ovformer_R50_bs8.yaml
```
To evaluate a model's performance on YouTubeVIS and OVIS datasets, use
```bash
python train_net_video.py \
  --config-file configs/youtubevis_2019/ovformer_R50_bs8.yaml \
  --eval-only MODEL.WEIGHTS models/ovformer_r50_lvis.pth
```
Upload to the specified server, you are expected to get results like this:

|    Name     | Backbone | YTVIS19 | YTVIS21 | OVIS |
|:-----------:|:--------:|:-------:|:-------:|:----:|
|  OVFormer   |   R-50   |  34.8   |  29.8   | 15.1 |
|  OVFormer   |  Swin-B  |  44.3   |  37.6   | 21.3 | 

Then, we train the OVFormer model on LV-VIS dataset:
```bash
python train_net_lvvis.py --num-gpus 8 \
  --config-file configs/lvvis/video_ovformer_R50_bs8.yaml
```
To evaluate a model's performance on LV-VIS dataset, use
```bash
python train_net_lvvis.py \
  --config-file configs/lvvis/video_ovformer_R50_bs8.yaml \
  --eval-only MODEL.WEIGHTS models/ovformer_r50_lvvis.pth
```
Run ```mAP.py```, you are expected to get results like this:

|    Name     | Backbone | mAP  | mAPb | mAPn |
|:-----------:|:--------:|:----:|:----:|:----:|
|  OVFormer   |   R-50   | 21.9 | 22.1 | 21.8 |
|  OVFormer   |  Swin-B  | 24.7 | 26.8 | 23.1 |


## Acknowledgement

This repo is based on [detectron2](https://github.com/facebookresearch/detectron2), 
[Mask2Former](https://github.com/facebookresearch/Mask2Former),
and [LVVIS](https://github.com/haochenheheda/LVVIS). Thanks for their great work!
