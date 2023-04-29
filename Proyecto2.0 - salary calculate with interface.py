from tkinter import *
from tkinter import messagebox


def funcion():
    ventana_salarial.state(newstate="normal")
    ventana1.state(newstate="withdraw")

def inicio():

    global ventana1
    ventana1=Tk()
    menu1 = Menu(ventana1)
    ventana1.title("Planilla")
    ventana1.geometry("900x700")
    ventana1.resizable(0,0)
    ventana1.configure(bg="light steel blue")
    titulo=Label(ventana1,text="Planilla",bg="LightCyan2",height="3", width="200")
    titulo.pack()
    Espacio=Label(ventana1,text="",bg="light steel blue",height="3", width="100")
    Espacio.pack()
    boton_calculo_salarial=Button(ventana1,text="Calculo Salarial",bg="LightCyan2",height="3", width="100",command=calculo_salarial)
    boton_calculo_salarial.pack() 
    Espacio2=Label(ventana1, text="",bg="light steel blue",height="3", width="100")
    Espacio2.pack()
    boton_calculo_gastos=Button(ventana1,text="Calculo de gastos",bg="LightCyan2",height="3", width="100", command=calculo_de_gastos)
    boton_calculo_gastos.pack()
    Espacio3=Label(ventana1,text="",bg="light steel blue",height="3", width="100")
    Espacio3.pack()
    boton_calculo_salarial=Button(ventana1,text="Calculo Salarial",bg="LightCyan2",height="3", width="100")
    boton_Salir=Button(ventana1,text="Salir",command=ventana1.quit,bg="LightCyan2",height="3", width="100")
    boton_Salir.pack()

    ventana1.mainloop()

def calculo_salarial():
    global ventana_salarial
    ventana_salarial=Toplevel(ventana1)
    ventana_salarial.title("Calculo salarial")
    ventana_salarial.geometry("900x700")
    ventana_salarial.configure(bg="light steel blue")
    texto1=Label(ventana_salarial, bg="LightCyan2",text="Bienvenido al calculo salarial, a continuación las opciones:")
    texto1.pack()
    Espacio_salarial=Label(ventana_salarial, text="",bg="light steel blue",height="2", width="50")
    Espacio_salarial.pack()
    Espacio_salarial2=Label(ventana_salarial, text="",bg="light steel blue",height="2", width="50")
    Espacio_salarial2.pack()
    boton_docente_secundaria=Button(ventana_salarial,text="Docente",bg="LightCyan2",height="2", width="50", command=secundaria)
    boton_docente_secundaria.pack()
    Espacio_salarial3=Label(ventana_salarial, text="",bg="light steel blue",height="2", width="50")
    Espacio_salarial3.pack()
    boton_guarda=Button(ventana_salarial,text="Guarda",bg="LightCyan2",height="2", width="50", command=Guarda)
    boton_guarda.pack()
    Espacio_salarial4=Label(ventana_salarial, text="",bg="light steel blue",height="2", width="50")
    Espacio_salarial4.pack()
    boton_conserje=Button(ventana_salarial,text="Conserje",bg="LightCyan2",height="2", width="50", command=Conserje)
    boton_conserje.pack()
    Espacio_salarial5=Label(ventana_salarial, text="",bg="light steel blue",height="2", width="50")
    Espacio_salarial5.pack()
    boton_auxiliar=Button(ventana_salarial,text="Auxiliar",bg="LightCyan2",height="2", width="50", command=Auxiliar)
    boton_auxiliar.pack()
    Espacio_salarial6=Label(ventana_salarial, text="",bg="light steel blue",height="2", width="50")
    Espacio_salarial6.pack()
    boton_direccion=Button(ventana_salarial,text="Direccion",bg="LightCyan2",height="2", width="50", command=Direccion)
    boton_direccion.pack()
    Espacio_salarial7=Label(ventana_salarial, text="",bg="light steel blue",height="2", width="50")
    Espacio_salarial7.pack()
    boton_cocinero=Button(ventana_salarial,text="Cocinero",bg="LightCyan2",height="2", width="50", command=Cocinero)
    boton_cocinero.pack()
    Espacio_salarial8=Label(ventana_salarial, text="",bg="light steel blue",height="2", width="50")
    Espacio_salarial8.pack()
    boton_orientador=Button(ventana_salarial,text="Orientador",bg="LightCyan2",height="2", width="50", command=Orientador)
    boton_orientador.pack()

def secundaria():      
    global ventana_secundaria
    ventana_secundaria=Toplevel(ventana_salarial)
    ventana_secundaria.title("Calculo salarial de secundaria")
    ventana_secundaria.geometry("900x700")
    global lecciones_secundaria_lunes
    lecciones_secundaria_lunes=IntVar()
    global lecciones_secundaria_martes
    lecciones_secundaria_martes=IntVar()
    global lecciones_secundaria_miercoles
    lecciones_secundaria_miercoles=IntVar()
    global lecciones_secundaria_jueves
    lecciones_secundaria_jueves=IntVar()
    global lecciones_secundaria_viernes
    lecciones_secundaria_viernes=IntVar()
    global pago_leccion
    pago_leccion=IntVar()
    ventana_secundaria.configure(bg="light steel blue")
    lecciones_lunes=Label(ventana_secundaria,bg="LightCyan2", text="Digite cuantas lecciones tiene los lunes")
    lecciones_lunes.pack()
    dato_lunes=Entry(ventana_secundaria, textvariable=lecciones_secundaria_lunes)
    dato_lunes.pack()
    lecciones_martes=Label(ventana_secundaria,bg="LightCyan2",text="Digite cuantas lecciones tiene los martes")
    lecciones_martes.pack()
    dato_martes=Entry(ventana_secundaria, textvariable=lecciones_secundaria_martes)
    dato_martes.pack()
    lecciones_miercoles=Label(ventana_secundaria,bg="LightCyan2", text="Digite cuantas lecciones tiene los miercoles")
    lecciones_miercoles.pack()
    dato_miercoles=Entry(ventana_secundaria, textvariable=lecciones_secundaria_miercoles)
    dato_miercoles.pack()
    lecciones_jueves=Label(ventana_secundaria,bg="LightCyan2", text="Digite cuantas lecciones tiene los jueves")
    lecciones_jueves.pack()
    dato_jueves=Entry(ventana_secundaria, textvariable=lecciones_secundaria_jueves)
    dato_jueves.pack()
    lecciones_viernes=Label(ventana_secundaria,bg="LightCyan2", text="Digite cuantas lecciones tiene los viernes")
    lecciones_viernes.pack()
    dato_viernes=Entry(ventana_secundaria, textvariable=lecciones_secundaria_viernes)
    dato_viernes.pack()
    digite_su_pago=Label(ventana_secundaria,bg="LightCyan2", text="Digite su pago de lección, porfavor")
    digite_su_pago.pack()
    pago_por_lección_secundaria=Entry(ventana_secundaria, textvariable=pago_leccion)
    pago_por_lección_secundaria.pack()
    Button(ventana_secundaria,bg="LightCyan2",text="Hacer calculo", command=mensaje).pack()

