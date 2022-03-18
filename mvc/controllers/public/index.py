import web # web.py Library
import app # app Library

# Define the URL views mappings
render = web.template.render("mvc/views/public/", base="layout")

class Index:
    """Clase para controlar la pagina mvc/views/public/index.html
    """

    def GET(self):
        """Metodo para renderizar la pagina mvc/views/public/index.html

        Returns:
            index{html}: mvc/views/public/index.html
        """        """"""
        return render.index()
