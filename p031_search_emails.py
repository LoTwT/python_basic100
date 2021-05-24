# 提取邮箱地址
import re

content = """
　　电子邮件地址怎么写问题，电子邮箱格式通常以类似guangjia@mail.com出现，
    前面的guangjia为您注册时的用户名，http://mail#com 为注册电子邮箱的域名，
    该域名后缀由电子邮箱注册网站的域名，假如在新浪注册电子邮箱，
    那么@后面的地址应该为 sdfas@sinacomcn，假如在网易163注册电子邮箱，
    就应该为 sdf_sdf-ffds@163.net，@为电子邮箱分隔符，根据国际惯例@符号为典型的电子邮箱地址格式分隔符，
    在@之前为电子邮箱的用户名，在@之后为电子邮箱的服务器域名地址(与邮箱注册网站的地址一致) ;
"""

pattern = re.compile(
    r"""
    [a-zA-Z0-9_-]+
    @
    [a-zA-Z0-9]+
    \.
    [a-zA-Z]{2,4}
    """,
    re.VERBOSE
)

results = pattern.findall(content)

for result in results:
    print(result)
