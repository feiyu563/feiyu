#coding=utf8
#by:zjk
import tornado.ioloop
import tornado.web
from session_factory import my_seesion
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print self.request
        s=my_seesion(self)
        ret=s['userinfo']
        if ret:
            self.redirect('/index')
        else:
            self.render('login.html')
    def post(self):
        s=my_seesion(self)
        user=self.get_argument('username')
        pwd=self.get_argument('password')
        li=[user,pwd]
        #这里可以写数据库校验
        if user=='zjk':
            s['userinfo']=li
            self.redirect('/index')
        else:
            self.redirect('/login')
            
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        s=my_seesion(self)
        ret=s['userinfo']
        if ret:
            self.write("Hello, "+ret[0])
        else:
            self.redirect('/login')
            
settings={'debug':True} #开启修改保存后自动重启服务
application = tornado.web.Application([
    (r"/login", MainHandler),
    (r"/index", IndexHandler),
],**settings) #开启修改保存后自动重启服务,传入的settings参数


#创建绑定多个域名
application.add_handlers('auto.zjk.com.cn', [
    (r"/index", MainHandler),
    ])
application.add_handlers('admin.zjk.com.cn', [
    (r"/index", MainHandler),
    ])

if __name__ == "__main__":
    print 'listening 8888'
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()