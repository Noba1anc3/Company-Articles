import json
import os
import cv2
import shutil

# 构建categories
classes = ['chapter', 'section', 'clause', 'subclause', 'body']
categories = []
for index, item in enumerate(classes):
    cat = {'supercategory': '', 'id': index, 'name': item}
    categories.append(cat)

# 构建images，同时annotations
path = "./output/prediction"
all_doc_path = os.path.join(path, 'image')
images, annotations = [], []
img_id, anno_id= 0, 0
for doc_index in os.listdir(all_doc_path):
    doc_path = os.path.join(all_doc_path, doc_index)
    for img_name in os.listdir(doc_path):
        img_path = os.path.join(doc_path, img_name)
        shutil.copy(img_path, os.path.join('./images', img_name))  # 把所有图片复制到另一个文件夹中

        img = cv2.imread(img_path)
        image = {
            'id': img_id,
            'file_name': img_name,
            'height': img.shape[0],
            'width': img.shape[1]
        }
        images.append(image)

        # 构建单个annotation并加入annotations中
        anno_path = img_path.replace('image', 'json').replace('jpg', 'txt')
        for line in open(anno_path):
            words = line.split(' ')
            cl, x0, y0, x1, y1 = words[0], int(words[1]), int(words[2]), int(words[3]), int(words[4])
            anno = {
                'segmentation': [[x0, y0, x1, y1, x0, y1, x1, y0]],
                'area': (x1 - x0) * (y1 - y0),
                'iscrowd': 0,
                'image_id': img_id,
                'bbox': [x0, y0, x1 - x0, y1 - y0],
                'category_id': classes.index(cl),
                'id': anno_id
            }
            annotations.append(anno)
            anno_id += 1
        img_id += 1

# 生成publaynet格式json并存储
train_dict = {'images': images, 'annotations': annotations, 'categories': categories}
# train_json = json.dumps(train_dict)

json_path = './train.json'
with open(json_path, 'w') as json_file:
    json.dump(train_dict, json_file)