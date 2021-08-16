import sys
import io
import requests
import base64
# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
#输入账号密码
username = ' '#学号
password = ' '#默认密码123456
username1 = base64.encodebytes(username.encode('utf8'))
password1 = base64.encodebytes(password.encode('utf8'))
# 个人信息上报需要的data数据
data2 = {
    #需要修改定位信息
    #需要修改定位信息
    #需要修改定位信息
    'data': '{"xmqkb":{"id":"40288073707f4e940170847957440000"},"c1":"36.9℃以下","c2":"正常","c8":"否","c35":"否","c36":"否","c37":"否","c38":"否","c39":"否","c40":"否","c41":"否","type":"yqsjcj","location_longitude":117.727625,"location_latitude":39.043617,"location_address":"天津市 滨海新区 信环西路 19号 靠近天河国家超级计算天津中心 "}',
    'msgUrl': 'syt/zzapply/list.htm?type=yqsjcj&xmid=40288073707f4e940170847957440000',
    'uploadFileStr': '{}',
    'multiSelectData': '{}'
}
# 创建session维持会话
mysession = requests.Session()
# 配置url地址
url0 = "http://xuegong.tsc.edu.cn//login/Login.htm"  # 提交登录表单
url1 = "http://xuegong.tsc.edu.cn/user/index.htm"  # 检查登录状态
url2 = "http://xuegong.tsc.edu.cn/syt/zzapply/operation.htm"  # 个人信息上报
url3 = "http://xuegong.tsc.edu.cn/syt/yiban/position/operation.htm"  # 位置签到
# 初始化url请求对象
r = requests.get(url1)
# 获取url请求对象中的有用信息，如token、cookies
JSESSOONID = r.cookies.items()[0][1]
token = r.cookies.items()[1][1]
cookies = r.cookies
session = requests.Session()
# 登录时需要POST的数据
data1 = {'username': username1,
         'password': password1,
         'token': token}
# 设置请求头
headers = {"Host": "xuegong.tsc.edu.cn",
           "Cookies": 'username=4183213233; menuVisible=0; JSESSIONID=' + JSESSOONID
           }
# 登录
s = mysession.post(url0, data1, headers)
ss = mysession.get(url1)
# 个人信息上报
xx = mysession.post(url2, data2, headers)
print('个人信息上报：' + xx.text)
#推送企业微信应用通知
#填写自己的
datatz = {"corpid": " ",
          "corpsecret": " ",
          "agentid": " ",
          "title": "xx今日健康打卡",
          "description": s.text + '\n' + '个人信息上报：' + xx.text + '\n',
          "url": "xuegong.tsc.edu.cn"
         }
#补充完整解开下面一行注释
#requests.post('https://api.htm.fun/api/Wechat/text_card/',datatz)