class Jugador:
    def __init__(self, nom, ciu, cam,num):
        self.nombre = nom
        self.ciudad = ciu
        self.campeonato= int(cam)
        self.numeroJ= int(num)

    def agregar_nombre(self, n):
            self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_campeonato(self, n):
            self.campeonato = n

    def obtener_campeonato(self):
        return self.campeonato

    def agregar_ciudad(self, n):
            self.ciudad = n

    def obtener_ciudad(self):
        return self.ciudad

    def agregar_numeroJ(self, n):
            self.numeroJ = n

    def obtener_numeroJ(self):
        return self.numeroJ

    def __str__(self):
        return "%s %s %d %.2f" %(self.nombre,self.ciudad, self.campeonato, self.numeroJ)

    def __repr__(self):
        return "%s %s %d %.2f" %(self.nombre,self.ciudad, self.campeonato, self.numeroJ)


class Operaciones(object):

    def __init__(self, listado):
        self.listado_estudiantes = listado

    def ordenar(self):
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
        """
        return sorted(self.listado_estudiantes, key=lambda estudiante: estudiante.nombre)

    def ordenar2(self):
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
        """
        return sorted(self.listado_estudiantes, key=lambda estudiante: estudiante.campeonato)