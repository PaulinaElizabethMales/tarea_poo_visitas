import tkinter as tk
from tkinter import ttk, messagebox

class VisitaApp:
    def __init__(self, root, servicio):
        self.servicio = servicio
        self.root = root
        self.root.title("Sistema de Registro de Visitantes")

        # Validadores
        vcmd_cedula = (root.register(self.validar_cedula), "%P")
        vcmd_nombre = (root.register(self.validar_nombre), "%P")

        # Campo Cédula
        tk.Label(root, text="Cédula:").grid(row=0, column=0)
        self.cedula_entry = tk.Entry(root, validate="key", validatecommand=vcmd_cedula)
        self.cedula_entry.grid(row=0, column=1)

        # Campo Nombre
        tk.Label(root, text="Nombre:").grid(row=1, column=0)
        self.nombre_entry = tk.Entry(root, validate="key", validatecommand=vcmd_nombre)
        self.nombre_entry.grid(row=1, column=1)

        tk.Label(root, text="Motivo:").grid(row=2, column=0)
        self.motivo_entry = tk.Entry(root)
        self.motivo_entry.grid(row=2, column=1)

        # Botones
        tk.Button(root, text="Registrar", command=self.registrar).grid(row=3, column=0)
        tk.Button(root, text="Eliminar", command=self.eliminar).grid(row=3, column=1)
        tk.Button(root, text="Limpiar", command=self.limpiar_campos).grid(row=3, column=2)

        # Tabla
        self.tree = ttk.Treeview(root, columns=("Cédula", "Nombre", "Motivo"), show="headings")
        self.tree.heading("Cédula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Motivo", text="Motivo")
        self.tree.grid(row=4, column=0, columnspan=3)

    def registrar(self):
        cedula = self.cedula_entry.get()
        nombre = self.nombre_entry.get()
        motivo = self.motivo_entry.get()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        if not cedula.isdigit():
            messagebox.showwarning("Error", "La cédula debe contener solo números")
            return

        if not nombre.replace(" ", "").isalpha():
            messagebox.showwarning("Error", "El nombre debe contener solo letras")
            return

        if self.servicio.agregar_visitante(cedula, nombre, motivo):
            messagebox.showinfo("Éxito", "Visitante registrado correctamente")
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Ya existe un visitante con esa cédula")

    def eliminar(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un visitante para eliminar")
            return

        cedula = str(self.tree.item(seleccionado[0])["values"][0])  # forzar string
        if self.servicio.eliminar_visitante(cedula):
            messagebox.showinfo("Éxito", "Visitante eliminado correctamente")
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el visitante")

    def limpiar_campos(self):
        self.cedula_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.motivo_entry.delete(0, tk.END)

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for v in self.servicio.listar_visitantes():
            self.tree.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))

    def validar_cedula(self, texto):
        # Permitir solo números
        return texto.isdigit() or texto == ""

    def validar_nombre(self, texto):
        # Permitir solo letras y espacios
        return texto.replace(" ", "").isalpha() or texto == ""