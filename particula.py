from algoritmos import distancia_euclidiana 
import json

class Particula:
    def __init__(self, id="", origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0, red=0, green=0, blue=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)  # Keep this line

    def __str__(self):
        return (
            f'ID: {self.__id}\n'
            f'  Origen: ({self.__origen_x}, {self.__origen_y})\n'
            f'  Destino: ({self.__destino_x}, {self.__destino_y})\n'
            f'  Velocidad: {self.__velocidad}\n'
            f'  Color: ({self.__red}, {self.__green}, {self.__blue})\n'
            f'  Distancia: {self.__distancia:.2f}\n'
        )

    def __lt__(self, other):
        return self.id < other.id
        
    def to_dict(self):
        return {
            "id": self.__id,
            "origen_x": self.__origen_x,
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }

    @staticmethod  
    def guardar_en_json(particles, filename='registroDatos.json'):
        with open(filename, 'w') as f:
            json.dump([particle.to_dict() for particle in particles], f, indent=4) 

    @staticmethod  
    def click_guardar_sesion(current_particles, filename=None):
        if filename is None:
            filename = 'registroDatos.json'  

        Particula.guardar_en_json(current_particles, filename)  
        print(f"Partículas guardadas en {filename}!")  

    @property
    def id(self):
        return self.__id

    @property
    def origen_x(self):  # Property for origen_x
        return self.__origen_x

    @property
    def origen_y(self):  # Property for origen_y
        return self.__origen_y

    @property
    def destino_x(self):
        return self.__destino_x

    @property
    def destino_y(self):
        return self.__destino_y

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue

    @property
    def distancia(self):
        return self.__distancia
