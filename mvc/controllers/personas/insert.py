import web

render = web.template.render("mvc/views/personas/", base="template")

class Insert():

    def GET(self):
        try:
            return render.insert() # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)