def mensaje():
    datos_secundaria_semana=[]
    datos_secundaria_semana.append(lecciones_secundaria_lunes.get())
    datos_secundaria_semana.append(lecciones_secundaria_martes.get())
    datos_secundaria_semana.append(lecciones_secundaria_miercoles.get())
    datos_secundaria_semana.append(lecciones_secundaria_jueves.get())
    datos_secundaria_semana.append(lecciones_secundaria_viernes.get())
    total_lecciones=lecciones_secundaria_lunes.get()+lecciones_secundaria_martes.get()+lecciones_secundaria_miercoles.get()+lecciones_secundaria_jueves.get()+lecciones_secundaria_viernes.get()
    if total_lecciones>45:
        messagebox.showerror("","Las lecciones no pueden exceder a 45")
        secundaria()
    else:
        datos_secundaria()

def datos_secundaria():
    datos_secundaria_semana=[]
    datos_secundaria_semana.append(lecciones_secundaria_lunes.get())
    datos_secundaria_semana.append(lecciones_secundaria_martes.get())
    datos_secundaria_semana.append(lecciones_secundaria_miercoles.get())
    datos_secundaria_semana.append(lecciones_secundaria_jueves.get())
    datos_secundaria_semana.append(lecciones_secundaria_viernes.get())
    ventana_datos=Toplevel(ventana_secundaria)
    ventana_datos.title("Total")
    ventana_datos.geometry("900x700")
    ventana_datos.configure(bg="light steel blue")
    pago_lunes=lecciones_secundaria_lunes.get()*pago_leccion.get()
    Label(ventana_datos, bg="LightCyan2",text="Su pago el lunes es de:").pack()
    Label(ventana_datos, text=pago_lunes).pack()
    pago_martes=lecciones_secundaria_martes.get()*pago_leccion.get()
    Label(ventana_datos, bg="LightCyan2",text="Su pago el martes es de:").pack()
    Label(ventana_datos, text=pago_martes).pack()
    pago_miercoles=lecciones_secundaria_miercoles.get()*pago_leccion.get()
    Label(ventana_datos,bg="LightCyan2",text="Su pago el miercoles es de:").pack()
    Label(ventana_datos,text=pago_miercoles).pack()
    pago_jueves=lecciones_secundaria_jueves.get()*pago_leccion.get()
    Label(ventana_datos,bg="LightCyan2",text="Su pago el jueves es de:").pack()
    Label(ventana_datos, text=pago_jueves).pack()
    pago_viernes=lecciones_secundaria_viernes.get()*pago_leccion.get()
    Label(ventana_datos,bg="LightCyan2", text="Su pago el viernes es de:").pack()
    Label(ventana_datos, text=pago_viernes).pack()
    total_lecciones=lecciones_secundaria_lunes.get()+lecciones_secundaria_martes.get()+lecciones_secundaria_miercoles.get()+lecciones_secundaria_jueves.get()+lecciones_secundaria_viernes.get()
    Label(ventana_datos,bg="LightCyan2", text="Sus lecciones por semana son:").pack()
    Label(ventana_datos, text=total_lecciones).pack()
    pago_semanal=pago_lunes+pago_martes+pago_miercoles+pago_jueves+pago_viernes
    Label(ventana_datos,bg="LightCyan2", text="Su pago a la semana es de:").pack()
    Label(ventana_datos, text=pago_semanal).pack()
    pago_quincena=pago_semanal*2
    Label(ventana_datos,bg="LightCyan2",text="Su pago por quincena es de:").pack()
    Label(ventana_datos, text=pago_quincena).pack()
    pago_mensual=pago_quincena*2
    Label(ventana_datos,bg="LightCyan2", text="Su pago mensual es de:").pack()
    Label(ventana_datos, text=pago_mensual).pack()
    porcentaje_seguro= pago_mensual * 0.05
    porcentaje_pension= pago_mensual * 0.03
    porcentaje_banco= pago_mensual * 0.01
    porcentaje_junta= pago_mensual * 0.02
    porcentaje_fondo= pago_mensual * 0.08
    salario_neto = pago_mensual-porcentaje_seguro-porcentaje_pension-porcentaje_banco-porcentaje_junta-porcentaje_fondo
    Label(ventana_datos,bg="LightCyan2", text="Su ingreso neto es de:").pack()
    Label(ventana_datos, text=salario_neto).pack()
    pago_anual=salario_neto*12
    Label(ventana_datos,bg="LightCyan2", text="Su salario anual es de:").pack()
    Label(ventana_datos, text=pago_anual).pack()
    bono_escolar=pago_anual*0.08
    Label(ventana_datos,bg="LightCyan2", text="Su bono escolar es de:").pack()
    Label(ventana_datos, text=bono_escolar).pack()
    aguinaldo=pago_anual/12
    Label(ventana_datos,bg="LightCyan2",text="Su aguinaldo es de:").pack()
    Label(ventana_datos, text=aguinaldo).pack()
    impuesto1=salario_neto*0.10
    impuesto2=salario_neto*0.15
    impuesto3=salario_neto*0.20
    impuesto4=salario_neto*0.25
    if salario_neto>840000 and salario_neto<1233000:
        salario_desp_impuesto1=salario_neto-impuesto1
        Label(ventana_datos,bg="LightCyan2", text="Su salario despues de impuestos de un 10% es de:").pack()
        Label(ventana_datos, text=salario_desp_impuesto1).pack()
    elif salario_neto>1233000 and salario_neto<2163000:
        salario_desp_impuesto2=salario_neto-impuesto2
        Label(ventana_datos,bg="LightCyan2", text="Su salario despues de impuestos de un 15% es de:").pack()
        Label(ventana_datos, text=salario_desp_impuesto2).pack()
    elif salario_neto>2163000 and salario_neto<4325000:
        salario_desp_impuesto3=salario_neto-impuesto3
        Label(ventana_datos,bg="LightCyan2", text="Su salario despues de impuestos de un 20% es de:").pack()
        Label(ventana_datos, text=salario_desp_impuesto3).pack()
    elif salario_neto>4325000:
        salario_desp_impuesto4=salario_neto-impuesto4
        Label(ventana_datos,bg="LightCyan2", text="Su salario despues de impuestos de un 25% es de:").pack()
        Label(ventana_datos, text=salario_desp_impuesto4).pack()
    elif salario_neto<840000:
        Label(ventana_datos,bg="LightCyan2", text="Su salario sin impuestos es de:").pack()
        Label(ventana_datos, text=salario_neto).pack()

def Guarda():
    global ventana_Guarda
    ventana_Guarda=Toplevel(ventana_salarial)
    ventana_Guarda.title("Calculo salarial de guarda")
    ventana_Guarda.geometry("900x700")
    global dias_trabajados_guarda
    dias_trabajados_guarda=IntVar()
    global horas_de_trabajo_guarda
    horas_de_trabajo_guarda=IntVar()
    global pago_hora_guarda
    pago_hora_guarda=IntVar()
    ventana_Guarda.configure(bg="light steel blue")
    dias_guarda=Label(ventana_Guarda,bg="LightCyan2", text="Cuantos dias trabaja a la semana¿?")
    dias_guarda.pack()
    dias_trabajo_guarda=Entry(ventana_Guarda, textvariable=dias_trabajados_guarda)
    dias_trabajo_guarda.pack()
    horas_guarda=Label(ventana_Guarda,bg="LightCyan2", text="Cuantas horas trabaja a la semana¿?")
    horas_guarda.pack()
    horas_trabajadas_guarda=Entry(ventana_Guarda, textvariable=horas_de_trabajo_guarda)
    horas_trabajadas_guarda.pack()
    digite_su_pago=Label(ventana_Guarda,bg="LightCyan2", text="Digite su pago por hora, porfavor")
    digite_su_pago.pack()
    pago_por_hora_guarda=Entry(ventana_Guarda, textvariable=pago_hora_guarda)
    pago_por_hora_guarda.pack()
    Button(ventana_Guarda,bg="LightCyan2",text="Hacer calculo",command=mensaje_guarda).pack()

