from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk

#Aqui defino la primera ventana, global para que funcione en donde sea que la solicite, y coloco dos botones que tienen la funcion de diferentes roles

def inicio():

    global ventana1
    ventana1=Tk()
    menu1 = Menu(ventana1)
    ventana1.title("Roles")
    ventana1.geometry("900x700")
    ventana1.resizable(0,0)
    titulo=Label(ventana1,text="Roles",height="3", width="200")
    titulo.pack()
    Espacio=Label(ventana1,text="",height="3", width="100")
    Espacio.pack()
    boton_administrador=Button(ventana1,text="Administrador",height="3", width="100",command=administrador)
    boton_administrador.pack() 
    Espacio2=Label(ventana1, text="",height="3", width="100")
    Espacio2.pack()
    boton_oficinista=Button(ventana1,text="Oficinista",height="3", width="100", command=oficinista)
    boton_oficinista.pack()

    ventana1.mainloop()

#Aqui creo otra ventana que va a tener las opciones disponibles para un aadministrador

def administrador():
    global ventana_crea_sec
    ventana_crea_sec=Toplevel(ventana1)
    ventana_crea_sec.title("Administrador")
    ventana_crea_sec.geometry("900x700")
    texto1=Label(ventana_crea_sec, text="Opciones disponibles para administrador")
    texto1.pack()
    espacio=Label(ventana_crea_sec, text="", height="2", width="50")
    espacio.pack()
    espacio1=Label(ventana_crea_sec, text="", height="2", width="50")
    espacio1.pack()
    boton_crea_sec=Button(ventana_crea_sec,text="Crear seccion", height="2", width="50", command=inscripcion)
    boton_crea_sec.pack()
    espacio2=Label(ventana_crea_sec, text="", height="2", width="50")
    espacio2.pack()
    boton_inscrip_est=Button(ventana_crea_sec,text="Inscripcion de estudiantes", height="2", width="50", command=inscripcion_estudiantes)
    boton_inscrip_est.pack()
    espacio3=Label(ventana_crea_sec, text="", height="2", width="50")
    espacio3.pack()
    boton_lista=Button(ventana_crea_sec,text="Lista", height="2", width="50", command=sec_con_est)
    boton_lista.pack()
    espacio5=Label(ventana_crea_sec, text="", height="2", width="50")
    espacio5.pack()
    boton_cerrar=Button(ventana_crea_sec,text="Cerrar", height="2", width="50", command=quit)
    boton_cerrar.pack()

#Aqui igualmente creo otra ventana pero esta vez con las opciones de oficinista

def oficinista():
    global ventana_ofi
    ventana_ofi=Toplevel(ventana1)
    ventana_ofi.title("Oficinista")
    ventana_ofi.geometry("900x700")
    texto=Label(ventana_ofi, text="Opciones disponibles para oficinista")
    texto.pack()
    Espacio=Label(ventana_ofi, text="", height="2", width="50")
    Espacio.pack()
    Espacio1=Label(ventana_ofi, text="", height="2", width="50")
    Espacio1.pack()
    boton_inscrip_est_ofi=Button(ventana_ofi,text="Inscripcion de estudiantes", height="2", width="50", command=inscripcion_estudiantes)
    boton_inscrip_est_ofi.pack()
    Espacio2=Label(ventana_ofi, text="", height="2", width="50")
    Espacio2.pack()
    boton_lista_ofi=Button(ventana_ofi,text="Lista", height="2", width="50", command=sec_con_est)
    boton_lista_ofi.pack()
    Espacio4=Label(ventana_ofi, text="", height="2", width="50")
    Espacio4.pack()
    boton_cerrar=Button(ventana_ofi,text="Cerrar", height="2", width="50", command=quit)
    boton_cerrar.pack()

#Esta ventana tiene la funcion de crear las secciones para agregar mas adelante a los estudiantes

