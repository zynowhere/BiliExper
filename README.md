<div align="center"> 

</div>


</br>[转至目录快速使用](#目录)

## 主要功能
**一、B站自动操作脚本BiliExp.py**

* [x] 每日获取经验(投币(支持自定义up主)、点赞、分享视频) 
* [x] 自动转发互动抽奖并评论点赞(官抽，非官抽支持指定关键字如"#互动抽奖#",支持跟踪转发模式)(Actions上默认1天执行1次，1次转发过去1天的动态，云函数上每次只转发过去10分钟的动态，建议修改为每10分钟执行1次)
* [x] 获取主站@和私聊消息提醒(便于多账号抽奖时获取中奖信息)
* [x] 参与官方转盘抽奖活动(目前没有自动搜集活动的功能,需要在配置文件config/activities.json里面手动指定,本项目***discussions***下会更新比较新的转盘抽奖活动)
* [x] 每日直播签到
* [x] 直播挂机(获取小心心,点亮粉丝牌，云函数默认关闭此功能，Actions上默认每次每个粉丝牌房间分别挂机45分钟)
* [x] 直播自动送出快过期礼物(默认送出两天内过期的礼物)
* [x] 直播天选时刻抽奖 (支持条件过滤，云函数默认搜索1次后立即退出，Actions上默认执行45分钟后退出，云函数上建议10分钟执行1次)
* [x] 直播应援团每日签到 
* [ ] ~~直播开启宝箱领取银瓜子(本活动已结束，不知道B站以后会不会再启动)~~ 
* [x] 每日兑换银瓜子为硬币 
* [x] 自动领取大会员每月权益(每月1号领取B币劵，优惠券)
* [x] 自动花费大会员剩余B币劵(每月28号执行，支持给自己充电或者兑换成金瓜子)
* [x] 漫画APP每日签到
* [x] 自动花费即将过期漫读劵(默认不开启)
* [x] 自动积分兑换漫画福利券(需中午12点启动，默认不开启)
* [x] 自动领取大会员漫画每月福利劵
* [ ] ~~自动参加每月"站友日"活动(本活动已结束，不知道B站以后会不会再启动)~~
* [x] 定时清理无效动态(转发的过期抽奖，失效动态，支持自定义关键字，非官方渠道抽奖无法判断是否过期，默认不开启本功能) 
* [x] 风纪委员投票(云函数默认没有案件立即退出，Actions默认45分钟内没有案件自动退出，云函数上建议每20分钟运行1次)

***默认所有任务每天只执行1次***，但建议***云函数***上***风纪投票***，***抽奖转发***，***天选时刻***等任务每天***多次***执行，***Actions***上***风纪投票***，***天选时刻***，***直播挂机(领小心心)***等任务可以***设置更长的超时时间***(默认45分钟后退出)。
</br>使用这些功能可以参考一下[部分功能推荐配置](https://github.com/happy888888/BiliExp/issues/178)

</br>[转至目录快速使用](#目录)
</br>

**二、脚本up主系列**
* python实现B站专栏的编写，排版和发表
* python实现B站视频稿件的上传和发布
* python实现B站音频(lrc歌词)稿件(单曲和合辑)的上传和发布
</br>(例子和教程请参考[专栏、视频和音频的发表(面向开发者)](/机器人up主#python实现B站发布专栏视频和音频的方法)

</br>[命令行视频投稿工具](#使用说明视频投稿部分)

**三、B站漫画下载mangaDownloader.py**支持合并为单个pdf文件,允许使用账号cookie下载已解锁部分
* [x] 支持使用账号cookie下载已解锁部分
* [x] 合并为单个pdf文件
</br>[快速使用](#使用方式下载器部分)
</br>

**四、B站视频下载videoDownloader.py**
* [x] 支持使用账号cookie下载大会员视频
* [x] 支持下载港澳台番剧(内置一个反向代理接口，接口源码见"player_proxy"文件夹，支持阿里/腾讯云函数部署此接口)
* [x] 支持下载弹幕(转成ass字幕文件,需要用支持ass字幕的播放器打开,目前只支持滚动弹幕和顶部/底部弹幕,不支持高级弹幕)
</br>[快速使用](#使用方式下载器部分)
</br>

# 目录

- [项目说明](#项目说明)
  - [主要功能](#主要功能)
- [目录](#目录)
- [使用说明(仅自动操作脚本部分)](#使用方式仅自动操作脚本部分)
  - [零、部分功能推荐配置](https://github.com/happy888888/BiliExp/issues/178)
  - [一、使用腾讯云函数(Actions部署)](#方式二使用腾讯云函数)
  - [二、使用阿里云函数(Actions部署)(不推荐)](#方式三不推荐使用阿里云函数)
  - [三、windows本地部署(依靠任务计划启动)](#方式四windows本地部署)
  - [四、linux本地部署(依靠crontab启动,shell自动下载安装)](#方式五linux本地部署)
  - [五、docker部署](#方式六docker安装)
  - [六、openwrt等路由器部署](#方式七openwrt等路由器部署)
- [使用说明(下载器部分)](#使用方式下载器部分)
- [使用说明(视频投稿部分)](#使用说明视频投稿部分)
- [使用说明(专栏、视频和音频的发表,面向开发者)](/机器人up主#python实现B站发布专栏视频和音频的方法)
- [更新日志](#更新日志)
- [欢迎打赏](#打赏)
- [获得B站账户cookies方法](#获得cookies方法)
- [一些实用的B站PC浏览器辅助小脚本](/browser_assist#这里是一些用于b站的浏览器辅助脚本)
  - [使用方式(仅适用pc浏览器)](/browser_assist#使用方式)
  - [脚本](/browser_assist#脚本列表)
    - [过期抽奖动态删除(目前已集成到自动操作脚本)](/browser_assist#所有过期抽奖动态删除)
    - [破解专栏不可复制](/browser_assist#b站专栏不可复制破解)
    - [删除关注up主](/browser_assist#删除关注的up主慎用)
    - [删除互粉粉丝](/browser_assist#删除互粉的粉丝慎用)
    - [关注话题页面up主(抽奖话题)](/browser_assist#关注话题页面up主主要是抽奖话题)
    - [b站自动新人答题](/browser_assist#b站自动答题非原创未测试)
</br>

## 使用方式(仅自动操作脚本部分)

***详细配置文件在/config/config.json，云函数部署后在/src/config/config.json，Actions上应使用secrets，如不修改则使用默认配置***

### 方式一、使用腾讯云函数

* 1.准备
* 1.1开通云函数 SCF 的腾讯云账号，在[访问秘钥页面](https://console.cloud.tencent.com/cam/capi)获取账号的 TENCENT_SECRET_ID，TENCENT_SECRET_KEY
> 注意！为了确保权限足够，获取这两个参数时不要使用子账户！此外，腾讯云账户需要[实名认证](https://console.cloud.tencent.com/developer/auth)。
* 1.2依次登录 [SCF 云函数控制台](https://console.cloud.tencent.com/scf) 和 [SLS 控制台](https://console.cloud.tencent.com/sls) 开通相关服务，确保您已开通服务并创建相应[服务角色](https://console.cloud.tencent.com/cam/role) **SCF_QcsRole、SLS_QcsRole**
* 1.3一个或多个B站账号，以及登录后获取的SESSDATA，bili_jct，DedeUserID ([获得B站账户cookies方法](#获得cookies方法))
* 1.4fork本项目
* 2.部署
*  2.1 在fork后的github仓库的 “Settings” --》“Secrets” 中添加"Secrets"，name和value分别为：
    *  2.1.1 name为"TENCENT_SECRET_ID"           value为腾讯云用户SecretID(需要主账户，子账户可能没权限)
    *  2.1.2 name为"TENCENT_SECRET_KEY"          value为腾讯云账户SecretKey
		![image](https://user-images.githubusercontent.com/67217225/96539780-7aef5400-12ce-11eb-9af6-696286a44885.png)
		注意图片上的***BILICONFIG***仅供Actions使用，***云函数仍需要部署后在云函数控制台中/config/config.json文件中手动填入账号cookie***
*  2.2 添加完上面 2个"Secrets"后，进入"Actions"(上面那个不是Secrets下面那个) --》"deploy for serverless"，点击右边的"Run workflow"即可部署至腾讯云函数(如果出错请在红叉右边点击"deploy for serverless"查看部署任务的输出信息找出错误原因)
    *  2.2.1 首次fork可能要去actions里面同意使用actions条款，如果"Actions"里面没有"deploy for serverless"，点一下右上角的"star"，"deploy for serverless"就会出现在"Actions"里面
    *  2.2.2 部署完成后一定要去云函数控制台将账号cookie填写到/config/config.json文件中

### 方式二(不推荐)、使用阿里云函数

目前有发现在Actions内无法ping通阿里云函数的域名，部署可能出现超时现象

* 1.准备
    *  这里直接参考[腾讯云函数部署步骤](#方式二使用腾讯云函数)

* 2.部署
    *  2.1在fork后的github仓库的 “Settings” --》“Secrets” 中添加"Secrets"，name和value分别为：
        *  2.1.1 name为"ACCOUNT_ID"           value为阿里云用户的账号ID
        *  2.1.2 name为"ACCESS_KEY_ID"        value为阿里云账户AccessKeyID(需要主账户，子账户可能没权限)
        *  2.1.3 name为"ACCESS_KEY_SECRET"    value为阿里云账户accessKeySecret
		![image](https://user-images.githubusercontent.com/67217225/96539780-7aef5400-12ce-11eb-9af6-696286a44885.png)
    *  2.2这里直接参考[腾讯云函数部署步骤](#方式二使用腾讯云函数)中的2.2步骤

### 方式三、windows本地部署

* 1.准备
    *  1.1一个或多个B站账号，以及登录后获取的SESSDATA，bili_jct，DedeUserID ([获得B站账户cookies方法](#获得cookies方法))
    *  1.2进入右边的[release](https://github.com/happy888888/BiliExp/releases) ,下载BiliExp-win32_64开头的压缩包

* 2.部署
    *  2.1解压步骤1.2下载的压缩包，并放置到合适位置(比如E:\Program Files)
    *  2.2进入解压后产生的config文件夹，配置config.json文件(包含功能的启用和账号cookie的配置)
    *  2.3退出config文件夹返回上层，运行setup_for_windows.bat文件(需要管理员权限)，按照提示即可完成安装。脚本将会在每天12:00启动(依赖于计划任务)。

***如果电脑上已经安装python3环境，比起使用release版本，更推荐直接下载代码到本地运行，因为release版本可能是老旧的版本***
	
### 方式五、linux本地部署

* 1.准备
    *  1.1一个或多个B站账号，以及登录后获取的SESSDATA，bili_jct，DedeUserID ([获得B站账户cookies方法](#获得cookies方法))

* 2.部署
    *  2.1执行如下命令，并按照提示安装
	      ```
		  wget https://glare.now.sh/happy888888/BiliExp/BiliExp-Linux-64 && mv BiliExp-Linux-64* BiliExp.tar && tar xvf BiliExp.tar && cd BiliExp && sudo chmod 755 setup_for_linux.sh && sudo ./setup_for_linux.sh
		  ```
    *  2.2安装成功后，可去/etc/BiliExp/config.json文件中进行详细配置，脚本将会在每天12:00启动(依赖于crontab)。

***如果服务器上已经安装python3环境，比起使用release版本，更推荐直接clone代码到本地运行，因为release版本可能是老旧的版本***

### 方式六、docker安装

[docker hub地址](https://registry.hub.docker.com/repository/docker/happy888888/biliexp) 

* 1.准备
    *  1.1一个或多个B站账号，以及登录后获取的SESSDATA，bili_jct，DedeUserID (获取方式见最下方示意图),可选：SCKEY，email用于微信或邮箱的消息推送
    *  1.2安装docker(以安装可忽略) `curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun`

* 2.部署
    *  2.1填写本项目下config/config.json文件，放到本地任意文件夹下(以路径 '/home/user/Biliexp' 为例)
    *  2.2执行如下命令，运行BiliExp
	      ```
		  docker run \
		  -v /home/user/Biliexp:/BiliExp \
		  happy888888/biliexp:runner-latest 
		  ```
    *  2.3其他参数
	      ```
		  docker run \
		  -v /home/user/Biliexp:/BiliExp \
		  happy888888/biliexp:runner-latest \
		  -t <tag> \
		  -d \
		  -c <cron>
		  ```
		  `<tag>`表示版本号,可以使用`latest`(不指定时默认,表示最新版),`newest`(表示拉取最新主分支代码执行),指定版本号例如`1.1.0`,当指定版本号时代码会缓存到挂载的路径(上面的例子是主机的`/home/user/Biliexp/code-cache`目录),不指定版本号为每次拉取github代码<br>
		  `-d`指定本参数时容器不会退出，而是在每天中午12:00执行代码<br>
		  `<cron>`表示cron表达式,指定后会按照指定表达式的时间执行，默认为`0 12 * * *`即每天中午12点执行,此项参数在不指定`-d`时无效<br>
		  
		  例子,每天8点执行BiliExp 1.1.0版本<br>
	      ```
		  docker run -d -v /home/user/Biliexp:/BiliExp happy888888/biliexp:runner-latest -t 1.1.0 -d -c "0 8 * * *"
		  ```
* 3.支持平台
    |  平台   | tag标签  |
    |  ----  | ----  |
    | windows/linux(x64)  | runner-latest |
    | linux(arm32)  | runner-arm-latest |
    | linux(arm64)  | runner-arm64-latest |
	
* 4.注意事项
    *  4.1docker镜像中不包含本项目代码，docker启动时会自动下载
    *  4.2下载代码的版本号由参数`-t`指定，只有指定`-t 版本号`时才会缓存代码下次使用，`-t latest`和`-t newest`均为每次下载代码
    *  4.3缓存代码后每次只会执行缓存的代码,要更新版本必须删除缓存才会重新下载新代码(指定了`-t latest`(默认)和`-t newest`除外)
    *  4.4日志也存放在挂载目录中，且增量保存，可以定时清理
	
* 5.其他docker版本
除了不带代码的`runner`版本，也有携带代码的`happy888888/biliexp:latest`,`happy888888/biliexp:arm64-latest`版本docker镜像可以使用，这些版本执行后会立即退出不能指定参数常驻后台

### 方式七、openwrt等路由器部署

***此方式难度较大，如果能用其他方式请尽量使用其他方式***

* 1.准备
    *  1.1一个或多个B站账号，以及登录后获取的SESSDATA，bili_jct，DedeUserID (获取方式见最下方示意图),可选：SCKEY，email用于微信或邮箱的消息推送
    *  1.2使用xshell等工具,登录openwrt(padavan等)路由器，使用命令安装python3
	   ```
	   opkg update
	   opkg install python3-light
	   ```
    *  1.3安装python `aiohttp`库
	   `aiohttp`库在`openwrt`(`padavan`)等路由器的opkg软件源上并没有直接的安装包，需要自己下载项目源码在openwrt平台上构建<br>
	   如果你的路由器架构是`mipsel`，可以下载我编译好的依赖库(与本项目代码一起打包),[BiliExp_with_aiohttp-mipsel.zip](https://github.com/happy888888/BiliExp/files/5673033/BiliExp.zip)

* 2.部署
    *  2.1下载本项目代码(步骤1.3压缩包包含代码),解压,填写config/config.json文件
    *  2.2通过`xftp`(`WinScp`)等软件把解压的文件夹上传到路由器内(比如路径为/root/BiliExp)
    *  2.3设置crontab使代码定时启动
	   使用xshell等工具,登录openwrt(padavan等)路由器，输入命令
	   ```
	   echo "0 12 * * * /usr/bin/python3 /root/BiliExp/BiliExp.py -c /root/BiliExp/config/config.json" >> "/etc/crontabs/root"
	   ```
	   也可以在路由器网页上寻找类似***计划任务***的功能,在默认添加一行`0 12 * * * /usr/bin/python3 /root/BiliExp/BiliExp.py -c /root/BiliExp/config/config.json`并保存
	   ![image](https://user-images.githubusercontent.com/67217225/101779806-b10fbe00-3b30-11eb-987b-f4b88ee3fa16.png)
	   
* 3.注意事项
    *  3.1在步骤1.3中我提供的依赖库只有"mipse"架构的路由器能使用,其他架构的路由器只能自行编译"aiohttp"库并安装
    *  3.2本项目依赖的库较大，不能外接U盘的路由器最好不要使用
	   
</br></br></br>

## 使用方式(下载器部分)

* 1.转至[release](https://github.com/happy888888/BiliExp/releases) ，下载BiliDownloader，解压。
* 2.从浏览器获取SESSDATA，bili_jct，DedeUserID这三个参数 ([获得B站账户cookies方法](#获得cookies方法))
* 3.将上述获取的三个参数填入config文件夹中的config.json文件(linux可将文件放入/etc/BiliExp/config.json)
* 4.使用videoDownloader
    ```
	命令行参数
	videoDownloader -a -p <下载文件夹> -v <视频1> -e <分集数> -q <质量序号> -v <视频2> -e <分集数> -q <质量序号> ...
	-a --ass       下载视频时附带ass文件,配合支持ass字幕的播放器可以显示弹幕
	-p --path      下载保存的路径，提供一个文件夹路径，没有会自动创建文件夹，默认为当前文件夹
	-v --video     下载的视频地址，支持链接，av号(avxxxxx)，BV号(BVxxxxxx)，ep，ss
	-e --episode   分p数，只对多P视频和多集的番剧有效，不提供默认为1，多个用逗号分隔，连续用减号分隔  -e 2,3,5-7,10 表示2,3,5,6,7,10集
	-q --quality   视频质量序号，0为能获取的最高质量(默认)，1为次高质量，数字越大质量越低
	-x --proxy     是否使用接口代理(可下载仅港澳台)，0为不使用(默认)，1为使用代理
	注意，一个 -v 参数对应一个 -e(-q, -x) 参数，如果出现两个 -v 参数但只有一个 -e(-q, -x) 参数则只应用于第一个，可以有多个 -v 参数以一次性下载多个视频
	-V --version   显示版本信息
	-h --help      显示帮助信息
	
	使用例子
	windows上(假如文件在D:\bilidownloader\videoDownloader.exe)，下载BV1qt411x7yQ的1,2,3,6集到D:\download目录
	打开cmd执行如下命令
	cd /d D:\bilidownloader
	videoDownloader -v BV1qt411x7yQ -e 1-3,6 -p D:\download
	
	linux上(提前将videoDownloader移动到/usr/local/bin)，下载BV1qt411x7yQ的1,2,3,6集到用户的download目录
	shell中执行
	videoDownloader -v BV1qt411x7yQ -e 1-3,6 -p ~/download
	```
* 5.使用mangaDownloader
    ```
	命令行参数
	mangaDownloader -p <下载文件夹> -m <漫画> -e <章节数> -f
	-p --path      下载保存的路径，提供一个文件夹路径，没有会自动创建文件夹，默认为当前文件夹
	-m --manga     下载的漫画mc号，整数
	-e --episode   章节数，不提供默认下载所有章节，多个用逗号分隔，连续用减号分隔  -e 2,3,5-7,10 表示2,3,5,6,7,10章节，注意番外也算一个章节
	-f --pdf       下载后合并为一个pdf
	-V --version   显示版本信息
	-h --help      显示帮助信息
	
	使用例子
	windows上(假如文件在D:\bilidownloader\mangaDownloader.exe)，下载漫画mc28565的3,9,12,13,14章到D:\download目录
	打开cmd执行如下命令
	cd /d D:\bilidownloader
	mangaDownloader -m 28565 -e 3,9,12-14 -p D:\download
	
	linux上(提前将mangaDownloader移动到/usr/local/bin)，下载漫画mc28565的3,9,12,13,14章到用户的download目录
	shell中执行
	mangaDownloader -m 28565 -e 3,9,12-14 -p ~/download
	```

</br></br></br>

## 使用说明(视频投稿部分)
* 1.转至[release](https://github.com/happy888888/BiliExp/releases) ，下载videoUploader，解压。
* 2.从浏览器获取SESSDATA，bili_jct，DedeUserID这三个参数 ([获得B站账户cookies方法](#获得cookies方法))
* 3.将上述获取的三个参数填入config文件夹中的config.json文件(linux可将文件放入/etc/BiliExp/config.json)
* 4.使用videoUploader
    ```
	命令行参数
	VideoUploader -v <视频文件路径> -t <视频标题> -d <视频简介> -c <视频封面图片路径> -t <视频标签> -n -s <非原创时视频来源 网址>
	-v --videopath     视频文件路径
	-t --title         视频标题，不指定默认为视频文件名
	-d --desc          视频简介，不指定默认为空
	-c --cover         视频封面图片路径，不提供默认用官方提供的第一张图片
	-i --tid           分区id，默认为174，即生活,其他分区
	-T --tags          视频标签，多个标签用半角逗号隔开，带空格必须打引号，不提供默认用官方推荐的前两个标签
	-n --nonOriginal   勾选转载，不指定本项默认为原创
	-s --source        -n参数存在时指定转载源视频网址
	-D --DelayTime     发布时间戳,10位整数,官方的延迟发布,时间戳距离现在必须大于4小时
	-S --singleThread  单线程上传,如果出现上传失败时使用,不指定本项为3线程上传
	-V --version       显示版本信息
	-h --help          显示帮助信息
	以上参数中只有-v --videopath为必选参数，其他均为可选参数
	
	使用例子
	windows上(假如程序在D:\VideoUploader\VideoUploader.exe,视频在D:\VideoUploader\测试视频.mp4)
	打开cmd执行如下命令
	cd /d D:\VideoUploader
	VideoUploader -v "D:\VideoUploader\测试视频.mp4"
	
	linux上(提前将VideoUploader移动到/usr/local/bin,视频文件在/root/upload/测试视频.mp4)
	shell中执行
	VideoUploader -v "/root/upload/测试视频.mp4"
	```

</br></br></br>

