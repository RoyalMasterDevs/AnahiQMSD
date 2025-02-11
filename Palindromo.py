import customtkinter as ctk  # Importamos la librería customTkinter para crear una interfaz gráfica moderna
import unicodedata  # Importamos unicodedata para manejar la eliminación de tildes

# Función para verificar si una frase es un palíndromo
def es_palindromo(frase):
    # Subfunción que elimina las tildes de un texto
    def eliminar_tildes(texto):
        # Normaliza los caracteres para separar letras y tildes, luego elimina las tildes
        return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

    frase = eliminar_tildes(frase.lower())  # Convertimos a minúsculas y eliminamos tildes
    frase = ''.join(c for c in frase if c.isalnum())  # Eliminamos espacios y caracteres no alfanuméricos
    return frase == frase[::-1]  # Comparamos la frase con su reversa

# Función para manejar el evento del botón "Verificar"
def verificar_palindromo():
    frase = entrada.get()  # Obtenemos el texto ingresado por el usuario en el campo de entrada
    if es_palindromo(frase):  # Llamamos a la función para verificar si es un palíndromo
        # Si es un palíndromo, mostramos un mensaje positivo en color verde
        resultado_label.configure(text="✅ Es un palíndromo", fg_color="green")
    else:
        # Si no es un palíndromo, mostramos un mensaje negativo en color rojo
        resultado_label.configure(text="❌ No es un palíndromo", fg_color="red")

# Configuración de la ventana principal
ctk.set_appearance_mode("dark")  # Configuramos el modo oscuro de la ventana
ctk.set_default_color_theme("blue")  # Aplicamos un tema azul por defecto

ventana = ctk.CTk()  # Creamos la ventana principal de la aplicación
ventana.title("Verificador de Palíndromos")  # Establecemos el título de la ventana
ventana.geometry("400x300")  # Definimos el tamaño de la ventana

# Etiqueta de título
titulo_label = ctk.CTkLabel(
    ventana, text="Verificador de Palíndromos", font=("Arial", 20, "bold")
)  # Creamos una etiqueta con el título principal
titulo_label.pack(pady=20)  # Empaquetamos la etiqueta con un margen superior de 20 píxeles

# Campo de entrada
entrada = ctk.CTkEntry(
    ventana, placeholder_text="Introduce una frase o palabra", width=300, font=("Arial", 14)
)  # Creamos un campo de entrada con un texto de sugerencia
entrada.pack(pady=10)  # Empaquetamos el campo de entrada con un margen superior de 10 píxeles

# Botón para verificar
verificar_boton = ctk.CTkButton(
    ventana, text="Verificar", command=verificar_palindromo, font=("Arial", 14)
)  # Creamos un botón que llama a la función 'verificar_palindromo' al hacer clic
verificar_boton.pack(pady=10)  # Empaquetamos el botón con un margen superior de 10 píxeles

# Etiqueta para mostrar el resultado
resultado_label = ctk.CTkLabel(
    ventana, text="", font=("Arial", 16)
)  # Creamos una etiqueta vacía para mostrar los resultados
resultado_label.pack(pady=20)  # Empaquetamos la etiqueta con un margen superior de 20 píxeles

# Ejecutar la aplicación
ventana.mainloop()  # Inicia el bucle principal de la interfaz gráfica
