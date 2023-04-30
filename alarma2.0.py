import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class Alarm:
    def __init__(self, name, time, days):
        self.name = name
        self.time = time
        self.days = days
        self.enabled = True

    def __str__(self):
        return f"{self.name} - {self.time.strftime('%I:%M %p')}"

class AlarmApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Alarma App")
        self.alarms = []

        self.name_label = tk.Label(master, text="Nombre:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.time_label = tk.Label(master, text="Hora (HH:MM AM/PM):")
        self.time_label.grid(row=1, column=0)
        self.time_entry = tk.Entry(master)
        self.time_entry.grid(row=1, column=1)

        self.days_label = tk.Label(master, text="Días:")
        self.days_label.grid(row=2, column=0)
        self.days_var = tk.StringVar(value="L,M,X,J,V,S,D")
        self.days_entry = tk.Entry(master, textvariable=self.days_var)
        self.days_entry.grid(row=2, column=1)

        self.add_button = tk.Button(master, text="Agregar Alarma", command=self.add_alarm)
        self.add_button.grid(row=3, column=0)

        self.alarm_listbox = tk.Listbox(master, selectmode="single")
        self.alarm_listbox.grid(row=4, column=0, columnspan=2)

        self.enable_button = tk.Button(master, text="Activar/Desactivar Alarma", command=self.enable_alarm)
        self.enable_button.grid(row=5, column=0)

        self.edit_button = tk.Button(master, text="Editar Alarma", command=self.edit_alarm)
        self.edit_button.grid(row=5, column=1)

        self.delete_button = tk.Button(master, text="Eliminar Alarma", command=self.delete_alarm)
        self.delete_button.grid(row=6, column=0)

        self.update_alarm_listbox()

    def add_alarm(self):
        name = self.name_entry.get()
        time_str = self.time_entry.get()
        days_str = self.days_var.get()

        try:
            time = datetime.strptime(time_str, "%I:%M %p")
        except ValueError:
            messagebox.showerror("Error", "Formato de hora inválido")
            return

        days = days_str.split(",")
        days = [day.strip()[:3].lower() for day in days]

        alarm = Alarm(name, time, days)
        self.alarms.append(alarm)
        self.update_alarm_listbox()

    def enable_alarm(self):
        selected_index = self.alarm_listbox.curselection()
        if len(selected_index) == 0:
            return

        alarm = self.alarms[selected_index[0]]
        alarm.enabled = not alarm.enabled
        self.update_alarm_listbox()

    def edit_alarm(self):
        selected_index = self.alarm_listbox.curselection()
        if len(selected_index) == 0:
            return

        alarm = self.alarms[selected_index[0]]
        edit_window = EditAlarmWindow(self.master, alarm)
        self.master.wait_window(edit_window.top)
        self.update_alarm_listbox()

    def delete_alarm(self):
        selected_index = self.alarm_listbox.curselection()
        if len(selected_index) == 0:
            return

        alarm = self.alarms[selected_index[0]]
        self.alarms.remove(alarm)
        self.update_alarm_listbox()

    def update_alarm_listbox(self):
        self.alarm_listbox.delete(0, tk.END)
        for alarm in self.alarms:
            self.alarm_listbox.insert(tk.END, str(alarm))

    def check_alarms(self):
        now = datetime.now()

        for alarm in self.alarms:
            if alarm.enabled and now.strftime("%a").lower() in alarm.days and now.time() == alarm.time.time():
                messagebox.showinfo("Alarma", f"¡{alarm.name} ha sonado!")

        self.master.after(1000 * 60, self.check_alarms)

class EditAlarmWindow:
    def __init__(self, master, alarm):
        self.top = tk.Toplevel(master)
        self.top.title("Editar Alarma")

        self.alarm = alarm

        self.name_label = tk.Label(self.top, text="Nombre:")
        self.name_label.grid(row=0, column=0)
        self.name_var = tk.StringVar(value=alarm.name)
        self.name_entry = tk.Entry(self.top, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1)

        self.time_label = tk.Label(self.top, text="Hora (HH:MM AM/PM):")
        self.time_label.grid(row=1, column=0)
        self.time_var = tk.StringVar(value=alarm.time.strftime("%I:%M %p"))
        self.time_entry = tk.Entry(self.top, textvariable=self.time_var)
        self.time_entry.grid(row=1, column=1)

        self.days_label = tk.Label(self.top, text="Días:")
        self.days_label.grid(row=2, column=0)
        self.days_var = tk.StringVar(value=", ".join(alarm.days))
        self.days_entry = tk.Entry(self.top, textvariable=self.days_var)
        self.days_entry.grid(row=2, column=1)

        self.save_button = tk.Button(self.top, text="Guardar", command=self.save_alarm)
        self.save_button.grid(row=3, column=0)

        self.cancel_button = tk.Button(self.top, text="Cancelar", command=self.top.destroy)
        self.cancel_button.grid(row=3, column=1)

    def save_alarm(self):
        self.alarm.name = self.name_var.get()
        time_str = self.time_var.get()
        days_str = self.days_var.get()

        try:
            time = datetime.strptime(time_str, "%I:%M %p")
        except ValueError:
            messagebox.showerror("Error", "Formato de hora inválido")
            return
        
        days = days_str.split(",")
        days = [d.strip().lower() for d in days]

        self.alarm.time = time.time()
        self.alarm.days = days
        self.parent.update_alarms_listbox()
        self.top.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmApp(root)
    app.check_alarms()
    root.mainloop()
