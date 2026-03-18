
import tkinter as tk
from servicios.visita_servicios import VisitaServicios
from ui.app_tkinter import VisitaApp

if __name__ == "__main__":
    root = tk.Tk()
    servicio = VisitaServicios()
    app = VisitaApp(root, servicio)
    root.mainloop()
