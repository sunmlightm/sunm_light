# _*_coding:utf-8_*_
# Author : sunm
# @Time :  20:31
#tesseract是google维护的具有学习功能的OCR引擎，3.0以后支持中文识别
import pytesseract
#Python Imaging Library，已经是Python平台事实上的图像处理标准库了。
# PIL功能非常强大，但API却非常简单易用
from PIL import Image

#使用PIL的Image.open()函数加载图片
image = Image.open("world.jpg")
# print(image)

#使用pytesseract模块的image_to_string把图片识别成文字
text = pytesseract.image_to_string(image)
#打印文本
print(text)
