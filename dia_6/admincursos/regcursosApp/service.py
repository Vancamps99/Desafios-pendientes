
from .models import Curso, Profesor, Estudiante, Direccion
def crear_curso(pCodigo,pNombre,pVersion=None):
    curso = Curso(codigo=pCodigo,nombre=pNombre)
    curso.save()    
    return curso

def crear_profesor(pRut,pNombre,pApellido,pCreado,pActivo=False):
    prof = Profesor(rut=pRut,nombre=pNombre, apellido=pApellido, creado_por=pCreado,activo=pActivo)
    prof.save()
    return prof

def crear_estudiante(pRut,pNombre,pApellido,pCreado,pbirth,pActivo=False):
    estudiante = Estudiante(rut=pRut,nombre=pNombre, apellido=pApellido,creado_por=pCreado,fecha_nacimiento=pbirth ,activo=pActivo)
    estudiante.save()
    return estudiante

def crear_direccion(rut_estu, pCalle, pNumero, pComuna, pRegion, pDpto=None):
    obj_estu = Estudiante.objects.get(pk=rut_estu)
    direccion = Direccion(estudiante=obj_estu, calle=pCalle, numero=pNumero, comuna=pComuna, region=pRegion, dpto=pDpto)
    direccion.save()
    return direccion

def obtiene_estudiante(rut):
    obj_estu=Estudiante.objects.get(pk=rut)
    return obj_estu

def obtiene_profesor(rut):
    return Profesor.objects.get(id=rut)#pasarla directo o hacer lo de arriba

def obtiene_curso(codigo):
    return Curso.objects.get(pk=codigo)

def agrega_profesor_a_curso(rut,codigo):#se puede combinar los metodos
    profesor=obtiene_profesor(rut)
    curso=obtiene_curso(codigo)
    profesor.cursos.add(curso)
    
def agrega_cursos_a_estudiante(rut, codigo):
    estudiante = obtiene_estudiante(rut)
    curso=obtiene_curso(codigo)
    estudiante.curso.add(curso)
   

def imprime_estudiante_cursos(estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    cursos = estudiante.cursos.all()
    for curso in cursos:
        print(f'Curso: {curso.nombre}')