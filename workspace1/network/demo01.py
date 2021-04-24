'''
1.2 打印设备名和 IPv4 地址
有时，你需要快速查看设备的某些信息，例如主机名、IP地址和网络接口的数量等。这些信
息使用Python脚本很容易获取。
'''

import socket

# 获取本机名
host_name = socket.gethostname()
print('host_name=%s'%host_name)

# 获取host_name对应的ip,
ip = socket.gethostbyname(host_name)
print('ip=%s'%ip)

# 获取远端设备ip地址
host_name = 'www.baidu.com'
ip = socket.gethostbyname(host_name)
print('ip=%s'%ip)
