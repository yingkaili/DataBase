# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib

from fuli import settings


class FuliPipeline(object):

    # __init__方法是可选的，做为类的初始化方法
    def __init__(self):
        # 创建了一个文件
        self.filename = open("fuli.json", "w")

    # process_item方法是必须写的，用来处理item数据
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii = False) + "\n"
        self.filename.write(jsontext.encode("utf-8"))
        dir_path = '%s/%s'%(settings.IMAGES_STORE,spider.name)#存储路径
        #print 'dir_path',dir_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item['douPicture']:
            print 'image_url',image_url
            list_name = image_url.split('/')
            file_name = list_name[len(list_name)-1]#图片名称
            # print 'filename',file_name
            file_path = '%s/%s'%(dir_path,file_name)
            # print 'file_path',file_path
            if os.path.exists(file_name):
                continue
            with open(file_path,'wb') as file_writer:
                conn = urllib.urlopen(image_url)#下载图片
                file_writer.write(conn.read())
            file_writer.close()
        return item

    # close_spider方法是可选的，结束时调用这个方法
    def close_spider(self, spider):
        self.filename.close()

