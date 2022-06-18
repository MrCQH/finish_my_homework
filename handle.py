import os
import shutil
from imutils import paths

flowr_name = [ ' ', 'daffodil', 'snowdrop', 'lily_valley', 'bluebell',
              'crocus', 'iris', 'tigerlily', 'tulip', 'fritillary',
              'sunflower', 'daisy', 'colts_foot', 'dandelion', 'cowslip',
              'buttercup','windflower', 'pansy']


for i in range(1, 18):
    i = str(flowr_name[i])
    if os.path.exists(i) is False:
        os.makedirs(i)

dataset_dir = os.path.abspath(r"./origin_dataset")

picture_list = list(paths.list_images(dataset_dir)) # 存放1360张图片的文件夹

picture_list.sort()

pic_num = 0  # 用来计数1360，便于接下来遍历存储图片


for i in range(1, 18):
    value = 0
    file_path = os.path.abspath(str(flowr_name[i]))
    while value < 80:
        shutil.copy(picture_list[pic_num], file_path)  # 这个是复制语句，将picture_list的图片复制到file文件夹里

        pic_num += 1
        value += 1
