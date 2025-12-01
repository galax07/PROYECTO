from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window     # Para controlar tamaño/propiedades de la ventana REPASO

# Clase de la primera pantalla
class Fondo1(Screen):
    pass

# Clase de la segunda pantalla
class Fondo2(Screen):
    pass

# Clase de la segunda pantalla
class Fondo3(Screen):
    pass

# Clase de la segunda pantalla
class Fondo4(Screen):
    pass

# Clase de la segunda pantalla
class Fondo5(Screen):
    pass

# Clase de la segunda pantalla
class Fondo6(Screen):
    pass

# Clase de la segunda pantalla
class Fondo7(Screen):
    pass

# Clase de la segunda pantalla
class Fondo8(Screen):
    pass

# Clase de la segunda pantalla
class Fondo9(Screen):
    pass

# Clase de la segunda pantalla
class Fondo10(Screen):
    pass

# Clase de la segunda pantalla
class Fondo11(Screen):
    pass

# Clase de la segunda pantalla
class Fondo12(Screen):
    pass

# Clase de la segunda pantalla
class Fondo13(Screen):
    pass

# Clase de la segunda pantalla
class Fondo14(Screen):
    pass

# Clase de la segunda pantalla
class Fondo15(Screen):
    pass

# Administrador de pantallas
class Pantallas(ScreenManager):
    pass

# Clase principal de la app
class PROYECTOApp(App):
    def build(self):
        return Pantallas()

# Ejecutar la aplicación
if __name__ == "__main__":
    Window.size = (500, 650) 
    PROYECTOApp().run()