def mensaje_guarda():
    datos_guarda=[]
    datos_guarda.append(dias_trabajados_guarda.get())
    datos_guarda.append(horas_de_trabajo_guarda.get())
    datos_guarda.append(pago_hora_guarda.get())
    if dias_trabajados_guarda.get()>7:
        messagebox.showerror("","No puede trabajar más de 7 días, la semana solo tiene 7 días")
        Guarda()
    elif horas_de_trabajo_guarda.get()>12:
        messagebox.showerror("","No puede trabajar más de 12 horas, según lo dice el Sistema Costarricense de Información Juridica")
        Guarda()
    elif dias_trabajados_guarda.get()<=7 and horas_de_trabajo_guarda.get()<=12:
        guardar_datos_guarda()

def guardar_datos_guarda():
    datos_guarda=[]
    datos_guarda.append(dias_trabajados_guarda.get())
    datos_guarda.append(horas_de_trabajo_guarda.get())
    datos_guarda.append(pago_hora_guarda.get())
    ventana_datos_guarda=Toplevel(ventana_Guarda)
    ventana_datos_guarda.title("Total")
    ventana_datos_guarda.geometry("900x700")
    ventana_datos_guarda.configure(bg="light steel blue")
    pago_dia_guarda= horas_de_trabajo_guarda.get()*pago_hora_guarda.get()
    Label(ventana_datos_guarda,bg="LightCyan2",text="Su pago por dia es:").pack()
    Label(ventana_datos_guarda, text=pago_dia_guarda).pack() 
    pago_semana_guarda= pago_dia_guarda*dias_trabajados_guarda.get()
    Label(ventana_datos_guarda,bg="LightCyan2", text="Su pago por semana:").pack()
    Label(ventana_datos_guarda, text= pago_semana_guarda).pack()
    pago_quincena_guarda=pago_semana_guarda*2
    Label(ventana_datos_guarda,bg="LightCyan2", text="Su pago quincenal:").pack()
    Label(ventana_datos_guarda, text=pago_quincena_guarda).pack()
    pago_mensual_guarda= pago_quincena_guarda*2
    Label(ventana_datos_guarda,bg="LightCyan2", text="Su pago mensual:").pack()
    Label(ventana_datos_guarda, text=pago_mensual_guarda).pack()
    porcentaje_seguro= pago_mensual_guarda * 0.05
    porcentaje_pension= pago_mensual_guarda * 0.03
    porcentaje_banco= pago_mensual_guarda * 0.01
    porcentaje_junta= pago_mensual_guarda * 0.02
    porcentaje_fondo= pago_mensual_guarda * 0.08
    salario_neto = pago_mensual_guarda-porcentaje_seguro-porcentaje_pension-porcentaje_banco-porcentaje_junta-porcentaje_fondo
    Label(ventana_datos_guarda,bg="LightCyan2", text="Su ingreso neto es de:").pack()
    Label(ventana_datos_guarda, text=salario_neto).pack()
    pago_anual=salario_neto*12
    Label(ventana_datos_guarda,bg="LightCyan2", text="Su salario anual es de:").pack()
    Label(ventana_datos_guarda, text=pago_anual).pack()
    bono_escolar=pago_anual*0.08
    Label(ventana_datos_guarda,bg="LightCyan2", text="Su bono escolar es de:").pack()
    Label(ventana_datos_guarda, text=bono_escolar).pack()
    aguinaldo=pago_anual/12
    Label(ventana_datos_guarda,bg="LightCyan2", text="Su aguinaldo es de:").pack()
    Label(ventana_datos_guarda, text=aguinaldo).pack()
    impuesto1=salario_neto*0.10
    impuesto2=salario_neto*0.15
    impuesto3=salario_neto*0.20
    impuesto4=salario_neto*0.25
    if salario_neto>840000 and salario_neto<1233000:
        salario_desp_impuesto1=salario_neto-impuesto1
        Label(ventana_datos_guarda,bg="LightCyan2", text="Su salario despues de impuestos de un 10% es de:").pack()
        Label(ventana_datos_guarda, text=salario_desp_impuesto1).pack()
    elif salario_neto>1233000 and salario_neto<2163000:
        salario_desp_impuesto2=salario_neto-impuesto2
        Label(ventana_datos_guarda,bg="LightCyan2", text="Su salario despues de impuestos de un 15% es de:").pack()
        Label(ventana_datos_guarda, text=salario_desp_impuesto2).pack()
    elif salario_neto>2163000 and salario_neto<4325000:
        salario_desp_impuesto3=salario_neto-impuesto3
        Label(ventana_datos_guarda,bg="LightCyan2", text="Su salario despues de impuestos de un 20% es de:").pack()
        Label(ventana_datos_guarda, text=salario_desp_impuesto3).pack()
    elif salario_neto>4325000:
        salario_desp_impuesto4=salario_neto-impuesto4
        Label(ventana_datos_guarda,bg="LightCyan2", text="Su salario despues de impuestos de un 25% es de:").pack()
        Label(ventana_datos_guarda, text=salario_desp_impuesto4).pack()
    elif salario_neto<840000:
        Label(ventana_datos_guarda,bg="LightCyan2", text="Su salario sin impuestos es de:").pack()
        Label(ventana_datos_guarda, text=salario_neto).pack()

def Conserje():
    global ventana_conserje
    ventana_conserje=Toplevel(ventana_salarial)
    ventana_conserje.title("Calculo salarial de conserje")
    ventana_conserje.geometry("900x700")
    global dias_trabajados_conserje
    dias_trabajados_conserje=IntVar()
    global total_hora_conserje
    total_hora_conserje=IntVar()
    global pago_hora_conserje
    pago_hora_conserje=IntVar()
    ventana_conserje.configure(bg="light steel blue")
    digite_su_dias=Label(ventana_conserje,bg="LightCyan2", text="Digite la cantidad de dias de trabajo")
    digite_su_dias.pack()
    dias_trabajo_conserje=Entry(ventana_conserje, textvariable=dias_trabajados_conserje)
    dias_trabajo_conserje.pack()
    digite_hora_trabajo=Label(ventana_conserje,bg="LightCyan2", text="Digite sus horas de trabajo diarias")
    digite_hora_trabajo.pack()
    total_por_hora_conserje=Entry(ventana_conserje,textvariable= total_hora_conserje)
    total_por_hora_conserje.pack()
    digite_pago_conserje=Label(ventana_conserje,bg="LightCyan2", text="Digite su pago por hora")
    digite_pago_conserje.pack()
    pago_por_hora_conserje=Entry(ventana_conserje,textvariable=pago_hora_conserje)
    pago_por_hora_conserje.pack()
    Button(ventana_conserje,bg="LightCyan2",text="Hacer calculo",command=mensaje_conserje).pack()

