import tornado.ioloop
import tornado.web
import os
from tornado import gen
from tornado.options import define,options
import psycopg2

class MainHandler(tornado.web.RequestHandler):
    def get(self):
         self.render('hello.html')

# class New(tornado.web.RequestHandler):
#     def get(self):
#         self.render('page.html')    

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html') 

    def post(self):
        a = self.get_body_argument("userid")
        b = self.get_body_argument("password")


        conn = psycopg2.connect(database="gorilla", user='postgres', password='root', host='localhost', port= '5432')
        conn.autocommit = True
        cursor = conn.cursor()
        if q = '''select * from employee where (userid,password) == ('%s','%s') ''' % (a,b):
            self.render('hello.html')
        else:
            self.render('fail.html')    
        cursor.execute(q)
        conn.commit()
        conn.close()
        # if userid == a and password == b:
        #     self.render('hello.html')
        #     #print('success')
        #     # self.set_current_user(username)
        #     # self.redirect(self.get_argument("next", u"/"))
        # else:
        #     self.render('fail.html')
            #print('fail')
            # error_msg = u"?error=" + tornado.escape.url_escape("Login incorrect.")
            # self.redirect(u"/login" + error_msg)

     # def check_permission(self, password, userid):
    #     if userid == "admin" and password == "admin":
    #          self.render('hello.html')
    #     else:
    #          self.render('hello.html')
       

    

# class NewHandler(tornado.web.RequestHandler):
#     async def get(self):
#         entries = await self.query("SELECT * FROM employee")
#         self.render("hello.html", entries=entries)

class SignupHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('page.html')    

    def post(self):
        a = self.get_body_argument("userid")
        b = self.get_body_argument("name")
        c = self.get_body_argument("email")
        d = self.get_body_argument("password")
        conn = psycopg2.connect(database="gorilla", user='postgres', password='root', host='localhost', port= '5432')
        conn.autocommit = True
        cursor = conn.cursor()
        q = '''
        INSERT INTO EMPLOYEE(userid,name,email,password) values('%s','%s','%s','%s')
        ''' % (a,b,c,d)
        cursor.execute(q)
        conn.commit()
        print("Records inserted........")
        conn.close()
        # obj=Employee(a==userid,b==name,c==email,d==password)
        # obj.save()            

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/login',LoginHandler),
        (r'/signup',SignupHandler),
        ])
# TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")    
#         (r'/signup',SignupHandler),
#     ])

# def get(self):
#     # Do some data processing
#     self.render('page.html', variable=value)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()         