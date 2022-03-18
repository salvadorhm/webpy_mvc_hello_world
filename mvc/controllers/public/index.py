import web # web.py Library
import app as app 

render = web.template.render("mvc/views/public/", base="layout")

class Index:

    def GET(self):
        return render.index()