def mensaje_conserje():
    datos_conserje=[]
    datos_conserje.append(dias_trabajados_conserje.get())
    datos_conserje.append(total_hora_conserje.get())
    datos_conserje.append(pago_hora_guarda.get())
    if dias_trabajados_conserje.get()>7:
        messagebox.showerror("","No puede trabajar más de 7 días, la semana solo tiene 7 días")
        Conserje()
    elif total_hora_conserje.get()>12:
        messagebox.showerror("","No puede trabajar más de 12 horas, según lo dice el Sistema Costarricense de Información Juridica")
        Conserje()
    elif dias_trabajados_conserje.get()<=7 and total_hora_conserje.get()<=12:
        guardar_datos_conserje()

def guardar_datos_conserje():
    datos_conserje=[]
    datos_conserje.append(dias_trabajados_conserje.get())
    datos_conserje.append(total_hora_conserje.get())
    datos_conserje.append(pago_hora_conserje.get())
    ventana_datos_conserje=Toplevel(ventana_conserje)
    ventana_datos_conserje.title("Total")
    ventana_datos_conserje.geometry("900x700")
    ventana_datos_conserje.configure(bg="light steel blue")
    pago_dia_conserje= pago_hora_conserje.get()*total_hora_conserje.get()
    Label(ventana_datos_conserje,bg="LightCyan2",  text="Su pago por dia es:").pack()
    Label(ventana_datos_conserje, text=pago_dia_conserje).pack()
    pago_semana_conserje= pago_dia_conserje*dias_trabajados_conserje.get()
    Label(ventana_datos_conserje,bg="LightCyan2",  text= "Su pago semanal:").pack()
    Label(ventana_datos_conserje, text=pago_semana_conserje).pack()
    pago_quincena_conserje= pago_semana_conserje*2
    Label(ventana_datos_conserje,bg="LightCyan2",  text= "Su pago quincenal es:").pack()
    Label(ventana_datos_conserje, text=pago_quincena_conserje).pack()
    pago_mensual_conserje= pago_quincena_conserje*2
    Label(ventana_datos_conserje, bg="LightCyan2", text="Su pago mensual es").pack()
    Label(ventana_datos_conserje,text=pago_mensual_conserje).pack()
    porcentaje_seguro= pago_mensual_conserje * 0.05
    porcentaje_pension= pago_mensual_conserje * 0.03
    porcentaje_banco= pago_mensual_conserje * 0.01
    porcentaje_junta= pago_mensual_conserje * 0.02
    porcentaje_fondo= pago_mensual_conserje * 0.08
    salario_neto = pago_mensual_conserje-porcentaje_seguro-porcentaje_pension-porcentaje_banco-porcentaje_junta-porcentaje_fondo
    Label(ventana_datos_conserje,bg="LightCyan2",  text="Su ingreso neto es de:").pack()
    Label(ventana_datos_conserje, text=salario_neto).pack()
    pago_anual=salario_neto*12
    Label(ventana_datos_conserje, bg="LightCyan2", text="Su salario anual es de:").pack()
    Label(ventana_datos_conserje, text=pago_anual).pack()
    bono_escolar=pago_anual*0.08
    Label(ventana_datos_conserje,bg="LightCyan2",  text="Su bono escolar es de:").pack()
    Label(ventana_datos_conserje, text=bono_escolar).pack()
    aguinaldo=pago_anual/12
    Label(ventana_datos_conserje,bg="LightCyan2", text="Su aguinaldo es de:").pack()
    Label(ventana_datos_conserje, text=aguinaldo).pack()
    impuesto1=salario_neto*0.10
    impuesto2=salario_neto*0.15
    impuesto3=salario_neto*0.20
    impuesto4=salario_neto*0.25
    if salario_neto>840000 and salario_neto<1233000:
        salario_desp_impuesto1=salario_neto-impuesto1
        Label(ventana_datos_conserje,bg="LightCyan2",  text="Su salario despues de impuestos de un 10% es de:").pack()
        Label(ventana_datos_conserje, text=salario_desp_impuesto1).pack()
    elif salario_neto>1233000 and salario_neto<2163000:
        salario_desp_impuesto2=salario_neto-impuesto2
        Label(ventana_datos_conserje,bg="LightCyan2",  text="Su salario despues de impuestos de un 15% es de:").pack()
        Label(ventana_datos_conserje, text=salario_desp_impuesto2).pack()
    elif salario_neto>2163000 and salario_neto<4325000:
        salario_desp_impuesto3=salario_neto-impuesto3
        Label(ventana_datos_conserje,bg="LightCyan2",  text="Su salario despues de impuestos de un 20% es de:").pack()
        Label(ventana_datos_conserje, text=salario_desp_impuesto3).pack()
    elif salario_neto>4325000:
        salario_desp_impuesto4=salario_neto-impuesto4
        Label(ventana_datos_conserje,bg="LightCyan2", text="Su salario despues de impuestos de un 25% es de:").pack()
        Label(ventana_datos_conserje, text=salario_desp_impuesto4).pack()
    elif salario_neto<840000:
        Label(ventana_datos_conserje,bg="LightCyan2", text="Su salario sin impuestos es de:").pack()
        Label(ventana_datos_conserje, text=salario_neto).pack()

def Auxiliar():
    global ventana_auxiliar
    ventana_auxiliar=Toplevel(ventana_salarial)
    ventana_auxiliar.title("Calculo salarial de auxiliar")
    ventana_auxiliar.geometry("900x700")
    global dias_trabajo_auxiliar
    dias_trabajo_auxiliar=IntVar()
    global horas_trabajo_auxiliar
    horas_trabajo_auxiliar=IntVar()
    global pago_hora_auxiliar
    pago_hora_auxiliar=IntVar()
    ventana_auxiliar.configure(bg="light steel blue")
    digite_dias=Label(ventana_auxiliar,bg="LightCyan2", text="Digite sus dias de trabajo: ")
    digite_dias.pack()
    digite_dias_auxiliar=Entry(ventana_auxiliar,textvariable=dias_trabajo_auxiliar)
    digite_dias_auxiliar.pack()
    digite_hora=Label(ventana_auxiliar,bg="LightCyan2", text="Digite sus horas diarias:")
    digite_hora.pack()
    digite_hora_auxiliar=Entry(ventana_auxiliar,textvariable=horas_trabajo_auxiliar)
    digite_hora_auxiliar.pack()
    digite_pago=Label(ventana_auxiliar,bg="LightCyan2", text="Digite su pago por hora:")
    digite_pago.pack()
    digite_pago_auxiliar=Entry(ventana_auxiliar,textvariable=pago_hora_auxiliar)
    digite_pago_auxiliar.pack()
    Button(ventana_auxiliar,bg="LightCyan2",text="Hacer calculo",command=mensaje_auxiliar).pack()

def mensaje_auxiliar():
    datos_guarda=[]
    datos_guarda.append(dias_trabajo_auxiliar.get())
    datos_guarda.append(horas_trabajo_auxiliar.get())
    datos_guarda.append(pago_hora_auxiliar.get())
    if dias_trabajo_auxiliar.get()>7:
        messagebox.showerror("","No puede trabajar más de 7 días, la semana solo tiene 7 días")
        Auxiliar()
    elif horas_trabajo_auxiliar.get()>12:
        messagebox.showerror("","No puede trabajar más de 12 horas, según lo dice el Sistema Costarricense de Información Juridica")
        Auxiliar()
    elif dias_trabajo_auxiliar.get()<=7 and horas_trabajo_auxiliar.get()<=12:
        guardar_datos_auxiliar()

