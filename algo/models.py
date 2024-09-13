#CARRERAS
its = 'ITS'
isc = 'ISC'

#MATERIAS
#ITS
programacion_avanzada = 'Programacion Avanzada'
concurrencia_paralelismo = 'Concurrencia y Paralelismo'
diseno_web = 'Diseño Web'
redes = 'Redes de computadoras'
bases_datos2 = 'Bases de Datos II'
ingles = 'Inglés V'
sistemas_embebidos = 'Sistemas Embebidos'

#MAESTROS
arquitecura_comp = 'Arquitectura Computacional'
estructuras_datos = 'Estructuras de Datos II'
graficacion = 'Graficación'
investigacion_operaciones = 'Investigación de Operaciones'
telecomunicaciones = 'Telecomunicaciones'
admin_archivos = 'Administración de archivos'
bases_datos = 'Bases de Datos I'

#PROFESORES
#ITS
contrato1 = {
    "nombre" : "CONCURSO OPOSICION F1",
    "carreras" : [its, isc],
    "materias" : [programacion_avanzada, diseno_web, bases_datos2],
    "disponibilidad" : [(7,9), (9,11), (11,13), (13,15), (15,16)]
}
contrato2 = {
    "nombre" : "CONCURSO OPOSICION F2",
    "carreras" : [its],
    "materias" : [concurrencia_paralelismo, sistemas_embebidos, telecomunicaciones],
    "disponibilidad" : [(7,9), (9,11), (11,13), (13,15), (15,16)]
}
contrato3 = {
    "nombre" : "CONCURSO OPOSICION F3",
    "carreras" : [its],
    "materias" : [redes, investigacion_operaciones],
    "disponibilidad" : [(7,9), (9,11), (11,13), (13,15), (15,16)]
}
jose_chavez = {
    "nombre" : "JOSÉ MANUEL CHÁVEZ MOLINA",
    "carreras" : [its, isc],
    "materias" : [ingles],
    "disponibilidad" : [(7,9), (11,13)]
}

#ISC
jose_garcia = {
    "nombre" : "JOSÉ ANGEL REYES",
    "carreras" : [isc],
    "materias" : [admin_archivos, estructuras_datos],
    "disponibilidad" : [(9,11), (11,13), (13,15)]
}
agapito = {
    "nombre" : "AGAPITO LEYVA CHIW",
    "carreras" : [isc],
    "materias" : [arquitecura_comp],
    "disponibilidad" : [(11,13), (9,11), (7,9)]
}
luz_hdz = {
    "nombre" : "LUZ MARIA HERNANDEZ CRUZ",
    "carreras" : [isc],
    "materias" : [bases_datos],
    "disponibilidad" : [(9,11), (11,13), (13,15)]
}
justino = {
    "nombre" : "JUSTINO RAMIREZ ORTEGON",
    "carreras" : [isc, its],
    "materias" : [graficacion],
    "disponibilidad" : [(7,9), (9,11), (11,13), (13,15)]
}
maestros = [jose_chavez, contrato1, contrato2, contrato3, jose_garcia, agapito, luz_hdz, justino]

#GRUPOS
its_5a = [(bases_datos2, 4), (diseno_web, 4), (concurrencia_paralelismo, 4), (sistemas_embebidos, 4), 
          (programacion_avanzada, 4), (redes, 4), (ingles, 4)]

isc_5a = [(admin_archivos, 4), (arquitecura_comp, 4), (bases_datos, 4), (estructuras_datos, 4), 
          (graficacion, 4), (investigacion_operaciones, 4), (telecomunicaciones, 3)]

grupos = [its_5a, isc_5a]


#CADA FILA ES UN DIA DE LA SEMANA, CADA COLUMNA ES UN BLOQUE DE 2H
horario_its5a = [[0]*7 for _ in range(5)]
horario_isc5a = [[0]*7 for _ in range(5)]




