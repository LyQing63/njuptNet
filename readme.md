# 南京邮电大学校园网自动登录

🚀🚀🚀

**by 灵檠**

## 项目介绍

由于连接校园网需要使用浏览器登录，十分麻烦，因此有了使用脚本开机自动登录校园网的想法。

## 项目实现

- 采用 python 向校园网后台直接发送登录请求，从而实现校园网登录功能
- 采用脚本程序实现配置开机自动启动，自动配置开机启动项
- 采用 yaml 的数据格式，用来配置登录信息

## 项目目标

- [x] 实现 WAN 口校园网自动登录
- [x] 实现 Windows 系统自动配置开机启动项功能
- [ ] 实现 WIFI 校园网自动登录功能
- [ ] 实现 WAN 口与 WIFI 连接检测
- [ ] 实现 MacOS 与 Linux 系统的自动登录
- [ ] 实现日志记录功能
- [ ] 对于请求的各种状态码的判断，并记录对应的信息
- [ ] 对于是否接入校园网的检测
