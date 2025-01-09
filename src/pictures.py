# -*- coding: utf-8 -*-            
# @Author : buyfakett
# @Time : 2025/1/2 17:17
import requests
import json
from PIL import Image
from io import BytesIO

# 默认描述
DEFAULT_DESCRIPTION = "这是一张图片"


# 读取 JSON 文件
def read_images_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        images = json.load(file)

    # 遍历每个图片，检查是否有描述字段，如果没有则填充默认描述
    for image in images:
        # 使用 .get() 来获取 description，如果没有则使用默认值
        image['description'] = image.get('description', DEFAULT_DESCRIPTION)

    return images


# 获取图片的宽和高
def get_image_size(url):
    try:
        response = requests.get(url, timeout=5)
        img = Image.open(BytesIO(response.content))
        return img.size  # 返回 (width, height)
    except Exception as e:
        print(f"Error fetching image from {url}: {e}")
        return None


# 生成带有图片信息的 JSON 输出
def generate_url_json(file_path):
    images = read_images_from_file(file_path)

    result = {
        "urls": [],
        "count": len(images)
    }

    # 获取每个图片的宽和高
    for image in images:
        size = get_image_size(image['url'])
        if size:
            width, height = size
            result["urls"].append({
                "url": image['url'],
                "description": image['description'],
                "width": width,
                "height": height
            })
        else:
            result["urls"].append({
                "url": image['url'],
                "description": image['description'],
                "width": None,
                "height": None
            })

    return result