def guardar_datos_auxiliar():
    datos_auxiliar=[]
    datos_auxiliar.append(dias_trabajo_auxiliar.get())
    datos_auxiliar.append(horas_trabajo_auxiliar.get())
    datos_auxiliar.append(pago_hora_auxiliar.get())
    ventana_datos_auxiliar=Toplevel(ventana_auxiliar)
    ventana_datos_auxiliar.title("Total")
    ventana_datos_auxiliar.geometry("900x700")
    ventana_datos_auxiliar.configure(bg="light steel blue")
    pago_dia_auxiliar=pago_hora_auxiliar.get()*horas_trabajo_auxiliar.get()
    Label(ventana_datos_auxiliar,bg="LightCyan2", text="Su pago por dia es:").pack()
    Label(ventana_datos_auxiliar,text=pago_dia_auxiliar).pack()
    pago_semana_auxiliar= pago_dia_auxiliar*dias_trabajo_auxiliar.get()
    Label(ventana_datos_auxiliar,bg="LightCyan2", text="Su pago semanal es de:").pack()
    Label(ventana_datos_auxiliar, text= pago_semana_auxiliar).pack()
    pago_quincena_auxiliar=pago_semana_auxiliar*2
    Label(ventana_datos_auxiliar,bg="LightCyan2", text="Su pago por quincena es de:").pack()
    Label(ventana_datos_auxiliar, text=pago_quincena_auxiliar).pack()
    pago_mes_auxiliar=pago_quincena_auxiliar*2
    Label(ventana_datos_auxiliar,bg="LightCyan2", text="Su pago por mes es:").pack()
    Label(ventana_datos_auxiliar, text=pago_mes_auxiliar).pack()
    porcentaje_seguro= pago_mes_auxiliar * 0.05
    porcentaje_pension= pago_mes_auxiliar * 0.03
    porcentaje_banco= pago_mes_auxiliar * 0.01
    porcentaje_junta= pago_mes_auxiliar * 0.02
    porcentaje_fondo= pago_mes_auxiliar * 0.08
    salario_neto = pago_mes_auxiliar-porcentaje_seguro-porcentaje_pension-porcentaje_banco-porcentaje_junta-porcentaje_fondo
    Label(ventana_datos_auxiliar,bg="LightCyan2", text="Su ingreso neto es de:").pack()
    Label(ventana_datos_auxiliar, text=salario_neto).pack()
    pago_anual=salario_neto*12
    Label(ventana_datos_auxiliar,bg="LightCyan2", text="Su salario anual es de:").pack()
    Label(ventana_datos_auxiliar, text=pago_anual).pack()
    bono_escolar=pago_anual*0.08
    Label(ventana_datos_auxiliar,bg="LightCyan2", text="Su bono escolar es de:").pack()
    Label(ventana_datos_auxiliar, text=bono_escolar).pack()
    aguinaldo=pago_anual/12
    Label(ventana_datos_auxiliar,bg="LightCyan2",text="Su aguinaldo es de:").pack()
    Label(ventana_datos_auxiliar, text=aguinaldo).pack()
    impuesto1=salario_neto*0.10
    impuesto2=salario_neto*0.15
    impuesto3=salario_neto*0.20
    impuesto4=salario_neto*0.25
    if salario_neto>840000 and salario_neto<1233000:
        salario_desp_impuesto1=salario_neto-impuesto1
        Label(ventana_datos_auxiliar,bg="LightCyan2", text="Su salario despues de impuestos de un 10% es de:").pack()
        Label(ventana_datos_auxiliar, text=salario_desp_impuesto1).pack()
    elif salario_neto>1233000 and salario_neto<2163000:
        salario_desp_impuesto2=salario_neto-impuesto2
        Label(ventana_datos_auxiliar,bg="LightCyan2", text="Su salario despues de impuestos de un 15% es de:").pack()
        Label(ventana_datos_auxiliar, text=salario_desp_impuesto2).pack()
    elif salario_neto>2163000 and salario_neto<4325000:
        salario_desp_impuesto3=salario_neto-impuesto3
        Label(ventana_datos_auxiliar,bg="LightCyan2", text="Su salario despues de impuestos de un 20% es de:").pack()
        Label(ventana_datos_auxiliar, text=salario_desp_impuesto3).pack()
    elif salario_neto>4325000:
        salario_desp_impuesto4=salario_neto-impuesto4
        Label(ventana_datos_auxiliar,bg="LightCyan2", text="Su salario despues de impuestos de un 25% es de:").pack()
        Label(ventana_datos_auxiliar, text=salario_desp_impuesto4).pack()
    elif salario_neto<840000:
        Label(ventana_datos_auxiliar,bg="LightCyan2", text="Su salario sin impuestos es de:").pack()
        Label(ventana_datos_auxiliar, text=salario_neto).pack()

def Direccion():
    global ventana_direccion
    ventana_direccion=Toplevel(ventana_salarial)
    ventana_direccion.title("Calculo salarial de dirección")
    ventana_direccion.geometry("900x700")
    global dias_trabajo_direccion
    dias_trabajo_direccion=IntVar()
    global horas_trabajo_direccion
    horas_trabajo_direccion=IntVar()
    global pago_hora_direccion
    pago_hora_direccion=IntVar()
    ventana_direccion.configure(bg="light steel blue")
    digite_dia=Label(ventana_direccion, bg="LightCyan2",text="Digite sus dias de trabajo")
    digite_dia.pack()
    digite_dia_direccion=Entry(ventana_direccion,textvariable=dias_trabajo_direccion)
    digite_dia_direccion.pack()
    digite_hora=Label(ventana_direccion, bg="LightCyan2", text="Digite su total de horas de trabajo diarias:")
    digite_hora.pack()
    digite_hora_direccion=Entry(ventana_direccion,textvariable=horas_trabajo_direccion)
    digite_hora_direccion.pack()
    pago_hora=Label(ventana_direccion, bg="LightCyan2", text="Digite su pago por hora")
    pago_hora.pack()
    pago_por_hora_direccion=Entry(ventana_direccion,textvariable=pago_hora_direccion)
    pago_por_hora_direccion.pack()
    Button(ventana_direccion,bg="LightCyan2", text="Hacer calculo",command=mensaje_direccion).pack()

def mensaje_direccion():
    datos_direccion=[]
    datos_direccion.append(dias_trabajo_direccion.get())
    datos_direccion.append(horas_trabajo_direccion.get())
    datos_direccion.append(pago_hora_direccion.get())
    if dias_trabajo_direccion.get()>7:
        messagebox.showerror("","No puede trabajar más de 7 días, la semana solo tiene 7 días")
        Direccion()
    elif horas_trabajo_direccion.get()>12:
        messagebox.showerror("","No puede trabajar más de 12 horas, según lo dice el Sistema Costarricense de Información Juridica")
        Direccion()
    elif dias_trabajo_direccion.get()<=7 and horas_trabajo_direccion.get()<=12:
        guardar_datos_Direccion()