#HORARIOS
horarios1 = [
    {'Grupo': 'ITS 5A', 'Materia': 'BASE DE DATOS II', 'Maestro': 'AGUILAR CANEPA JOSÉ CARLOS', 'Horas a la semana': 4, 'Lunes': '13-15', 'Martes': '', 'Miércoles': '11-13', 'Jueves': '', 'Viernes': ''},
    {'Grupo': 'ITS 5A', 'Materia': 'DISEÑO WEB', 'Maestro': 'AGUILAR CANEPA JOSÉ CARLOS', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '12-14', 'Miércoles': '', 'Jueves': '11-13', 'Viernes': ''},
    {'Grupo': 'ITS 5A', 'Materia': 'CONCURRENCIA Y PARALELISMO', 'Maestro': 'CONCURSO OPOSICION F2', 'Horas a la semana': 4, 'Lunes': '11-13', 'Martes': '', 'Miércoles': '08-10', 'Jueves': '', 'Viernes': ''},
    {'Grupo': 'ITS 5A', 'Materia': 'SISTEMAS EMBEBIDOS', 'Maestro': 'CONCURSO OPOSICION F2', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '10-12', 'Miércoles': '', 'Jueves': '13-15', 'Viernes': ''},
    {'Grupo': 'ITS 5A', 'Materia': 'PROGRAMACIÓN AVANZADA', 'Maestro': 'AGUILAR CANEPA JOSÉ CARLOS', 'Horas a la semana': 4, 'Lunes': '09-11', 'Martes': '11-13', 'Miércoles': '', 'Jueves': '', 'Viernes': ''},
    {'Grupo': 'ITS 5A', 'Materia': 'REDES DE COMPUTADORAS', 'Maestro': 'CONCURSO OPOSICION F3', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '13-15', 'Miércoles': '', 'Jueves': '13-15', 'Viernes': ''},
    {'Grupo': 'ITS 5A', 'Materia': 'INGLES 5', 'Maestro': 'CHAVEZ MOLINA JOSE MANUEL', 'Horas a la semana': 4, 'Lunes': '15-16', 'Martes': '', 'Miércoles': '', 'Jueves': '09-11', 'Viernes': '09-10'},
    {'Grupo': '5A ISC', 'Materia': 'ADMINISTRACIÓN DE ARCHIVOS', 'Maestro': 'GARCÍA REYES JOSÉ ÁNGEL, MTRO.', 'Horas a la semana': 3, 'Lunes': '09-11', 'Martes': '', 'Miércoles': '', 'Jueves': '', 'Viernes': '11-12'},
    {'Grupo': '5A ISC', 'Materia': 'ARQUITECTURA COMPUTACIONAL', 'Maestro': 'LEYVA CHIW AGAPITO', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '11-13', 'Miércoles': '', 'Jueves': '09-11', 'Viernes': ''},
    {'Grupo': '5A ISC', 'Materia': 'BASES DE DATOS I', 'Maestro': 'HERNÁNDEZ CRUZ LUZ MARÍA', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '09-11', 'Miércoles': '', 'Jueves': '13-15', 'Viernes': ''},
    {'Grupo': '5A ISC', 'Materia': 'ESTRUCTURA DE DATOS II', 'Maestro': 'GARCÍA REYES JOSÉ ÁNGEL', 'Horas a la semana': 4, 'Lunes': '13-15', 'Martes': '', 'Miércoles': '09-11', 'Jueves': '', 'Viernes': ''},
    {'Grupo': '5A ISC', 'Materia': 'GRAFICACIÓN', 'Maestro': 'RAMÍREZ ORTEGÓN JUSTINO', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '13-15', 'Miércoles': '11-13', 'Jueves': '', 'Viernes': ''},
    {'Grupo': '5A ISC', 'Materia': 'INVESTIGACION DE OPERACIONES I', 'Maestro': 'CONCURSO OPOSICIÓN F3', 'Horas a la semana': 3, 'Lunes': '', 'Martes': '11-13', 'Miércoles': '', 'Jueves': '14-15', 'Viernes': ''},
    {'Grupo': '5A ISC', 'Materia': 'TELECOMUNICACIONES', 'Maestro': 'CONCURSO OPOSICIÓN F2', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '07-09', 'Miércoles': '', 'Jueves': '12-14', 'Viernes': ''}
]

