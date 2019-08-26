from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

############### FRAME #######################
miFrame=Frame(root, width=1200, height=600)
miFrame.pack()
#############################################


################## FUNCIONES DE ALERTAS ############################################
def infoAdicional():
    messagebox.showinfo("¡INFO!", "Procesador de textos 2019")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salir():
    valor=messagebox.askquestion("Salir", "¿Deseas Salir de la APP?")
    if valor == "yes":
        root.destroy()

################################################################################################

######################### FUNCIONES CRUD ########################################
def conectar():
    miConexion=sqlite3.connect("Usuarios")
    try:
            
        miCursor=miConexion.cursor()

        miCursor.execute('''
                CREATE TABLE DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(10),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(100))
        ''')

        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
            messagebox.showwarning("¡ Atención !", "La BBDD ya existe")
                
def borrarCampos():

        miId.set("")
        miNombre.set("")
        miApellido.set("")
        miDireccion.set("")
        miPass.set("")
        textoComentario.delete(1.0, END)

def crear():
    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '"+ miNombre.get()+
    "','"+ miPass.get()+
    "','"+ miApellido.get()+
    "','"+ miDireccion.get()+
    "','"+ textoComentario.get("1.0", END) + "')")

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro Insertado con éxito")

def leer():
        miConexion=sqlite3.connect("Usuarios")

        miCursor=miConexion.cursor()

        miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())

        user = miCursor.fetchall()
        for usuario in user:
                miId.set(usuario[0])
                miNombre.set(usuario[1])
                miPass.set(usuario[2])
                miApellido.set(usuario[3])
                miDireccion.set(usuario[4])
                textoComentario.insert(1.0, usuario[5])

        miConexion.commit()            

def actualizar():
        miConexion=sqlite3.connect("Usuarios")

        miCursor=miConexion.cursor()
        miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get()+
        "', PASSWORD='" + miPass.get() +
        "', APELLIDO='" + miApellido.get() +
        "', DIRECCION='" + miDireccion.get() +
        "', COMENTARIOS='" + textoComentario.get("1.0", END) +
        "' WHERE ID="+ miId.get())
        

        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con éxito")   

def eliminar():
        miConexion=sqlite3.connect("Usuarios")

        miCursor=miConexion.cursor()
        miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())

        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro borrado con éxito")

############# MENÚ #################################       
barraMenu=Menu(miFrame)
root.config(menu=barraMenu, width=300, height=300)
####################################################

############ CONECTAR BD ##################
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conectar)
bbddMenu.add_separator()
bbddMenu.add_command(label="Salir", command=salir)    
###########################################

############# BORRAR #########################
borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar", command=borrarCampos)
############################################### 

############# CRUD ############################
crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_separator()
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_separator()
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_separator()
crudMenu.add_command(label="Borrar", command=eliminar)        
###############################################

############# AYUDA ###############################################
archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de ...", command=infoAdicional)
#######################################################################

############### INTEGRACIÓN AL MENÚ ##############################
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
###################################################################

        
############### CAMPOS DE LABEL #########################
ide=Label(miFrame, text="ID: ")
ide.grid(row=0, column=0, sticky="w")

name=Label(miFrame, text="NOMBRE: ")
name.grid(row=1, column=0, sticky="w")

pas=Label(miFrame, text="PASSWORD: ")
pas.grid(row=2, column=0, sticky="w")

ape=Label(miFrame, text="APELLIDOS: ")
ape.grid(row=3, column=0, sticky="w")

dire=Label(miFrame, text="DIRECCIÓN: ")
dire.grid(row=4, column=0, sticky="w")

come=Label(miFrame, text="COMENTARIOS: ")
come.grid(row=5, column=0, sticky="w")
##########################################################


#################### CAMPOS DE TEXTO #######################
miId= StringVar()    # Convertir los campos a String.
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroId=Entry(miFrame, textvariable=miId)
cuadroId.grid(row=0, column=1, pady=10)

cuadroName=Entry(miFrame, textvariable=miNombre)
cuadroName.grid(row=1, column=1, pady=10)

cuadroPas=Entry(miFrame, textvariable=miPass)
cuadroPas.grid(row=2, column=1, pady=10)
cuadroPas.config(show="*")

cuadroApe=Entry(miFrame, textvariable=miApellido)
cuadroApe.grid(row=3, column=1, pady=10)

cuadroDire=Entry(miFrame, textvariable=miDireccion)
cuadroDire.grid(row=4, column=1, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)
###############################################################


###################### BÓTONES CRUD ##############################
miFrame2=Frame(root)
miFrame2.pack()

botonCreate=Button(miFrame2, text="Create", command=crear)
botonCreate.grid(row=6, column=0, pady=10)

botonRead=Button(miFrame2, text="Read", command=leer)
botonRead.grid(row=6,  column=1, pady=10)

botonUpdate=Button(miFrame2, text="Update", command=actualizar)
botonUpdate.grid(row=6, column=2, pady=10)

botonDelete=Button(miFrame2, text="Delete", command=eliminar)
botonDelete.grid(row=6, column=3, pady=10)
####################################################################


root.mainloop()        


