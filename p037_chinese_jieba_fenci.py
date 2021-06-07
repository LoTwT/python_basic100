# 中文文章分词
import jieba
import re

content = '''
    我一直想看一场日落。
    或许是因为诗人王维的那句：“大漠孤烟直，长河落日圆”让我看见了落日的金色余晖和那份诗人的离愁。
    又或许是因为那句描写滕王阁的千载名句：“落霞与孤骛齐飞，秋水共长天一色”让我目睹了日落时水天一色的祥和美景。
　　就在这天放学回家的路上，我路过了一片河堤。
    金色的夕阳打柳叶中穿过将整个河岸都映成了浪漫的橙红色，放眼望去，满目的水波在夕阳温柔的亲吻下闪烁着柔和的光芒。
    再把目光抬高放远，有零星的渔船在河水中缓缓而行，身后荡漾的水波化成圆弧散开，彻底融化进了无尽的晚霞。
    我屏住呼吸，静静观赏着太阳姑娘的完美谢幕，河对岸的小白房子已经升起了袅袅炊烟，天色完全暗了下来。
　　真美啊!回家后我不由得跟妈妈感慨起夕阳的美丽，同时我也明白了其实夕阳除了意味着一天的结束，同时也代表着另一天即将开始，关键在于我们要有一颗满怀希望的内心。
'''
content = re.sub(r"[\s。，、“”：]", "", content)

word_list = jieba.cut(content)

print(list(word_list))
