import web

urls = (
  '/', 'Index'  
)
             
app = web.application(urls, globals())  

render = web.template.render('templates/')

class Index(object):
	def GET(self):
		greeting = "Hello World!"
		return render.index(greeting = greeting)   

if __name__ == "__main__":
	app.run()

	
----------------------------------------------------------------------------
--------------------------万恶分割线----------------------------------------
----------------------------------------------------------------------------
在浏览器通过访问到你的网页应用程序时，发生了下面一些事情：

1.浏览通过网络连到你自己的电脑，它的名字叫做localhost，这是一个标准称谓，表示
  的就是网络中你自己的这台计算机，不管它实际名字是什么，你都可以使用locahost来
  访问。它使用到的网络端口是80。
2.连接成功以后，浏览器对 bin/app.py这个应用程序发出了 HTTP请求(request),要求访
  问URL/，这通常是一个网络的第一个 URL。
3.在 bin/app.py里，我们有一个列表，里边包含了 URL 和类的匹配关系。我们这里只定
  义了一组匹配，那就是 '/', 'index'的匹配。它的含义是：如果有人使用浏览器访问
  / 这一级目录， lpthw.web将找到并加载 calss index,从而用它处理这个浏览器请求。
4.现在 lpthw.web将找到了 class index，然后针对这个类的一个实例调用了 index.GET
  这个方法函数。该函数运行后返回一个字符串，以供 lpthw.web将其传递给浏览器。
5.最后 lpthw.web完成了对于浏览器请求的处理，将响应(response)回传给浏览器，于是
  你看到了现在的页面。

确定你真的弄懂了这些，你需要画一个示意图，来理清信息是如何从浏览器传递到 lpthw.web，
再到 index.GET，再回到你的浏览器的。
