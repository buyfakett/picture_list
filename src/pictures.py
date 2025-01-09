# -*- coding: utf-8 -*-            
# @Author : buyfakett
# @Time : 2025/1/2 17:17
import requests
from PIL import Image
from io import BytesIO

# 读取 URLs 列表
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    # 移除每行末尾的换行符并返回
    return [url.strip() for url in urls]

def get_image_size(url):
    """
    获取图片的宽和高
    """
    try:
        response = requests.get(url, timeout=5)
        img = Image.open(BytesIO(response.content))
        return img.size  # 返回 (width, height)
    except Exception as e:
        print(f"Error fetching image from {url}: {e}")
        return None

def generate_url_json(file_path):
    urls = read_urls_from_file(file_path)

    result = {
        "urls": [],
        "count": len(urls)
    }

    # 获取每个图片的宽和高
    for url in urls:
        size = get_image_size(url)
        if size:
            width, height = size
            result["urls"].append({
                "url": url,
                "width": width,
                "height": height
            })
        else:
            result["urls"].append({
                "url": url,
                "width": None,
                "height": None
            })

    return result