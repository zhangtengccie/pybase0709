import hashlib
import re
from ssh_router import ssh_cli
import time



def qytang_get_config(ip,username='cisco',password='cisco'):
    try:
        device_config_raw = ssh_cli(ip,username,password,cmd='show run')
        split_result = re.split(r'\r\nhostname \S+\r\n',device_config_raw)
        device_config = device_config_raw.replace(split_result[0], '').strip()
        return device_config
    except Exception:
        return
def qytang_check_diff(ip,username='cisco',password='cisco'):
    before_md5 = ''
    while True:
        device_config = qytang_get_config(ip,username,password)
        m = hashlib.md5()
        m.update(device_config.encode())
        md5_value = m.hexdigest()
        print(md5_value)
        if not before_md5:
            before_md5 = md5_value
        elif before_md5 != md5_value:
            print('MD5 value changed')
            break
        time.sleep(5)




if __name__ == '__main__':
    # print(qytang_get_config('1.1.1.200',username='cisco',password='cisco'))
    qytang_check_diff('1.1.1.200',username='cisco',password='cisco')