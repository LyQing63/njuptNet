import requests
import json
import re
import yaml
import socket
 
def get_local_ip():
    ip = socket.gethostbyname(socket.getfqdn())
    return ip  

def request_data(url): 
    req = requests.get(url, timeout=30) # 请求连接
    jsonp_str = req.content.decode('utf-8')
    json_str = json.loads(re.match(".*?({.*}).*", jsonp_str, re.S).group(1))
    return json_str

account = ''
password = ''
IP = get_local_ip()
login_method = ''

def isLogin():
    res = request_data(ISLOGIN_URL)
    code = res.get('result')
    msg = res.get('msg')
    if (code == 1):
        print(msg)
        return True
    return False

def login():
    if (isLogin()):
        return
    res = request_data(LOGIN_URL)
    code = res.get('result')
    msg = res.get('msg')
    if (code == 1):
        print('login successful!')
    elif(code == 0):
        print('already login.')
    print(msg)

def logout():
    if (not isLogin()):
        return
    res = request_data(LOGOUT_URL)
    code = res.get('result')
    msg = res.get('msg')
    if (code == 1):
        print('logout successful!')
    elif(code == 0):
        print('already logout.')
    print(msg)

if __name__== "__main__" :
    # 从文件中读取YAML配置
    with open('config.yaml', 'r') as file:
        config = yaml.load(file, Loader=yaml.CLoader)
        account = config.get('user').get('account')
        password = config.get('user').get('password')
        login_method = config.get('proxy')
    
    LOGIN_URL = f'https://p.njupt.edu.cn:802/eportal/portal/login?login_method=1&user_account=%2C0%2C{account}%40{login_method}&user_password={password}&wlan_user_ip={IP}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=7241&lang=zh'
    ISLOGIN_URL = f'https://p.njupt.edu.cn:802/eportal/portal/online_list?user_account=&user_password=&wlan_user_mac=000000000000&wlan_user_ip={IP}&curr_user_ip={IP}&jsVersion=4.X&v=6900&lang=zh'
    LOGOUT_URL = f'https://p.njupt.edu.cn:802/eportal/portal/logout?login_method=1&user_account=drcom&user_password=123&ac_logout=1&register_mode=1&wlan_user_ip={IP}&wlan_user_ipv6=&wlan_vlan_id=0&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&v=791&lang=zh'

    login()
