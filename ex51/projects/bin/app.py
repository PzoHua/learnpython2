#_*_coding=utf-8_*_
import web

urls = (
  '/hello', 'Index'  
)

app = web.application(urls, globals())

# render用于渲染网页(以绿色较大字体显示内容)
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.hello_form()
    
    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        return render.index(greeting = greeting)
            
if __name__ == "__main__":
	app.run()

# ---------------------------------------------------------------------------------------------
# 程序流程：
# 0.在浏览器中输入网址 http://localhost:8080/hello
# 1.浏览器以 GET方式第一次请求(request1)，服务器第一次响应(response1)：给浏览器返回网页hello_form.html内容；
# 2.网页hello_form.html中提交表单；(提交后该网页要求以POST方式再次请求服务器)
# 3.浏览器以 POST方式第二次请求(request2)，服务器第二次响应(response2)：给浏览器返回 index.html的内容。
# 4.网页index.html中有超链接指向hello_form.html(以此达到循环)。
