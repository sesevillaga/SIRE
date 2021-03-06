from django.conf.urls import url
from views import *
from viewsHorarios import *
from viewsClientes import *
from viewTrabajadores import *
from viewsProveedores import *
from viewsNegocios import *
from viewsCamiones import *
from viewsMaterialRecolectado import *

urlpatterns = [
# ----------------URLS proveedores------------------
url(r'guardarProveedores/$',insertarProveedores),
url(r'proveedores/$',insertarProveedores),



# -------------URLS proveedores-----------------
# url(r'consltarTrabajadores/$',consltarTrabajadores),      (hay problemas con esta url)
url(r'trabajadores/$',trabajadores),
url(r'insertarTrabajador/$',insertarTrabajador),


# -----------URLS horarios------------------
url(r'insertarHorario/$',insertarHorario),
url(r'consultarHorarios/$',consultarHorarios),
url(r'modificarHorarios/$',modificarHorarios),
url(r'guardarHorarios/$',guardarHorarios),
url(r'horariosEliminar/$',horariosEliminar),
url(r'eliminarHorarios/$',eliminarHorarios),

# -------------URLS clientes--------------------
url(r'eliminarCli/$',eliminarCli),
url(r'eliminarCliente/$',eliminarCliente),
url(r'guardarCambiosClientes/$',guardarCambiosClientes),
url(r'modificarClientes/$',modificarClientes),
url(r'consultarClientes/$',consultarClientes),
url(r'guardarClientes/$',insertarClientes),
url(r'clientes/$',insertarClientes),

# ---------------URLS negocios----------------------
url(r'eliminarNegocios/$',eliminarNegocios),
url(r'eliminarNeg/$',eliminarNeg),
url(r'guardarNegocios/$',guardarNegocios),
url(r'consultarNegocios/modificarNegocio/$',modificarNegocios),
url(r'consultarNegocios/$',consultarNegocios),
url(r'insertarNegocios/$',insertarNegocios),
url(r'negocios/$',insertarNegocios),


# --------------URLS material recolectado----------------------
url(r'insertarMaterialRecolectado/$',insertarMaterialRecolectado),
url(r'consultarMaterialRecolectado/$',consultarMaterialRecolectado),
url(r'modificarMaterialRecolectado/$',modificarMaterialRecolectado),
url(r'guardarMaterialRecolectado/$',guardarMaterialRecolectado),
url(r'eliminarMaterialRecolectado/$',eliminarMaterialRecolectado),

# --------------URLS camiones----------------------
url(r'insertarCamiones/$',insertarCamion),
url(r'consultarCamion/$',consultarCamion),
url(r'modificarCamiones/$',modificarCamion),
url(r'guardarCamion/$',guardarCamion),
url(r'eliminarCamiones/$',eliminarCamion),



url(r'^$',menu),

]