def inscripcion():
    global ventana_inscripcion
    ventana_inscripcion=Toplevel(ventana1)
    ventana_inscripcion.title("Creacion de secciones")
    ventana_inscripcion.geometry("900x700")
    global nombre_seccion
    nombre_seccion=StringVar()
    global campos_seccion
    campos_seccion=IntVar()
    escriba_nombreSec=Label(ventana_inscripcion, text="Escriba el nombre que desea agregar a la seccion:").pack()
    escriba_nombreSec=Entry(ventana_inscripcion,textvariable=nombre_seccion).pack()
    campos_Sec=Label(ventana_inscripcion, text="Digite los campos deseados para esta seccion:").pack()
    campos_Sec=Entry(ventana_inscripcion,textvariable=campos_seccion).pack()
    Label(ventana_inscripcion, text="",height="1", width="50").pack()
    Button(ventana_inscripcion, text="Guardar seccion", command=guardar_seccion1).pack()
    Button(ventana_inscripcion, text="Info de la seccion creada", command=info_crea_sec).pack()

seccioncreada={}

def guardar_seccion1():
    global valores
    global i
    seccioncreada[nombre_seccion.get()]=campos_seccion.get()
    valores=[]
    for i,x in seccioncreada.items():
        valores.append(i)

#Esta otra ventana posee la funcion de agregar a los estudiantes que van a estar en la seccion creada anteriormente

def inscripcion_estudiantes():
    global ventana_inscripcion_estudiantes
    ventana_inscripcion_estudiantes=Toplevel(ventana1)
    ventana_inscripcion_estudiantes.title("Inscripcion de estudiantes")
    ventana_inscripcion_estudiantes.geometry("900x700")
    global nombre
    nombre=StringVar()
    global apellidos
    apellidos=StringVar()
    global cedula
    cedula=IntVar()
    global seccion
    seccion=StringVar()
    nombreSec=Label(ventana_inscripcion_estudiantes, text="Nombre del estudiante:").pack()
    nombreSec=Entry(ventana_inscripcion_estudiantes,textvariable=nombre).pack()
    apellidos_Sec=Label(ventana_inscripcion_estudiantes, text="Apellidos del estudiante:").pack()
    apellidos_Sec=Entry(ventana_inscripcion_estudiantes,textvariable=apellidos).pack()  
    cedulaSec=Label(ventana_inscripcion_estudiantes, text="Cedula del estudiante:").pack()
    cedulaSec=Entry(ventana_inscripcion_estudiantes,textvariable=cedula).pack()
    Sec=Label(ventana_inscripcion_estudiantes, text="Seccion en la que va a estar:").pack()
    combo=ttk.Combobox(ventana_inscripcion_estudiantes,values=valores)
    combo.pack()
    Label(ventana_inscripcion_estudiantes, text="",height="1", width="50").pack()
    Button(ventana_inscripcion_estudiantes, text="Info completa",command=info_completa).pack()
    Label(ventana_inscripcion_estudiantes, text="",height="1", width="50").pack()
    Button(ventana_inscripcion_estudiantes, text="Guardar estudiantes", command=guardar_estudiantes1).pack()

datos_estudiantes={}

def guardar_estudiantes1():
    global valores
    global i
    datos_estudiantes[nombre_seccion.get()]=nombre.get()
    valores=[]
    for i,x in datos_estudiantes.items():
        valores.append(i)

#Este es un simple guardado de datos para los estudiantes agregados a alguna seccion, mas le que esta en la linea 138 a 146

