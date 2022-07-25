# coding:utf-8

import matplotlib as plt
import os
from nuscenes import NuScenes
nusc = NuScenes(version='v1.0-mini', dataroot='./dataset', verbose=True)

# 展示lidarseg的种类，按count排列，从小到大排列
nusc.list_lidarseg_categories(sort_by='count')

# 按索引顺序获取类名
print(nusc.lidarseg_idx2name_mapping)

# 按类名获取索引顺序
print(nusc.lidarseg_name2idx_mapping)

# 从panoptic检查每个语义类别的点数
# nuscenes-panoptic
nusc.list_lidarseg_categories(sort_by='count', gt_from='panoptic')

# 该函数将计算每帧的实例数，实例总数(唯一的对象ID)和实例状态(一个实例可能有多个状态)。
# 它还计算每个类别的统计数据，包括一个实例跨越的帧数的平均值和标准偏差，以及每个实例的点数的平均值和标准偏差。
nusc.list_panoptic_instances(sort_by='count')

# 获取一个sample
my_sample = nusc.sample[5]
# nuscenes-lidarseg
nusc.get_sample_lidarseg_stats(my_sample['token'], sort_by='count')


# 从nuscenes-panoptic中获取
nusc.get_sample_lidarseg_stats(my_sample['token'], sort_by='count', gt_from='panoptic')

# 渲染lidarseg
sample_data_token = my_sample['data']['LIDAR_TOP']
nusc.render_sample_data(sample_data_token,
                        with_anns=True,
                        show_lidarseg=True)

# 通过类别索引进行过滤
nusc.render_sample_data(sample_data_token,
                        with_anns=False,
                        show_lidarseg=True,
                        filter_lidarseg_labels=[17, 23])


# 显示图例
nusc.render_sample_data(sample_data_token,
                        with_anns=False,
                        show_lidarseg=True,
                        show_lidarseg_legend=True)

# 渲染panoptic标签
sample_data_token = my_sample['data']['LIDAR_TOP']
nusc.render_sample_data(sample_data_token,
                        with_anns=False,
                        show_lidarseg=False,
                        show_panoptic=True)

# show trucks and car
nusc.render_sample_data(sample_data_token,
                        with_anns=False,
                        show_panoptic=True,
                        filter_lidarseg_labels=[17, 23])

# show stuff category legends
nusc.render_sample_data(sample_data_token,
                        with_anns=False,
                        show_lidarseg=False,
                        show_lidarseg_legend=True,
                        show_panoptic=True)

# nuscenes-lidarseg
# 将点云叠加到相机对应的图像中
nusc.render_pointcloud_in_image(my_sample['token'],
                                pointsensor_channel='LIDAR_TOP',
                                camera_channel='CAM_FRONT',
                                render_intensity=False,
                                show_lidarseg=True,
                                filter_lidarseg_labels=[17, 23, 24],
                                show_lidarseg_legend=True)

# nuscenes-panoptic
# 显示全景标签而不是语义标签。只显示物品类别的图例。
nusc.render_pointcloud_in_image(my_sample['token'],
                                pointsensor_channel='LIDAR_TOP',
                                camera_channel='CAM_FRONT',
                                render_intensity=False,
                                show_lidarseg=False,
                                filter_lidarseg_labels=[17, 23, 24],
                                show_lidarseg_legend=True,
                                show_panoptic=True)

# nuscenes-lidarseg
nusc.render_sample(my_sample['token'],
                   show_lidarseg=True,
                   filter_lidarseg_labels=[17, 23])

# 要使用render_sample显示panoptic标签，只需设置show_panoptic=True
# nuscenes-panoptic
nusc.render_sample(my_sample['token'],
                   show_lidarseg=False,
                   filter_lidarseg_labels=[17, 23],
                   show_panoptic=True)


my_scene = nusc.scene[0]
# nuscenes-lidarseg
nusc.render_scene_channel_lidarseg(my_scene['token'],
                                   'CAM_FRONT',
                                   filter_lidarseg_labels=[18, 28],
                                   verbose=True,
                                   dpi=100,
                                   imsize=(1280, 720))


# nuscenes-lidarseg
import os
nusc.render_scene_lidarseg(my_scene['token'],
                           filter_lidarseg_labels=[17, 24],
                           verbose=True,
                           dpi=100)



my_sample = nusc.sample[80]
sample_data_token = my_sample['data']['LIDAR_TOP']
my_predictions_bin_file = os.path.join('./dataset/lidarseg/v1.0-mini', sample_data_token + '_lidarseg.bin')

nusc.render_pointcloud_in_image(my_sample['token'],
                                pointsensor_channel='LIDAR_TOP',
                                camera_channel='CAM_BACK',
                                render_intensity=False,
                                show_lidarseg=True,
                                filter_lidarseg_labels=[22, 23],
                                show_lidarseg_legend=True,
                                lidarseg_preds_bin_path=my_predictions_bin_file)


my_sample = nusc.sample[87]
sample_data_token = my_sample['data']['LIDAR_TOP']
my_predictions_bin_file = os.path.join('./dataset/panoptic/v1.0-mini', sample_data_token + '_panoptic.npz')

nusc.render_pointcloud_in_image(my_sample['token'],
                                pointsensor_channel='LIDAR_TOP',
                                camera_channel='CAM_BACK',
                                render_intensity=False,
                                show_lidarseg=False,
                                filter_lidarseg_labels=[17,22, 23, 24],
                                show_lidarseg_legend=True,
                                lidarseg_preds_bin_path=my_predictions_bin_file,
                                show_panoptic=True)
