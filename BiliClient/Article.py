
__all__ = (
    'Article',
)

from . import bili

class Article(object):
    "B站专栏类,用于发表B站专栏"
    createArticle = bili.createArticle
    deleteArticle = bili.deleteArticle
    getArticle = bili.getArticle
    articleUpcover = bili.articleUpcover
    articleCreateVote = bili.articleCreateVote
    articleCardsBvid = bili.articleCardsBvid
    articleCardsCvid = bili.articleCardsCvid
    articleMangas = bili.articleMangas

    #本类只继承bili中与Article有关的方法
    class Content(object):
        "文本类用来处理B站奇葩的专栏提交格式"
        def __init__(self):
            self._content = ""
        def add(self, text):
            "添加内容"
            self._content = f'{self._content}{text}'
            return self
        def startH(self):
            "开始一个标题"
            self._content = f'{self._content}<h1>'
            return self
        def endH(self):
            "结束一个标题"
            self._content = f'{self._content}</h1>'
            return self
        def startP(self, align=""):
            "开始一段正文"
            if align == "":
                self._content = f'{self._content}<p>'
            elif align == "left":
                self._content = f'{self._content}<p style="text-align: left;">'
            elif align == "center":
                self._content = f'{self._content}<p style="text-align: center;">'
            elif align == "right":
                self._content = f'{self._content}<p style="text-align: right;">'
            else:
                self._content = f'{self._content}<p>'
            return self
        def endP(self):
            "结束一段正文"
            self._content = f'{self._content}</p>'
            return self
        def startD(self):
            "开始一段带删除线的文字"
            self._content = f'{self._content}<span style="text-decoration: line-through;">'
            return self
        def endD(self):
            "结束一段带删除线的文字"
            self._content = f'{self._content}</span>'
            return self
        def startS(self, size=16):
            "开始一段大小为size的文字"
            self._content = f'{self._content}<span class="font-size-{size}">'
            return self
        def endS(self):
            "结束一段特定大小的文字"
            self._content = f'{self._content}</span>'
            return self
        def startB(self):
            "开始一段加粗的文字"
            self._content = f'{self._content}<strong>'
            return self
        def endB(self):
            "结束一段加粗的文字"
            self._content = f'{self._content}</strong>'
            return self
        def startY(self):
            "开始一段引用"
            self._content = f'{self._content}<blockquote>'
            return self
        def endY(self):
            "结束一段引用"
            self._content = f'{self._content}</blockquote>'
            return self
        def br(self):
            "插入换行，不用结束，一般新段默认换行"
            self._content = f'{self._content}<p><br/></p>'
            return self
        def line(self,type=0):
            "插入一段分割线，不用结束"
            ll = ('<figure class="img-box" contenteditable="false"><img src="//i0.hdslb.com/bfs/article/0117cbba35e51b0bce5f8c2f6a838e8a087e8ee7.png" class="cut-off-1"/></figure>',
                  '<figure class="img-box" contenteditable="false"><img src="//i0.hdslb.com/bfs/article/4aa545dccf7de8d4a93c2b2b8e3265ac0a26d216.png" class="cut-off-2"/></figure>',
                  '<figure class="img-box" contenteditable="false"><img src="//i0.hdslb.com/bfs/article/71bf2cd56882a2e97f8b3477c9256f8b09f361d3.png" class="cut-off-3"/></figure>',
                  '<figure class="img-box" contenteditable="false"><img src="//i0.hdslb.com/bfs/article/db75225feabec8d8b64ee7d3c7165cd639554cbc.png" class="cut-off-4"/></figure>',
                  '<figure class="img-box" contenteditable="false"><img src="//i0.hdslb.com/bfs/article/4adb9255ada5b97061e610b682b8636764fe50ed.png" class="cut-off-5"/></figure>',
                  '<figure class="img-box" contenteditable="false"><img src="//i0.hdslb.com/bfs/article/02db465212d3c374a43c60fa2625cc1caeaab796.png" class="cut-off-6"/></figure>')
            self._content = f'{self._content}{ll[type]}'
            return self
        def startU(self):
            "开始一段无序列表"
            self._content = f'{self._content}<ul class=" list-paddingleft-2">'
            return self
        def endU(self):
            "结束一段无序列表"
            self._content = f'{self._content}</ul>'
            return self
        def startO(self):
            "开始一段有序列表"
            self._content = f'{self._content}<ol class=" list-paddingleft-2">'
            return self
        def endO(self):
            "结束一段有序列表"
            self._content = f'{self._content}</ol>'
            return self
        def startL(self):
            "开始列表中的一列"
            self._content = f'{self._content}<li>'
            return self
        def endL(self):
            "结束列表中的一列"
            self._content = f'{self._content}</li>'
            return self
        def startA(self, url=""):
            "插入站内链接,链接说明文字请用add方法添加"
            self._content = f'{self._content}<a href="{url}">'
            return self
        def endA(self):
            "结束插入站内链接"
            self._content = f'{self._content}</a>'
            return self
        def picUrl(self, url="", text="", width="", height=""):
            "插入站内图片链接,添加图片说明,指定图片长宽,比如15px，25%"
            self._content = f'{self._content}<figure contenteditable="false" class="img-box"><img src="{url}" '
            if width:
                self._content = f'{self._content}width="{width}" '
            if height:
                self._content = f'{self._content}height="{height}" '
            self._content = f'{self._content}/><figcaption class="caption" contenteditable="">{text}</figcaption></figure>'
            return self
        def picFile(self, article: "Article类的实例", file: "本地图片文件或图片Bytes", text="", width="", height=""):
            "插入本地图片文件或Bytes,添加图片说明,指定图片长宽,比如15px，25%"
            ret = article.articleUpcover(file)
            picurl = ret["data"]["url"]
            picurl = picurl.replace("http", "https")
            return self.picUrl(picurl, text, width, height)
        def vote(self, article: "Article类的实例", vote: "vote投票结构体字典"):
            "插入站内投票"
            id = article.articleCreateVote(vote)["data"]["vote_id"]
            self._content = f'{self._content}<figure class="img-box" contenteditable="false"><img src="//i0.hdslb.com/bfs/article/a9fb8e570e9683912de228446e606745cce62aa6.png" class="vote-display" data-vote-id="{id}"/><figcaption class="vote-title web-vote" contenteditable="">{vote["title"]}</figcaption></figure>'
            return self
        def card(self, Article: "Article类的实例", id: "根据type类型填写id", type: "video:视频标签 str,article:专栏标签,fanju:番剧标签,music:音乐标签,shop:会员购标签,caricature:漫画标签 int,live:直播标签 str"):
            "插入引用标签"
            def video():
                ret = Article.articleCardsBvid(id)
                picurl = ret["data"][id]["pic"]
                picurl = picurl.replace("http", "https")
                aid = ret["data"][id]["aid"]
                return f'<figure class="img-box" contenteditable="false"><img src="{picurl}" aid="{aid}" class="video-card nomal" type="nomal"/></figure>'
            def article():
                ret = Article.articleCardsCvid(id)
                picurl = ret["data"]["banner_url"]
                picurl = picurl.replace("http", "https")
                aid = ret["data"]["id"]
                return f'<figure class="img-box" contenteditable="false"><img src="{picurl}" aid="{aid}" class="article-card" type="normal"/></figure>'
            def fanju():
                ret = Article.articleCardsCvid(id)
                picurl = ret["data"]["cover"]
                picurl = picurl.replace("http", "https")
                return f'<figure class="img-box" contenteditable="false"><img src="{picurl}" aid="{id}" class="fanju-card" type="normal"/></figure>'
            def music():
                ret = Article.articleCardsCvid(id)
                picurl = ret["data"]["cover_url"]
                picurl = picurl.replace("http", "https")
                return f'<figure class="img-box" contenteditable="false"><img src="{picurl}" aid="{id}" class="music-card" type="normal"/></figure>'
            def shop():
                ret = Article.articleCardsCvid(id)
                picurl = ret["data"]["performance_image"]
                picurl = picurl.replace("http", "https")
                return f'<figure class="img-box" contenteditable="false"><img src="{picurl}" aid="{id}" class="shop-card" type="normal"/></figure>'
            def caricature():
                ret = Article.articleMangas(id)
                picurl = ret["data"][id]["vertical_cover"]
                picurl = picurl.replace("http", "https")
                return f'<figure class="img-box" contenteditable="false"><img src="{picurl}" aid="{id}" class="caricature-card nomal" type="nomal"/></figure>'
            def live():
                ret = Article.articleCardsCvid(id)
                picurl = ret["data"]["cover"]
                picurl = picurl.replace("http", "https")
                aid = ret["data"]["room_id"]
                return f'<figure class="img-box" contenteditable="false"><img src="{picurl}" aid="{aid}" class="live-card" type="normal"/></figure>'

            index = {
                "video": video,
                "article": article,
                "fanju": fanju,
                "music": music,
                "shop": shop,
                "caricature": caricature,
                "live": live,
                }
            if type in index:
                self._content = f'{self._content}{index[type]()}'
            return self
        def output(self):
            "输出,用于Article类提交content"
            return self._content

    def __init__(self, cookieData, tilte="", content="", aid=0, category=0, list_id=0, tid=4, original=1, image_urls="", origin_image_urls=""):
        "创建一个B站专栏草稿"
        bili.__init__(self)
        bili.login_by_cookie(self, cookieData)
        self._tilte = tilte
        self._content = content
        self._category = category
        self._list_id = list_id
        self._tid = tid
        self._original = original
        self._image_urls = image_urls
        self._origin_image_urls = origin_image_urls
        if(aid == 0):
            ret = self.createArticle(tilte, content, aid, category, list_id, tid, original, image_urls, origin_image_urls)
            self._aid = ret["data"]["aid"]
        else:
            self._aid = aid

    def setTilte(self, tilte=0):
        "设置专栏标题"
        self._tilte = tilte
    def setCategory(self, category=0):
        "设置专栏分类"
        self._category = category
    def setListId(self, list_id=0):
        "设置文集编号"
        self._list_id = list_id
    def setTid(self, tid=4):
        "设置专栏封面类型"
        self._tid = tid
    def setOriginal(self, original=1):
        "设置专栏是否为原创,原创为1,非原创为0"
        self._original = original
    def setImage(self, origin_image_urls: str, image_urls=""):
        "设置专栏缩略图,image_urls为缩略图网址，origin_image_urls为缩略图原图在文章中的网址"
        self._origin_image_urls = origin_image_urls
        if image_urls:
            self._image_urls = image_urls
        else:
            self._image_urls = origin_image_urls
    def setContent(self, content: Content):
        "设置文章内容"
        self._content = content.output()

    def getAid(self, url=False):
        "返回创建文章的aid或url,可通过url在网页上修改此文章"
        if url:
            return f'https://member.bilibili.com/v2#/upload/text/edit?aid={self._aid}'
        else:
            return self._aid

    def refresh(self):
        "如果在本程序外(例如网页上)修改了本文章,执行此函数同步"
        ret = self.getArticle(self._aid)
        self._tilte = ret["data"]["tilte"]
        self._content = ret["data"]["content"]
        self._category = ret["data"]["category"]["id"]
        if(ret["data"]["list"] != None):
            self._list_id = ret["data"]["list"]["id"]
        self._tid = ret["data"]["template_id"]
        self._original = ret["data"]["original"]
        self._image_urls = ret["data"]["image_urls"][0]
        self._origin_image_urls = ret["data"]["origin_image_urls"][0] #这里可能有丢失封面的问题

    def save(self):
        "保存至B站上草稿箱,不发布,网页上可编辑"
        return self.createArticle(self._tilte, self._content, self._aid, self._category, self._list_id, self._tid, self._original, self._image_urls, self._origin_image_urls)

    def submit(self):
        "发布至B站上"
        return self.createArticle(self._tilte, self._content, self._aid, self._category, self._list_id, self._tid, self._original, self._image_urls, self._origin_image_urls, True)

    def delself(self):
        '''删除当前文章草稿'''
        self.deleteArticle(self._aid)

    def __del__(self):
        bili.close(self)