def guardar_datos_inscripcion_estudiantes():
    datos_inscripcion_estudiantes=[]
    datos_inscripcion_estudiantes.append(nombre.get())
    datos_inscripcion_estudiantes.append(apellidos.get())
    datos_inscripcion_estudiantes.append(cedula.get())
    datos_inscripcion_estudiantes.append(seccion.get())
    ventana_datos_inscripcion_estudiantes=Toplevel(ventana_inscripcion_estudiantes)
    ventana_datos_inscripcion_estudiantes.title("Estudiante")
    ventana_datos_inscripcion_estudiantes.geometry("500x500")
    nombre_estudiante= nombre.get()
    Label(ventana_datos_inscripcion_estudiantes,text="Nombre del estudiante:").pack()
    Label(ventana_datos_inscripcion_estudiantes, text=nombre_estudiante).pack()
    apellidos_estudiante= apellidos.get()
    Label(ventana_datos_inscripcion_estudiantes,text="Apellidos del estudiante:").pack()
    Label(ventana_datos_inscripcion_estudiantes, text=apellidos_estudiante).pack()   
    cedula_estudiante= cedula.get()
    Label(ventana_datos_inscripcion_estudiantes,text="Cedula del estudiante:").pack()
    Label(ventana_datos_inscripcion_estudiantes, text=cedula_estudiante).pack()
    seccion_estudiante= seccion.get()
    Label(ventana_datos_inscripcion_estudiantes,text="Seccion en la que va a estar:").pack()
    Label(ventana_datos_inscripcion_estudiantes, text=nombre_seccion.get()).pack()

#Este es otro guardado de datos que en este caso sirve para guardar la seccion creada, mas el que esta en la linea 99 a 107

def guardar_datos_inscripcion():
    datos_inscripcion=[]
    datos_inscripcion.append(nombre_seccion.get())
    datos_inscripcion.append(campos_seccion.get())
    ventana_datos_inscripcion=Toplevel(ventana_inscripcion)
    ventana_datos_inscripcion.title("Seccion")
    ventana_datos_inscripcion.geometry("500x500")
    nombre_de_seccion= nombre_seccion.get()
    Label(ventana_datos_inscripcion,text="El nombre de la seccion es de:").pack()
    Label(ventana_datos_inscripcion, text=nombre_de_seccion).pack()
    campo_sec= campos_seccion.get()
    Label(ventana_datos_inscripcion,text="Los campos para esta seccion son de:").pack()
    Label(ventana_datos_inscripcion, text=campo_sec).pack()

#Esta funcion sirve para ver los estudiantes agregados y a que seccion pertenecen

def total():
    datos_estudiantes=[]
    datos_estudiantes.append(nombre.get())
    datos_estudiantes.append(nombre_seccion.get())
    datos_estudiantes_total=Toplevel(ventana_inscripcion_estudiantes)
    datos_estudiantes_total.title("Seccion y estudiantes")
    datos_estudiantes_total.geometry("500x500")
    nombre_estudiante= nombre.get()
    Label(datos_estudiantes_total,text="Nombre del estudiante:").pack()
    Label(datos_estudiantes_total, text=nombre_estudiante).pack()
    seccion_estudiante= seccion.get()
    Label(datos_estudiantes_total,text="Seccion en la que fue agregado:").pack()
    Label(datos_estudiantes_total, text=nombre_seccion.get()).pack()
    Button(datos_estudiantes_total, text="Ir a administador", command=administrador).pack()
    Label(datos_estudiantes_total, text="",height="1", width="50").pack()
    Button(datos_estudiantes_total, text="Ir a oficinista", command=oficinista).pack()

#Esta otra funcion muestra la informacion completa de todo los agregado anteriormente, nombre de seccion, campos, nombre del estudiante, etc...