def guardar_datos_Direccion():
    datos_direccion=[]
    datos_direccion.append(dias_trabajo_direccion.get())
    datos_direccion.append(horas_trabajo_direccion.get())
    datos_direccion.append(pago_hora_direccion.get())
    ventana_datos_direccion=Toplevel(ventana_direccion)
    ventana_datos_direccion.title("Calculo salarial de auxiliar")
    ventana_datos_direccion.geometry("900x700")
    ventana_datos_direccion.configure(bg="light steel blue")
    pago_dia_direccion=horas_trabajo_direccion.get()*pago_hora_direccion.get()
    Label(ventana_datos_direccion, bg="LightCyan2", text="Su pago por dia es de:").pack()
    Label(ventana_datos_direccion, text=pago_dia_direccion).pack()
    pago_semana_direccion=pago_dia_direccion*dias_trabajo_direccion.get()
    Label(ventana_datos_direccion, bg="LightCyan2", text="Su pago semanal es de:").pack()
    Label(ventana_datos_direccion,text=pago_semana_direccion).pack()
    pago_quiencena_direccion=pago_semana_direccion*2
    Label(ventana_datos_direccion, bg="LightCyan2", text="Su oago por quiencena es de:").pack()
    Label(ventana_datos_direccion,text=pago_quiencena_direccion).pack()
    pagp_mes_direccion=pago_quiencena_direccion*2
    Label(ventana_datos_direccion, bg="LightCyan2", text="Su pago mensual es de: ").pack()
    Label(ventana_datos_direccion,text=pagp_mes_direccion).pack()
    porcentaje_seguro= pagp_mes_direccion * 0.05
    porcentaje_pension= pagp_mes_direccion * 0.03
    porcentaje_banco= pagp_mes_direccion * 0.01
    porcentaje_junta= pagp_mes_direccion * 0.02
    porcentaje_fondo= pagp_mes_direccion * 0.08
    salario_neto = pagp_mes_direccion-porcentaje_seguro-porcentaje_pension-porcentaje_banco-porcentaje_junta-porcentaje_fondo
    Label(ventana_datos_direccion, bg="LightCyan2", text="Su ingreso neto es de:").pack()
    Label(ventana_datos_direccion, text=salario_neto).pack()
    pago_anual=salario_neto*12
    Label(ventana_datos_direccion, bg="LightCyan2", text="Su salario anual es de:").pack()
    Label(ventana_datos_direccion, text=pago_anual).pack()
    bono_escolar=pago_anual*0.08
    Label(ventana_datos_direccion, bg="LightCyan2", text="Su bono escolar es de:").pack()
    Label(ventana_datos_direccion, text=bono_escolar).pack()
    aguinaldo=pago_anual/12
    Label(ventana_datos_direccion, bg="LightCyan2", text="Su aguinaldo es de:").pack()
    Label(ventana_datos_direccion, text=aguinaldo).pack()
    impuesto1=salario_neto*0.10
    impuesto2=salario_neto*0.15
    impuesto3=salario_neto*0.20
    impuesto4=salario_neto*0.25
    if salario_neto>840000 and salario_neto<1233000:
        salario_desp_impuesto1=salario_neto-impuesto1
        Label(ventana_datos_direccion, bg="LightCyan2", text="Su salario despues de impuestos de un 10% es de:").pack()
        Label(ventana_datos_direccion, text=salario_desp_impuesto1).pack()
    elif salario_neto>1233000 and salario_neto<2163000:
        salario_desp_impuesto2=salario_neto-impuesto2
        Label(ventana_datos_direccion, bg="LightCyan2", text="Su salario despues de impuestos de un 15% es de:").pack()
        Label(ventana_datos_direccion, text=salario_desp_impuesto2).pack()
    elif salario_neto>2163000 and salario_neto<4325000:
        salario_desp_impuesto3=salario_neto-impuesto3
        Label(ventana_datos_direccion, bg="LightCyan2", text="Su salario despues de impuestos de un 20% es de:").pack()
        Label(ventana_datos_direccion, text=salario_desp_impuesto3).pack()
    elif salario_neto>4325000:
        salario_desp_impuesto4=salario_neto-impuesto4
        Label(ventana_datos_direccion, bg="LightCyan2", text="Su salario despues de impuestos de un 25% es de:").pack()
        Label(ventana_datos_direccion, text=salario_desp_impuesto4).pack()
    elif salario_neto<840000:
        Label(ventana_datos_direccion, bg="LightCyan2", text="Su salario sin impuestos es de:").pack()
        Label(ventana_datos_direccion, text=salario_neto).pack()

def Cocinero():
    global ventana_cocinero
    ventana_cocinero=Toplevel(ventana_salarial)
    ventana_cocinero.title("Calculo salarial de cocinero")
    ventana_cocinero.geometry("900x700")
    global dias_trabajo_cocinero
    dias_trabajo_cocinero=IntVar()
    global horas_dia_cocinero
    horas_dia_cocinero=IntVar()
    global pago_hora_cocinero
    pago_hora_cocinero=IntVar()
    ventana_cocinero.configure(bg="light steel blue")
    digite_dias=Label(ventana_cocinero,bg="LightCyan2", text="Digite sus dias de trabajo")
    digite_dias.pack()
    digite_dias_cocinero=Entry(ventana_cocinero,textvariable=dias_trabajo_cocinero)
    digite_dias_cocinero.pack()
    digite_horas=Label(ventana_cocinero,bg="LightCyan2", text="Digite su horas de trabajo diarias")
    digite_horas.pack()
    digite_horas_cocinero=Entry(ventana_cocinero,textvariable=horas_dia_cocinero)
    digite_horas_cocinero.pack()
    digite_pago=Label(ventana_cocinero,bg="LightCyan2", text="indique su pago por hora")
    digite_pago.pack()
    digite_pago_cocinero=Entry(ventana_cocinero,textvariable=pago_hora_cocinero)
    digite_pago_cocinero.pack()
    Button(ventana_cocinero,bg="LightCyan2", text="Hacer calculo",command=mensaje_cocinero).pack()

def mensaje_cocinero():
    datos_guarda=[]
    datos_guarda.append(dias_trabajo_cocinero.get())
    datos_guarda.append(horas_dia_cocinero.get())
    datos_guarda.append(pago_hora_cocinero.get())
    if dias_trabajo_cocinero.get()>7:
        messagebox.showerror("","No puede trabajar más de 7 días, la semana solo tiene 7 días")
        Cocinero()
    elif horas_dia_cocinero.get()>12:
        messagebox.showerror("","No puede trabajar más de 12 horas, según lo dice el Sistema Costarricense de Información Juridica")
        Cocinero()
    elif dias_trabajo_cocinero.get()<=7 and horas_dia_cocinero.get()<=12:
        guardar_datos_Cocinero()

