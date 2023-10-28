# Diccionario de elementos
elementos = {
    "header": {
        "espanol": "Encabezado",
        "ingles": "Header",
        "portugues": "Cabeçalho"
    },
    "nav": {
        "espanol": "Barra de Navegación",
        "ingles": "Navigation Bar",
        "portugues": "Barra de Navegação"
    },
    "main": {
        "espanol": "Contenido Principal",
        "ingles": "Main Content",
        "portugues": "Conteúdo Principal"
    },
    "aside": {
        "espanol": "Barra Lateral",
        "ingles": "Sidebar",
        "portugues": "Barra Lateral"
    },
    "footer": {
        "espanol": "Pie de Página",
        "ingles": "Footer",
        "portugues": "Rodapé"
    },
    "a": {
        "espanol": "Enlaces",
        "ingles": "Links",
        "portugues": "Links"
    },
    "img": {
        "espanol": "Imágenes",
        "ingles": "Images",
        "portugues": "Imagens"
    },
    "ul": {
        "espanol": "Listas no ordenadas",
        "ingles": "Unordered Lists",
        "portugues": "Listas não ordenadas"
    },
    "ol": {
        "espanol": "Listas ordenadas",
        "ingles": "Ordered Lists",
        "portugues": "Listas ordenadas"
    },
    "li": {
        "espanol": "Elementos de Lista",
        "ingles": "List Items",
        "portugues": "Itens de Lista"
    },
    "form": {
        "espanol": "Formularios",
        "ingles": "Forms",
        "portugues": "Formulários"
    },
    "p": {
        "espanol": "Párrafos",
        "ingles": "Paragraphs",
        "portugues": "Parágrafos"
    },
    "h1": {
        "espanol": "Encabezado 1",
        "ingles": "Heading 1",
        "portugues": "Cabeçalho 1"
    },
    "h2": {
        "espanol": "Encabezado 2",
        "ingles": "Heading 2",
        "portugues": "Cabeçalho 2"
    }
}


# Patrón Factory
class WebsiteFactory:
    def create_website(self, language):
        website = Website()
        website.set_language(language)
        website.set_elements(elementos)
        return website


# Patrón Singleton
class WebsiteSingleton:
    _instances = {}

    def __new__(cls, language):
        if language not in cls._instances:
            cls._instances[language] = super(WebsiteSingleton, cls).__new__(cls)
            cls._instances[language].set_language(language)
            cls._instances[language].set_elements(elementos)
        return cls._instances[language]


# Patrón Prototype
class Website:
    def set_language(self, language):
        self.language = language

    def set_elements(self, elements):
        self.elements = elements

    def clone(self):
        new_website = Website()
        new_website.set_language(self.language)
        new_website.set_elements(self.elements)
        return new_website


# Función para mostrar
def mostrar_elementos(website):
    language = website.language
    elements = website.elements
    print(f"Elementos en {language}:")
    for elemento, traduccion in elements.items():
        print(f"{elemento}: {traduccion[language]}")


# Función para seleccionar el idioma
def seleccionar_idioma_creacion_sitio():
    factory = WebsiteFactory()
    while True:
        print("Seleccione el idioma para construir el sitio web:")
        print("1. Español")
        print("2. Inglés")
        print("3. Portugués")
        print("0. Salir")

        opcion = input("Elija una opción (0/1/2/3): ")

        if opcion == "0":
            break
        elif opcion in ["1", "2", "3"]:
            idioma_elegido = "espanol" if opcion == "1" else "ingles" if opcion == "2" else "portugues"
            website = factory.create_website(idioma_elegido)
            mostrar_elementos(website)
        else:
            print("Opción no válida. Por favor, elija una opción válida.")



seleccionar_idioma_creacion_sitio()