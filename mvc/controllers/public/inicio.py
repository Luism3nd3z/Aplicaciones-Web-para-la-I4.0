import web
import app

app = web.application(urls, globals()) 
render = web.template.render('mvc/views/public/', base="layout")

class Inicio:
    def GET(self):
        return render.inicio()