horarios2 = [
    {'Grupo': 'ITS 5A', 'Materia': 'BASE DE DATOS II', 'Maestro': 'AGUILAR CANEPA JOSÉ CARLOS', 'Horas a la semana': 4, 'Lunes': '13-15', 'Martes': '', 'Miércoles': '11-13', 'Jueves': '11-13', 'Viernes': ''},
    {'Grupo': 'ITS 5A', 'Materia': 'DISEÑO WEB', 'Maestro': 'AGUILAR CANEPA JOSÉ CARLOS', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '11-13', 'Miércoles': '', 'Jueves': '12-14', 'Viernes': ''},
    {'Grupo': 'ITS 5A', 'Materia': 'CONCURRENCIA Y PARALELISMO', 'Maestro': 'CONCURSO OPOSICION F2', 'Horas a la semana': 4, 'Lunes': '11-13', 'Martes': '', 'Miércoles': '08-10', 'Jueves': '', 'Viernes': ''},
    {'Grupo': 'ITS 5A', 'Materia': 'SISTEMAS EMBEBIDOS', 'Maestro': 'CONCURSO OPOSICION F2', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '13-15', 'Miércoles': '', 'Jueves': '10-12', 'Viernes': ''},
    {'Grupo': 'ITS 5A', 'Materia': 'PROGRAMACIÓN AVANZADA', 'Maestro': 'AGUILAR CANEPA JOSÉ CARLOS', 'Horas a la semana': 4, 'Lunes': '09-11', 'Martes': '11-13', 'Miércoles': '', 'Jueves': '', 'Viernes': ''},
    {'Grupo': 'ITS 5A', 'Materia': 'REDES DE COMPUTADORAS', 'Maestro': 'CONCURSO OPOSICION F3', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '13-15', 'Miércoles': '', 'Jueves': '13-15', 'Viernes': ''},
    {'Grupo': 'ITS 5A', 'Materia': 'INGLES 5', 'Maestro': 'CHAVEZ MOLINA JOSE MANUEL', 'Horas a la semana': 4, 'Lunes': '15-16', 'Martes': '', 'Miércoles': '', 'Jueves': '09-11', 'Viernes': '09-10'},
    {'Grupo': '5A ISC', 'Materia': 'ADMINISTRACIÓN DE ARCHIVOS', 'Maestro': 'GARCÍA REYES JOSÉ ÁNGEL, MTRO.', 'Horas a la semana': 3, 'Lunes': '09-11', 'Martes': '', 'Miércoles': '', 'Jueves': '', 'Viernes': '11-12'},
    {'Grupo': '5A ISC', 'Materia': 'ARQUITECTURA COMPUTACIONAL', 'Maestro': 'LEYVA CHIW AGAPITO', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '09-11', 'Miércoles': '', 'Jueves': '09-11', 'Viernes': ''},
    {'Grupo': '5A ISC', 'Materia': 'BASES DE DATOS I', 'Maestro': 'HERNÁNDEZ CRUZ LUZ MARÍA', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '13-15', 'Miércoles': '', 'Jueves': '13-15', 'Viernes': ''},
    {'Grupo': '5A ISC', 'Materia': 'ESTRUCTURA DE DATOS II', 'Maestro': 'GARCÍA REYES JOSÉ ÁNGEL', 'Horas a la semana': 4, 'Lunes': '13-15', 'Martes': '', 'Miércoles': '09-11', 'Jueves': '', 'Viernes': ''},
    {'Grupo': '5A ISC', 'Materia': 'GRAFICACIÓN', 'Maestro': 'RAMÍREZ ORTEGÓN JUSTINO', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '11-13', 'Miércoles': '11-13', 'Jueves': '', 'Viernes': ''},
    {'Grupo': '5A ISC', 'Materia': 'INVESTIGACION DE OPERACIONES I', 'Maestro': 'CONCURSO OPOSICIÓN F3', 'Horas a la semana': 3, 'Lunes': '', 'Martes': '11-13', 'Miércoles': '', 'Jueves': '14-15', 'Viernes': ''},
    {'Grupo': '5A ISC', 'Materia': 'TELECOMUNICACIONES', 'Maestro': 'CONCURSO OPOSICIÓN F2', 'Horas a la semana': 4, 'Lunes': '', 'Martes': '12-14', 'Miércoles': '', 'Jueves': '12-14', 'Viernes': ''}
]

horarios = [horarios1, horarios2]