def info_completa():
    info_inscripcion=[]
    info_inscripcion.append(nombre_seccion.get())
    info_inscripcion.append(campos_seccion.get())
    info_inscripcion_estudiantes=[]
    info_inscripcion_estudiantes.append(nombre.get())
    info_inscripcion_estudiantes.append(apellidos.get())
    info_inscripcion_estudiantes.append(cedula.get())
    info_inscripcion_estudiantes.append(seccion.get())
    ventana_info_inscripcion_estudiantes=Toplevel(ventana_inscripcion_estudiantes)
    ventana_info_inscripcion_estudiantes.title("Informacion general")
    ventana_info_inscripcion_estudiantes.geometry("500x500")
    nombre_de_seccion= nombre_seccion.get()
    Label(ventana_info_inscripcion_estudiantes,text="El nombre de la seccion creada anteriormente:").pack()
    Label(ventana_info_inscripcion_estudiantes, text=nombre_de_seccion).pack()
    campo_sec= campos_seccion.get()
    Label(ventana_info_inscripcion_estudiantes,text="Los campos para esta seccion son de:").pack()
    Label(ventana_info_inscripcion_estudiantes, text=campo_sec).pack()
    nombre_estudiante= nombre.get()
    Label(ventana_info_inscripcion_estudiantes,text="Nombre del estudiante:").pack()
    Label(ventana_info_inscripcion_estudiantes, text=nombre_estudiante).pack()
    apellidos_estudiante= apellidos.get()
    Label(ventana_info_inscripcion_estudiantes,text="Apellidos del estudiante:").pack()
    Label(ventana_info_inscripcion_estudiantes, text=apellidos_estudiante).pack() 
    cedula_estudiante= cedula.get()
    Label(ventana_info_inscripcion_estudiantes,text="Cedula del estudiante:").pack()
    Label(ventana_info_inscripcion_estudiantes, text=cedula_estudiante).pack()
    seccion_estudiante= seccion.get()
    Label(ventana_info_inscripcion_estudiantes,text="Seccion en la que fue agregado:").pack()
    Label(ventana_info_inscripcion_estudiantes, text=nombre_seccion.get()).pack()
    Button(ventana_info_inscripcion_estudiantes, text="Ir a administador", command=administrador).pack()
    Label(ventana_info_inscripcion_estudiantes, text="",height="1", width="50").pack()
    Button(ventana_info_inscripcion_estudiantes, text="Ir a oficinista", command=oficinista).pack()
    Label(ventana_info_inscripcion_estudiantes, text="",height="1", width="50").pack()
    Button(ventana_info_inscripcion_estudiantes, text="Agregar mas estudiantes", command=inscripcion_estudiantes).pack()

#Esta funcion me guarda los datos de cuando se crea una seccion, pero de extra le agrego dos botones para que pueda seguir o para poder devolverse a crear otra seccion

def info_crea_sec():
    info_creacion_sec=[]
    info_creacion_sec.append(nombre_seccion.get())
    info_creacion_sec.append(campos_seccion.get())
    ventana_info_creacion_sec=Toplevel(ventana_inscripcion)
    ventana_info_creacion_sec.title("Seccion creada")
    ventana_info_creacion_sec.geometry("500x500")
    nombre_de_seccion= nombre_seccion.get()
    Label(ventana_info_creacion_sec,text="El nombre de la seccion es de:").pack()
    Label(ventana_info_creacion_sec, text=nombre_de_seccion).pack()
    campo_sec= campos_seccion.get()
    Label(ventana_info_creacion_sec,text="Los campos para esta seccion son de:").pack()
    Label(ventana_info_creacion_sec, text=campo_sec).pack()
    Button(ventana_info_creacion_sec, text="Seguir", command=administrador).pack()
    Label(ventana_info_creacion_sec, text="",height="1", width="50").pack()
    Button(ventana_info_creacion_sec, text="Crear otra seccion", command=inscripcion).pack()

#Esta funcion almacena a las secciones creadas y las muestra en un combobox para que puedan escojer que seccion con estudiantes quieren ver

def sec_con_est():
    global ventana_seccion_con_est
    ventana_seccion_con_est=Toplevel(ventana1)
    ventana_seccion_con_est.title("Seccion con estudiantes")
    ventana_seccion_con_est.geometry("500x500")
    global seccion
    seccion=StringVar()
    Sec=Label(ventana_seccion_con_est, text="Estudiantes en la seccion:").pack()
    combo=ttk.Combobox(ventana_seccion_con_est,values=[nombre_seccion.get()])
    combo.pack()
    Label(ventana_seccion_con_est, text="",height="1", width="50").pack()
    Button(ventana_seccion_con_est, text="Ir",command=total).pack()

inicio()