def guardar_datos_Cocinero():
    datos_cocinero=[]
    datos_cocinero.append(dias_trabajo_cocinero.get())
    datos_cocinero.append(horas_dia_cocinero.get())
    datos_cocinero.append(pago_hora_cocinero.get())
    ventana_datos_cocinero=Toplevel(ventana_cocinero)
    ventana_datos_cocinero.title("Total")
    ventana_datos_cocinero.geometry("900x700")
    ventana_datos_cocinero.configure(bg="light steel blue")
    pago_dia_cocinero=horas_dia_cocinero.get()*pago_hora_cocinero.get()
    Label(ventana_datos_cocinero,bg="LightCyan2", text=("Su pago por dia es:")).pack()
    Label(ventana_datos_cocinero,text=pago_dia_cocinero).pack()
    pago_semana_cocinero=pago_dia_cocinero*dias_trabajo_cocinero.get()
    Label(ventana_datos_cocinero,bg="LightCyan2", text="Su pago semanal es de:").pack()
    Label(ventana_datos_cocinero,text=pago_semana_cocinero).pack()
    pago_quincena_cocinero=pago_semana_cocinero*2
    Label(ventana_datos_cocinero,bg="LightCyan2", text="Su pago por quincena es de:").pack()
    Label(ventana_datos_cocinero,text=pago_quincena_cocinero).pack()
    pago_mes_cocinero=pago_quincena_cocinero*2
    Label(ventana_datos_cocinero,bg="LightCyan2",text="Su pago mensual es de:").pack()
    Label(ventana_datos_cocinero,text=pago_mes_cocinero).pack()
    porcentaje_seguro= pago_mes_cocinero * 0.05
    porcentaje_pension= pago_mes_cocinero * 0.03
    porcentaje_banco= pago_mes_cocinero * 0.01
    porcentaje_junta= pago_mes_cocinero * 0.02
    porcentaje_fondo= pago_mes_cocinero * 0.08
    salario_neto = pago_mes_cocinero-porcentaje_seguro-porcentaje_pension-porcentaje_banco-porcentaje_junta-porcentaje_fondo
    Label(ventana_datos_cocinero,bg="LightCyan2",  text="Su ingreso neto es de:").pack()
    Label(ventana_datos_cocinero, text=salario_neto).pack()
    pago_anual=salario_neto*12
    Label(ventana_datos_cocinero,bg="LightCyan2",  text="Su salario anual es de:").pack()
    Label(ventana_datos_cocinero, text=pago_anual).pack()
    bono_escolar=pago_anual*0.08
    Label(ventana_datos_cocinero,bg="LightCyan2",  text="Su bono escolar es de:").pack()
    Label(ventana_datos_cocinero, text=bono_escolar).pack()
    aguinaldo=pago_anual/12
    Label(ventana_datos_cocinero,bg="LightCyan2", text="Su aguinaldo es de:").pack()
    Label(ventana_datos_cocinero, text=aguinaldo).pack()
    impuesto1=salario_neto*0.10
    impuesto2=salario_neto*0.15
    impuesto3=salario_neto*0.20
    impuesto4=salario_neto*0.25
    if salario_neto>840000 and salario_neto<1233000:
        salario_desp_impuesto1=salario_neto-impuesto1
        Label(ventana_datos_cocinero, bg="LightCyan2", text="Su salario despues de impuestos de un 10% es de:").pack()
        Label(ventana_datos_cocinero, text=salario_desp_impuesto1).pack()
    elif salario_neto>1233000 and salario_neto<2163000:
        salario_desp_impuesto2=salario_neto-impuesto2
        Label(ventana_datos_cocinero, bg="LightCyan2", text="Su salario despues de impuestos de un 15% es de:").pack()
        Label(ventana_datos_cocinero, text=salario_desp_impuesto2).pack()
    elif salario_neto>2163000 and salario_neto<4325000:
        salario_desp_impuesto3=salario_neto-impuesto3
        Label(ventana_datos_cocinero, bg="LightCyan2", text="Su salario despues de impuestos de un 20% es de:").pack()
        Label(ventana_datos_cocinero, text=salario_desp_impuesto3).pack()
    elif salario_neto>4325000:
        salario_desp_impuesto4=salario_neto-impuesto4
        Label(ventana_datos_cocinero, bg="LightCyan2", text="Su salario despues de impuestos de un 25% es de:").pack()
        Label(ventana_datos_cocinero, text=salario_desp_impuesto4).pack()
    elif salario_neto<840000:
        Label(ventana_datos_cocinero, bg="LightCyan2", text="Su salario sin impuestos es de:").pack()
        Label(ventana_datos_cocinero, text=salario_neto).pack()

def Orientador():
    global ventana_orientador
    ventana_orientador=Toplevel(ventana_salarial)
    ventana_orientador.title("Calculo salarial de orientador")
    ventana_orientador.geometry("900x700")
    global dias_orientador
    dias_orientador=IntVar()
    global horas_orientador
    horas_orientador=IntVar()
    global pago_horas_orientador
    pago_horas_orientador=IntVar()
    ventana_orientador.configure(bg="light steel blue")
    digite_dia=Label(ventana_orientador,bg="LightCyan2", text="Digite sus dias laborales")
    digite_dia.pack()
    digite_dia_orientador=Entry(ventana_orientador,textvariable=dias_orientador)
    digite_dia_orientador.pack()
    digite_hora=Label(ventana_orientador,bg="LightCyan2",text="Digite sus horas laboradas")
    digite_hora.pack()
    digite_hora_orientador=Entry(ventana_orientador,textvariable=horas_orientador)
    digite_hora_orientador.pack()
    digite_pago_hora=Label(ventana_orientador,bg="LightCyan2",text="Digite su pago por hora")
    digite_pago_hora.pack()
    pago_hora_orientador=Entry(ventana_orientador,textvariable=pago_horas_orientador)
    pago_hora_orientador.pack()
    Button(ventana_orientador,bg="LightCyan2",text="Hacer calculo",command=mensaje_orientador).pack()

def mensaje_orientador():
    datos_guarda=[]
    datos_guarda.append(dias_orientador.get())
    datos_guarda.append(horas_orientador.get())
    datos_guarda.append(pago_horas_orientador.get())
    if dias_orientador.get()>7:
        messagebox.showerror("","No puede trabajar más de 7 días, la semana solo tiene 7 días")
        Orientador()
    elif horas_orientador.get()>12:
        messagebox.showerror("","No puede trabajar más de 12 horas, según lo dice el Sistema Costarricense de Información Juridica")
        Orientador()
    elif dias_orientador.get()<=7 and horas_orientador.get()<=12:
        guardar_datos_Orientador()

