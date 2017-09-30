# Ownnet DDNS NSServer(Python3版本)
## 简介
## 安装
### Python3及Pip安装
#### Windows：
请前往[python](https://www.python.org/downloads/)官网下载  
pip安装：https://pip.pypa.io/en/stable/installing/
#### Debian：
debian下推荐使用包管理器  
`sudo apt-get install python3 python3-pip`
#### CentOS：
使用包管理器
RH系列操作系统需要安装epel仓库   
```
sudo yum install epel-release
sudo yum update
sudo yum install python34 python34-pip
```

随着centos版本的升级，包管理器中python3的版本有可能发生改变，建议在安装前使用`yum search python3`根据输出判断仓库中python3的版本

其他方案：https://stackoverflow.com/questions/32618686/how-to-install-pip-in-centos-7
#### OSX：
请前往[Python Release for Mac OS X](https://www.python.org/downloads/mac-osx/)下载  
pip安装https://pip.pypa.io/en/stable/installing/  


### 下载源码
git clone或http方式下载并解压本仓库  

### 程序安装
1. 进入根目录，以root身份执行`pip3 install -r requirements.txt`  
备注:普通用户身份安装dnslib库时可能会报错
2. 将main.bak.db重命名为main.db 
3. 如果有需要，可安装redis或memchace作为查询缓存，缓存启用请修改conf.py中CACHE_TYPE字段及服务器连接信息
4. 默认使用sqlite数据库。mysql同样支持，但并未测试。如需使用，可手动导出sqlite数据库并导入mysql。

### 修改配置  
配置文件位于conf.py中，请按需修改数据库位置，监听的ip及端口以及DNS ZONE信息

### 运行
在程序根目录以root用户（或其它有监听熟知端口权限的用户）执行  
`python3 server.py`


可在screen中运行或使用nohup运行；在windows下运行时请保持命令行窗口开启

### 测试
`dig @localhost your.domain.com A`

### 简易使用说明：
1. 自用时，若不想部署前端，可自行手动修改数据库中record表
2. 泛解析支持：若存在*.abc.com记录，则对域名abc.com进行泛解析
3. 如需部署前端，可使用ownnet/ddns_webserver。管理员账户密码默认均为admin，请尽快修改。

### 动态DNS使用方法
见ownnet/ddns仓库中文档：01
