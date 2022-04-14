import web
import app

app = web.application(urls, globals()) 
render = web.template.render('mvc/controllers/public/', base="layout")

class Inicio:
    def GET(self):
        return render.inicio()