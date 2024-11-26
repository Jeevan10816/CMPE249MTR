# -*- coding: utf-8 -*-
"""MTR_Waymo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eF3-S9j5zLWKXj7p6OPbbcJeKix5tmLi
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/content/drive')
# %cd drive

# Commented out IPython magic to ensure Python compatibility.
# %cd MyDrive
!ls -la

!sudo apt-get install python3.8-venv python3.8-dev python3-pip -y

#!pip install -r mrtrequirements.txt

#!git clone https://github.com/sshaoshuai/MTR.git

# Commented out IPython magic to ensure Python compatibility.
# %cd MTR

!python3 setup.py install

#only run it once

#!pip install waymo-open-dataset-tf-2-11-0

# Commented out IPython magic to ensure Python compatibility.
# %cd mtr/datasets/waymo

from google.colab import auth
auth.authenticate_user()

#!gsutil -m cp -r \
#  "gs://waymo_open_dataset_motion_v_1_2_0/uncompressed/scenario/testing" \
#  .

#!gsutil -m cp -r \
#  "gs://waymo_open_dataset_motion_v_1_2_0/uncompressed/scenario/training" \
#  .

#!gsutil -m cp -r \
#  "gs://waymo_open_dataset_motion_v_1_2_0/uncompressed/scenario/validation" \
#  .

#!pip install numpy==1.23

#only need to run once as well

!python3 data_preprocess.py ../../../data/waymo/scenario/  ../../../data/waymo

# Commented out IPython magic to ensure Python compatibility.
# %cd ../../../tools

#training

!bash scripts/dist_train.sh 8 --cfg_file cfgs/waymo/mtr+100_percent_data.yaml --batch_size 80 --epochs 30 --extra_tag my_first_exp

#validation

bash scripts/dist_test.sh 8 --cfg_file cfgs/waymo/mtr+100_percent_data.yaml --ckpt ../output/waymo/mtr+100_percent_data/my_first_exp/ckpt/checkpoint_epoch_30.pth --extra_tag my_first_exp --batch_size 80