# -*- coding: utf-8 -*-            
# @Author : buyfakett
# @Time : 2024/11/20 09:15
import os, json

from src.pictures import generate_url_json

def generate_headers():
    uris = ["/pictures"]

    # 确保 dist 目录存在
    os.makedirs("dist", exist_ok=True)

    # 写入 _headers 文件
    with open("dist/_headers", "w", encoding="utf-8") as f:
        for uri in uris:
            f.write(f"{uri}\n")

            # 默认的 Content-Type
            f.write("  Content-Type: text/plain; charset=utf-8\n")

            f.write("\n")

if __name__ == '__main__':
    pictures = generate_url_json('picture_list.txt')
    # 确保目标目录存在
    os.makedirs("dist", exist_ok=True)
    with open('dist/pictures', 'w', encoding='utf-8') as file:
        json.dump(pictures, file, ensure_ascii=False, indent=4)  # 使用 JSON 格式写入
    generate_headers()