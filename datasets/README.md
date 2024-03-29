# Prepare Datasets for OVFormer

OVFormer has builtin support for a few datasets.
The datasets are assumed to exist in a directory specified by the environment variable
`DETECTRON2_DATASETS`.
Under this directory, detectron2 will look for datasets in the structure described below, if needed.
```
$DETECTRON2_DATASETS/
  coco/
  lvis/
  LVVIS/
  ytvis_2019/
  ytvis_2021/
  ovis/
  metadata/
```

You can set the location for builtin datasets by `export DETECTRON2_DATASETS=/path/to/datasets`.
If left unset, the default is `./datasets` relative to your current working directory.

<!-- The [model zoo](https://github.com/facebookresearch/MaskFormer/blob/master/MODEL_ZOO.md)
contains configs and models that use these builtin datasets. -->

## STEP-1: Prepare Image & Video Instance Segmentation datasets
### Expected dataset structure for [COCO](https://cocodataset.org/#download):

```
coco/
  annotations/
    instances_{train,val}2017.json
  {train,val}2017/
```

### Expected dataset structure for [LVIS](https://www.lvisdataset.org/dataset):

```
lvis/
  lvis_v1_train.json
  lvis_v1_val.json
```
Next, prepare the open-vocabulary LVIS training set using
```bash
python tools/remove_lvis_rare.py --ann datasets/lvis/lvis_v1_train.json
```
This will generate```datasets/lvis/lvis_v1_train_norare.json.```

### Expected dataset structure for [LV-VIS](https://github.com/haochenheheda/LVVIS):

```
LVVIS/
  train/
    JPEGImages/
    train_instances.json
  val/
    JPEGImages/
    val_instances.json  
  test/
    JPEGImages/
```
Next, prepare the open-vocabulary LV-VIS training set using
```bash
python tools/remove_lvvis_novel.py --ann datasets/LVVIS/train/train_instances.json
```
This will generate```datasets/LVVIS/train/train_instances_nonovel.json.```

### Expected dataset structure for [YouTubeVIS 2019](https://codalab.lisn.upsaclay.fr/competitions/7682):

```
ytvis_2019/
  {train,valid,test}.json
  {train,valid,test}/
    JPEGImages/
```

### Expected dataset structure for [YouTubeVIS 2021](https://codalab.lisn.upsaclay.fr/competitions/7680):

```
ytvis_2021/
  {train,valid,test}.json
  {train,valid,test}/
    JPEGImages/
```

### Expected dataset structure for [OVIS](https://codalab.lisn.upsaclay.fr/competitions/4763):

```
ovis/
  annotations/
    {train,valid,test}.json
  {train,valid,test}/
```

## STEP-2: Prepare metadata
#### Download [metadata](https://drive.google.com/file/d/1-qnYtlHSBoraUyr69o3Kds-CD-5xeNTR/view?usp=sharing), and organize the files according to the following structure:
```
metadata/
  fg_bg_5_10_coco_ens.npy
  fg_bg_5_10_lvis_ens.npy
  fg_bg_5_10_lvvis_ens.npy
  fg_bg_5_10_ovis_ens.npy
  fg_bg_5_10_ytvis19_ens.npy
  fg_bg_5_10_ytvis21_ens.npy
```
the metadata contains pre-computed classifiers for each dataset, which are generated by [DetPro](https://github.com/dyabel/detpro). 
If you want to generate customer classifiers, please follow this project.

```
metadata/
  lvis_v1_train_cat_info.json
  lvvis_train_cat_info.json
```
the metadata contains category information for two training sets, 
which are generated by [get_lvis_cat_info](../tools/get_lvis_cat_info.py) and [get_lvvis_cat_info](../tools/get_lvvis_cat_info.py).

```
metadata/
  lvis_train_clip_feature.pkl
  lvis_val_clip_feature.pkl
  lvvis_train_clip_feature.pkl
  lvvis_val_clip_feature.pkl
  ytvis_2019_val_clip_feature.pkl
  ytvis_2021_val_clip_feature.pkl
  ovis_val_clip_feature.pkl
```
the metadata contains CLIP image features for each dataset, 
which are generated by [save_clip_features](../tools/save_clip_features.py)

## STEP-3: Prepare Pretrained Model
Like [OV2Seg](https://github.com/haochenheheda/LVVIS), our paper uses ImageNet-21K pretrained models that are not part of Detectron2 (ResNet-50-21K from [MIIL](https://github.com/Alibaba-MIIL/ImageNet21K) and SwinB-21K from [Swin-Transformer](https://github.com/microsoft/Swin-Transformer)). Before training, 
please download the models and place them under `models/`, and following [this tool](../tools/convert-thirdparty-pretrained-model-to-d2.py) to convert the format.

```
models/
  resnet50_miil_21k.pkl
  swin_base_patch4_window12_384_22k.pkl
datasets/
  metadata/
  ...
```