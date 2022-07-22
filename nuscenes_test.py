# coding:utf-8
from nuscenes.nuscenes import NuScenes
nusc = NuScenes(version='v1.0-mini', dataroot='E:\code\\nuscenes\dataset', verbose=True)
import time

nusc.list_scenes()

my_scene = nusc.scene[0]
print(my_scene)

first_sample_token = my_scene['first_sample_token']  #获取第一个sample的token值
print(first_sample_token)

my_sample = nusc.get('sample', first_sample_token)
print(my_sample)

print(my_sample['data'])

# 可视化前方的毫米波雷达传感器
# sensor_radar = 'RADAR_FRONT'  #这里选择的传感器为前方的毫米波雷达传感器
# radar_front_data = nusc.get('sample_data',my_sample['data'][sensor_radar])
# print(radar_front_data)
#
# print("-" * 50)
# nusc.render_sample_data(radar_front_data['token'])

# 可视化前方的相机
sensor_CAM_FRONT = 'CAM_FRONT'  #这里选择的传感器为前方的毫米波雷达传感器
CAM_FRONT_data = nusc.get('sample_data', my_sample['data'][sensor_CAM_FRONT])
print(CAM_FRONT_data)
nusc.render_sample_data(CAM_FRONT_data['token'])

# 可视化顶部激光雷达
# sensor_LIDAR_TOP = 'LIDAR_TOP'  #这里选择的传感器为前方的毫米波雷达传感器
# LIDAR_TOP_data = nusc.get('sample_data', my_sample['data'][sensor_LIDAR_TOP])
# print(LIDAR_TOP_data)
# nusc.render_sample_data(LIDAR_TOP_data['token'])

# 获取特定sample的标注信息
# print("-" * 50)
# my_annotation_token = my_sample['anns'][18]
# my_annotation_metadata = nusc.get('sample_annotation', my_annotation_token)
# print(my_annotation_metadata)
# # 可视化
# nusc.render_annotation(my_annotation_metadata['token'])
# time.sleep(3)


# 获取某个实例对象，并输出其信息
# my_instance = nusc.instance[5]
# print(my_instance)
# # 通过实例的token值，进行可视化
# instance_token = my_instance['token']
# nusc.render_instance(instance_token)
# time.sleep(3)

# print("-" * 50)
# nusc.list_categories()
#
# nusc.list_attributes()


# 可视化
# print("-" * 50)
# # 选取当前sample标注信息中的一个token值
# anntoken = my_sample['anns'][9]
# visibility_token = nusc.get('sample_annotation', anntoken)['visibility_token']
# print("Visibility: {}".format(nusc.get('visibility', visibility_token)))
# nusc.render_annotation(anntoken)
# time.sleep(3)

# # 展示传感器信息
# print("-" * 50)
# print(nusc.sensor)
#
# # 展示传感器的校准信息
# sensor_token = nusc.calibrated_sensor[0]
# print(sensor_token)
#
# # 车辆姿态ego_pose信息
# print(nusc.ego_pose[0])
#
# # 日志信息
# print(nusc.log[0])
#
# # 地图信息
# print(nusc.map[0])