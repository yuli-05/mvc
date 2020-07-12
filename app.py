import web

urls = (
    '/delete', 'mvc.controllers.personas.delete.Delete',
    '/', 'mvc.controllers.index.Index',
    '/insert', 'mvc.controllers.personas.insert.Insert',
    '/list', 'mvc.controllers.personas.list.List',
    '/update', 'mvc.controllers.personas.update.Update',
    '/view', 'mvc.controllers.personas.view.View',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()