def guardar_datos_Orientador():
    datos_orientador=[]
    datos_orientador.append(dias_orientador.get())
    datos_orientador.append(horas_orientador.get())
    datos_orientador.append(pago_horas_orientador.get())
    ventana_datos_orientador=Toplevel(ventana_orientador)
    ventana_datos_orientador.title("Total")
    ventana_datos_orientador.geometry("900x700")
    ventana_datos_orientador.configure(bg="light steel blue")
    pago_dia_orientador= horas_orientador.get()*pago_horas_orientador.get()
    Label(ventana_datos_orientador,bg="LightCyan2",text="Su pago al dia es de:").pack()
    Label(ventana_datos_orientador,text=pago_dia_orientador).pack()
    pago_semana_orienatdor= pago_dia_orientador*dias_orientador.get() 
    Label(ventana_datos_orientador,bg="LightCyan2", text="Su pago semanal es de:").pack()
    Label(ventana_datos_orientador,text=pago_semana_orienatdor).pack()
    pago_quincena_orientador=pago_semana_orienatdor*2
    Label(ventana_datos_orientador,bg="LightCyan2", text="Su pago por quincena:").pack()
    Label(ventana_datos_orientador,text=pago_quincena_orientador).pack()
    pago_mensual_orientador=pago_quincena_orientador*2
    Label(ventana_datos_orientador,bg="LightCyan2", text="Su pago mensual es de:").pack()
    Label(ventana_datos_orientador,text=pago_mensual_orientador).pack()
    porcentaje_seguro= pago_mensual_orientador * 0.05
    porcentaje_pension= pago_mensual_orientador * 0.03
    porcentaje_banco= pago_mensual_orientador * 0.01
    porcentaje_junta= pago_mensual_orientador * 0.02
    porcentaje_fondo= pago_mensual_orientador * 0.08
    salario_neto = pago_mensual_orientador-porcentaje_seguro-porcentaje_pension-porcentaje_banco-porcentaje_junta-porcentaje_fondo
    Label(ventana_datos_orientador,bg="LightCyan2", text="Su ingreso neto es de:").pack()
    Label(ventana_datos_orientador, text=salario_neto).pack()
    pago_anual=salario_neto*12
    Label(ventana_datos_orientador,bg="LightCyan2", text="Su salario anual es de:").pack()
    Label(ventana_datos_orientador, text=pago_anual).pack()
    bono_escolar=pago_anual*0.08
    Label(ventana_datos_orientador,bg="LightCyan2", text="Su bono escolar es de:").pack()
    Label(ventana_datos_orientador, text=bono_escolar).pack()
    aguinaldo=pago_anual/12
    Label(ventana_datos_orientador,bg="LightCyan2", text="Su aguinaldo es de:").pack()
    Label(ventana_datos_orientador, text=aguinaldo).pack()
    impuesto1=salario_neto*0.10
    impuesto2=salario_neto*0.15
    impuesto3=salario_neto*0.20
    impuesto4=salario_neto*0.25
    if salario_neto>840000 and salario_neto<1233000:
        salario_desp_impuesto1=salario_neto-impuesto1
        Label(ventana_datos_orientador,bg="LightCyan2", text="Su salario despues de impuestos de un 10% es de:").pack()
        Label(ventana_datos_orientador, text=salario_desp_impuesto1).pack()
    elif salario_neto>1233000 and salario_neto<2163000:
        salario_desp_impuesto2=salario_neto-impuesto2
        Label(ventana_datos_orientador,bg="LightCyan2", text="Su salario despues de impuestos de un 15% es de:").pack()
        Label(ventana_datos_orientador, text=salario_desp_impuesto2).pack()
    elif salario_neto>2163000 and salario_neto<4325000:
        salario_desp_impuesto3=salario_neto-impuesto3
        Label(ventana_datos_orientador,bg="LightCyan2", text="Su salario despues de impuestos de un 20% es de:").pack()
        Label(ventana_datos_orientador, text=salario_desp_impuesto3).pack()
    elif salario_neto>4325000:
        salario_desp_impuesto4=salario_neto-impuesto4
        Label(ventana_datos_orientador,bg="LightCyan2", text="Su salario despues de impuestos de un 25% es de:").pack()
        Label(ventana_datos_orientador, text=salario_desp_impuesto4).pack()
    elif salario_neto<840000:
        Label(ventana_datos_orientador,bg="LightCyan2", text="Su salario sin impuestos es de:").pack()
        Label(ventana_datos_orientador, text=salario_neto).pack()
   
def calculo_de_gastos():
    global ventana_calculo
    ventana_calculo=Toplevel(ventana1)
    ventana_calculo.title("Calculo de gastos")
    ventana_calculo.geometry("900x700")
    ventana_calculo.configure(bg="light steel blue")
    global pago_luz
    pago_luz=IntVar()
    global pago_agua
    pago_agua=IntVar()
    global pago_telefono
    pago_telefono=IntVar()
    global pago_transporte
    pago_transporte=IntVar()
    global pago_cable
    pago_cable=IntVar()
    global pago_internet
    pago_internet=IntVar()
    global pago_alquiler_hipoteca
    pago_alquiler_hipoteca=IntVar()
    global pago_pension
    pago_pension=IntVar()
    global pago_diario
    pago_diario=IntVar()
    global salario_total
    salario_total=IntVar()
    Label(ventana_calculo,bg="LightCyan2", text="Digite su salario").pack()
    salario=Entry(ventana_calculo, textvariable=salario_total).pack()
    Label(ventana_calculo,bg="LightCyan2", text="Cual es su pago de luz¿?").pack()
    luz=Entry(ventana_calculo, textvariable=pago_luz).pack()
    Label(ventana_calculo,bg="LightCyan2", text="Cual es su pago de agua¿?").pack()
    agua=Entry(ventana_calculo, textvariable=pago_agua).pack()
    Label(ventana_calculo, bg="LightCyan2", text="Cual es su pago de telefono¿?").pack()
    telefono=Entry(ventana_calculo, textvariable=pago_telefono).pack()
    Label(ventana_calculo, bg="LightCyan2", text="Cual es su pago de transporte¿?").pack()
    transporte=Entry(ventana_calculo, textvariable=pago_transporte).pack()
    Label(ventana_calculo, bg="LightCyan2", text="Cuanto paga de alquiler/hipoteca¿?").pack()
    alquiler=Entry(ventana_calculo,textvariable=pago_alquiler_hipoteca).pack()
    Label(ventana_calculo,bg="LightCyan2", text="Cuanto paga aproximadamente de diario¿?").pack()
    diario=Entry(ventana_calculo,textvariable=pago_diario).pack()
    Label(ventana_calculo,bg="LightCyan2", text="Usted paga televisión por cable¿?").pack()
    Label(ventana_calculo,bg="LightCyan2", text="En caso de no pagar, deje el monto en 0").pack()
    cable=Entry(ventana_calculo, textvariable=pago_cable).pack()
    Label(ventana_calculo, bg="LightCyan2", text="Usted paga internet¿?").pack()
    Label(ventana_calculo,bg="LightCyan2", text="En caso de no pagar, deje el monto en 0").pack()
    internet=Entry(ventana_calculo,textvariable=pago_internet).pack()
    Label(ventana_calculo,bg="LightCyan2", text="Usted paga pension¿?").pack()
    Label(ventana_calculo,bg="LightCyan2", text="En caso de no pagar, deje el monto en 0").pack()
    pension=Entry(ventana_calculo,textvariable=pago_pension).pack()
    Button(ventana_calculo, bg="LightCyan2", text="Hacer calculo",command=guardar_datos_calculo).pack()

def guardar_datos_calculo ():
    datos_calculo=[]
    datos_calculo.append(salario_total.get())
    datos_calculo.append(pago_luz.get())
    datos_calculo.append(pago_agua.get())
    datos_calculo.append(pago_telefono.get())
    datos_calculo.append(pago_transporte.get())
    datos_calculo.append(pago_cable.get())
    datos_calculo.append(pago_alquiler_hipoteca.get())
    datos_calculo.append(pago_diario.get())
    datos_calculo.append(pago_internet.get())
    datos_calculo.append(pago_pension.get())
    gastos_total=pago_luz.get()+pago_agua.get()+pago_telefono.get()+pago_transporte.get()+pago_cable.get()+pago_alquiler_hipoteca.get()+pago_diario.get()+pago_internet.get()+pago_pension.get()
    neto=salario_total.get()-gastos_total
    ventana_calculada=Toplevel(ventana_calculo)
    ventana_calculada.title("Total")
    ventana_calculada.geometry("900x700")
    ventana_calculada.configure(bg="light steel blue")
    Label(ventana_calculada,bg="LightCyan2", text="Su total de gastos es de:").pack()
    Label(ventana_calculada, text=gastos_total).pack()
    Label(ventana_calculada,bg="LightCyan2", text="Su salario libre es de:").pack()
    Label(ventana_calculada, text=neto).pack()

inicio()