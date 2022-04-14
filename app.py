import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base
import json # se importa la libreria de json para hacer uso y modificación de estos elementos

urls = (
    '/user_list', 'mvc.controllers.admin.user_list.User_list',
    '/bienvenida_administrador','mvc.controllers.admin.bienvenida_administrador.Bienvenida_admintrador',
    '/sensor','mvc.controllers.admin.sensor.Sensor', 
    '/user_view/(.*)','mvc.controllers.admin.user_view.User_view',
    '/registro','mvc.controllers.admin.registro.Registro',
    
    '/bienvenida_usuario','mvc.controllers.operador.bienvenida_usuario.Bienvenida',
    '/sensor','mvc.controllers.operador.sensor.Sensor',

    '/', 'mvc.controllers.public.inicio.Inicio',  
    '/loyout', 'mvc.controllers.public.loyout.Loyout',
    '/login', 'mvc.controllers.public.login.Login',
    '/recuperar_cuenta', 'mvc.controllers.public.recuperar_cuenta.Recuperar_cuenta',   
)
app = web.application(urls, globals())
wsgiapp = app.wsgifunc()


if __name__ == "__main__":
    web.config.debug = True 
    app.run()