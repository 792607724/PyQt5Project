# coding = utf8
import glob
import multiprocessing
import os
import threading
from time import sleep

os.path.abspath("../uifile")
"""
    @Project:pythonProject_seevision
    @File:pc.py
    @Author:十二点前要睡觉
    @Date:2022/3/10 10:49
"""

"""
    Description:
    图片坏点检测：
    1、0 - 纯白图片检测：判断每个像素点Y亮度小于-5即为坏点
    2、1 - 纯黑图片检测：判断每个像素点Y亮度大于60即为坏点
    
    换算公式：
    Y(亮度)=(0.299*R)+(0.587*G)+(0.114*B)
    
    判断单张图片是否PASS：坏点数不超过0.002%
    
"""

from PIL import Image


class PointCheck:

    def __init__(self, picture_path, check_type, picture_name):
        """
        坏点检测实现脚本 - 初始化函数
        :param picture_path:待检测图片路径
        :param check_type:待检测图片的检测类型
        :param picture_name:待检测图片名称
        """
        self.picture_path = picture_path
        self.check_type = check_type
        self.img_src = Image.open(self.picture_path)
        self.picture_name = picture_name

    def getPictureSize(self):
        """
        获取待检测图片的宽高值
        :return:返回待检测图片宽高值
        """
        return self.img_src.size

    def getPicturePixels(self):
        """
        获取待检测图片的所有像素点
        :return:返回待检测图片的所有像素点
        """
        img_src = self.img_src.convert("RGBA")
        pixel_list = img_src.load()
        return pixel_list

    def getAll_pixelsCoordinate(self, picture_size):
        """
        获取待检测图片的所有像素点的坐标
        :param picture_size:待检测图片宽高值
        :return:返回包含所有像素点的坐标列表
        """
        point_coordinate = []
        for x in range(0, picture_size[0]):
            for y in range(0, picture_size[1]):
                point_coordinate.append((x, y))
        return point_coordinate

    def analysis_point_info(self, pixel_list, point_coordinate, check_type):
        """
        亮/暗像素点分析，分析一张图片的所有像素点，找出坏点的个数、位置，并生成一张新的图片，坏点使用其他颜色突出显示，指出图片总像素点数以及坏点数
        :param pixel_list:待检测图片所有像素点列表
        :param point_coordinate:待检测图片的所有像素点的坐标
        :param check_type:待检测图片的检测类型
        :return:返回每张图片的检测结果和坏点列表（包含每个坏点的坐标和亮度值）再对每张图片进行坏点突出绘制一张新的图片
        """
        # 每个像素点一个进程去分析
        bad_point_list = []
        for point in point_coordinate:
            # (215, 186, 154, 255)
            point_info = pixel_list[point]
            point_r = point_info[0]
            point_g = point_info[1]
            point_b = point_info[2]
            # print(point_info)
            # print("R is：{}".format(point_r))
            # print("G is：{}".format(point_g))
            # print("B is：{}".format(point_b))
            """
            换算公式：
            Y(亮度)=(0.299*R)+(0.587*G)+(0.114*B)
            """
            point_Y = 0.299 * point_r + 0.587 * point_g + 0.114 * point_b
            # print(point_Y)
            """
            图片坏点检测：
            1、0 - 纯白图片检测：判断每个像素点Y亮度小于-5即为坏点
            2、1 - 纯黑图片检测：判断每个像素点Y亮度大于60即为坏点
            
            判断单张图片是否PASS：坏点数不超过0.002%
            """
            if check_type == 1:
                if point_Y > 60:
                    bad_point_list.append({"coordinate": point, "Y": point_Y})
            elif check_type == 0:
                if point_Y < -5:
                    bad_point_list.append({"coordinate": point, "Y": point_Y})
        if bad_point_list:
            print("当前图片【{}】总像素点【{}】，坏点数【{}】".format(self.picture_name, len(point_coordinate), len(bad_point_list)))
            if len(bad_point_list) / len(point_coordinate) <= 0.00002:
                picture_infos = {"bad_point_list": bad_point_list, "result": "PASS",
                                 "wholePointCount": len(point_coordinate)}
            else:
                picture_infos = {"bad_point_list": bad_point_list, "result": "FALSE",
                                 "wholePointCount": len(point_coordinate)}
            # 返回每张图片的检测结果和坏点列表（包含每个坏点的坐标和亮度值）再对每张图片进行坏点突出绘制一张新的图片
            return picture_infos
        else:
            print("{} - 图片没有坏点!!!".format(self.picture_name))

    def rebuild_picture_forBADPoint(self, picture_infos):
        """
        对有坏点的图片进行坏点突出，重新绘制一张新的图片
        :param picture_infos:图片检测后的数据，包括所有坏点坐标、该图片的测试结果、总像素点数
        :return:None
        """
        # 图片命名 原图片名+总像素点数+坏点数.jpg
        # print(picture_infos)
        bad_point_list = picture_infos["bad_point_list"]
        for one_point in bad_point_list:
            # print(one_point)
            point_l = (one_point["coordinate"][0], one_point["coordinate"][1])
            self.img_src.putpixel(point_l, (234, 53, 57, 255))
        print("Done")
        self.img_src = self.img_src.convert("RGB")
        if not os.path.exists("./convertPicture/"):
            os.mkdir("./convertPicture/")
        self.img_src.save(
            "./convertPicture/测试结果【{}】总点数{}有{}个坏点_{}".format(picture_infos["result"], picture_infos["wholePointCount"],
                                                             len(bad_point_list),
                                                             self.picture_name))


def bad_check_area(picture_path, check_type, picture):
    """
    单张图片坏点检测流程控制
    :param picture_path:待检测图片路径
    :param check_type:待检测图片的检测类型
    :param picture:待检测图片名称
    :return:None
    """
    pc = PointCheck(picture_path, check_type, picture)
    point_coordinate = pc.getAll_pixelsCoordinate(pc.getPictureSize())
    picture_infos = pc.analysis_point_info(pc.getPicturePixels(), point_coordinate, check_type)
    if picture_infos:
        pc.rebuild_picture_forBADPoint(picture_infos)


def interface_Out(image_path):
    """
        Description:坏点检测流程控制
        图片坏点检测：
        1、0 - 纯白图片检测：判断每个像素点Y亮度小于-5即为坏点
        2、1 - 纯黑图片检测：判断每个像素点Y亮度大于60即为坏点
        换算公式：
        Y(亮度)=(0.299*R)+(0.587*G)+(0.114*B)
        判断单张图片是否PASS：坏点数不超过0.002%
        :param image_path:待检测图片路径
    """

    # glob 优化筛选模式 节约算力
    types = ("*.jpg", "*.bmp")
    files_list = []
    for files in types:
        files_list.extend(glob.glob(os.path.join(image_path, files)))
    print(files_list)
    pictureFile = os.listdir(image_path)
    check_type = 1
    for picture in files_list:
        if len(pictureFile) >= 10:
            sleep(1)
        print("正在分析图片：{},图片较多请耐心等候！ ".format(picture))
        t = threading.Thread(target=bad_check_area, args=(picture, check_type, picture.split("\\")[1],))
        t.start()
        t.join(3)
    return "Done"


if __name__ == '__main__':
    image_path = "./pictures_cat/"
    interface_Out(image_path)
