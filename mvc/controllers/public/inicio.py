import web
import app

render = web.template.render('mvc/controllers/public/', base="layout")

class Inicio:
    def GET(self):
        return render.inicio()