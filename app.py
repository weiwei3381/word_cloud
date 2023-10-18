# coding: utf-8
# @Time : 2023/10/19 0:59
# @Author : wowbat
# @File : main.py.py
# @Describe: 

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 需要显示的文本内容
texts = [
    [('张XX，男，21岁，学号20210703', 1), ('2021年高考入学', 1), ('工程装备管理与维修专业（本科）', 1),
     ('入学成绩和排名：562（7/16）', 3), ('爱好特长：足球，长跑', 3)],
    [('平均绩点（GPA）3.5', 3), ('课程通过率100%', 3), ('学分修满度58%', 3), ('基础课成绩和排名82分（5/16）', 2),
     ('专业课成绩和排名：85分（3/16）', 2)],
    [('学习方法好；自我管理能力强', 1), ('学术成绩优秀，XX学科竞赛奖X次（1/3）', 3), ('实习和实践成绩：87（3/16）', 2)],
    [('领导能力强', 1), ('协作能力强', 1), ('创造性思维能力强', 1), ('实践创新和解决问题的能力强', 2),
     ('创新成果：全国XX比赛一等奖（1/4）', 3)],
    [('领导能力强', 1), ('协作能力强', 1), ('创造性思维能力强', 1), ('实践创新和解决问题的能力强', 2),
     ('创新成果：全国XX比赛一等奖（1/4）', 3)],
    [('领导能力强', 1), ('协作能力强', 1), ('创造性思维能力强', 1), ('实践创新和解决问题的能力强', 2),
     ('创新成果：全国XX比赛一等奖（1/4）', 3)]
]


# 主程序
def main():
    background_img = plt.imread("./assets/background.jpg")
    plt.imshow(background_img, alpha=1)  # 显示背景图, alpha参数表示透明度

    # 对图0-5的不同矩形图片进行遍历
    for i in range(6):
        print("The {}.jpg is processing.".format(i))

        # 获得要显示的文字
        whole_text_list = []
        for t in texts[i]:  # 对第i个数组进行循环，t是数组的每个元组
            for j in range(t[1]):  # 对元组的第2位，即频数进行循环，出现多少次就循环显示多少次
                whole_text_list.append(t[0])  # 加到文字列表中
        whole_text = " ".join(whole_text_list)  # 以空格分割形成一整段文字

        # 得到要显示的词云
        img = plt.imread("./assets/{}.jpg".format(i))  # 获得遮罩图路径
        wc = WordCloud(
            background_color="rgba(255,255,255,0)",  # 设置背景颜色为透明
            mode="RGBA",  # 设置模式为rgba模式，带透明色
            mask=img,  # 设置遮罩的图片
            width=800,
            height=800,
            font_path="./assets/msyh.ttc",  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
            max_words=200,  # 设置最大显示的字数
            max_font_size=80,  # 设置字体最大值
            random_state=30  # 设置有多少种随机生成状态，即有多少种配色方案
        )
        wordcloud_img = wc.generate(whole_text)
        plt.imshow(wordcloud_img)

    # 保存图片
    plt.axis("off")  # 去掉坐标轴显示
    plt.savefig('./词云图.png', dpi=600)  # 保存图片


if __name__ == "__main__":
    main()
