# 1. 项目开发基础概念
## 1.1 企业的web项目类型
1. 商城
	- B2C 直销商城，上家与会员直接交易（Business To Customer）
	- B2B 批发商城 商家与上家直接交易
	- B2B2C 商家和会员在另一个商家提供的平台上进行交易
	- C2B 定制商城 会员像上家发起定制商品的需求 商家去完成
	- O2O 线下线上交易平台
	- C2C 二手交易平台
2. 门户网站企业占和门户站
3. 社交网站
4. 咨询论坛
5. 内部系统
6. 个人博客
7. 内容收费站

## 1.2 企业项目开发流程

![5d576de73448e23333b541c73469e532.png](:/6c748abcfcd944eebf2077c92755e336)
![625c56ee197767b4b2e5d9130019600d.png](:/e7b10a2b2805463bbad715307fe02122)

原型设计网
https://www.axure.com.cn/resource

## 1.3立项申请阶段
立项就是对产品项目进行评估 究竟能不能做 提出理论基础，大的互联网项目都有比较正规的立项流程
![e2c4efc342c825e415f7397950c06f2c.png](:/e61f9b58000f4ca1b120cbcc0137f9cf)

通常公司内部要研发一款软硬件的产品之前。都要经过市场评估，产生一份 产品立项报告给公司
产品立项报告一般包含以下内容	
```text
项目概述
需求市场
需求分析和项目建设的必要性
业务分析
总体建设方案
项目风险和风险管理
可行性分析阶段
```

# 2. 需求分析
## 2.1. 首页
功能： 导航栏，轮播图， 退出登录
![076611107153addb31337a39940bf173.png](:/4cb52196e78a4bfb94cf772b5f9e488d)

## 2.2. 登录注册
功能：用户登录，极验验证码，多条件登录，记住密码，短信发送，短信冷却倒计时，jwd认证
![7d6e1346dcaeeebe7d614470f5767eb8.png](:/3ce670e4b76c492293366800ee17e57e)

## 2.3 课程列表
功能： 课程分类，课程列表，课程多条件筛选展示，课程分类展示，课程分页展示，课程章节课时展示，课程优惠策略



## 2.4 课程详情
功能：课程信息展示，视频播放，富文本编译器

## 2.5 购物车
功能： 购物车商品列表，添加商品，删除商品，勾选商品状态，商品结算，订单生成，唯一订单生成

## 2.6 商品结算
功能： 订单信息商品列表，订单信息展示，积分功能计算，优惠券策略，课程有效计算，第三方支付平台接口	

## 2.7 购买成功

## 2.8 个人中心
功能列表：我的订单，订单状态改变

## 2.9 视频播放
功能： 视频加密播放


# 3. 环境搭建
## 创建虚拟环境
- anaconda 
- mkvirtualenv
- python -m venv venv

三种方法任选其一

## 相关命令
见博客
项目开发完毕运行
`pip freeze >> requirements.txt`

记得 写好版本号和说明

## 技术选型

外部依赖
1. 注册支付宝开发账号
2. 注册服务器和域名
3. 注册容联云短信接口平台的账号
4. 注册保利威视频服务平台的账号

```
pip install django
pip install djangorestframework
pip install Pymysql
pip install Pillow
pip install django-redis
```
