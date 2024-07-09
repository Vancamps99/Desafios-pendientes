from django.db import models

# Create your models here.
#PRIMERO EL CURSO O EL PROFESOR NO SE PUEDE POR EL ESTUDIANTE YA QUE A ESTE LE AGREGAREMOS EL CURSO
class Curso(models.Model):
    codigo = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50 , null=False, blank=False)
    version = models.IntegerField()

def __str__(self):
    return self.name

class Profesor(models.Model):
    rut= models.CharField(max_length=9,primary_key=True)
    nombre= models.CharField(max_length=50, null=False,blank=False)
    apellido= models.CharField(max_length=50, null=False,blank=False)
    activo= models.BooleanField(default=False)
    creado_por= models.CharField(max_length=50, null=False,blank=False)
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
    #relacion many to many
    cursos  =models.ManyToManyField(Curso,related_name='profesores')   

class Estudiante(models.Model):  
    rut= models.CharField(max_length=9,primary_key=True)
    nombre= models.CharField(max_length=50, null=False,blank=False)
    apellido= models.CharField(max_length=50, null=False,blank=False)
    fecha_nacimiento= models.DateTimeField(null=False,blank=False)
    activo= models.BooleanField(default=False)
    creado_por= models.CharField(max_length=50, null=False,blank=False)
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
    #relacion one to many
    curso=models.OneToOneField(Curso,related_name='alumnos',on_delete=models.CASCADE)

class Direccion():
    id=models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50,null=False,blank=False)
    numero = models.CharField(max_length=50,null=False,blank=False)
    dpto= models.CharField(max_length=10,null=True,blank=False)
    comuna= models.CharField(max_length=50,null=False,blank=False)
    ciudad= models.CharField(max_length=50,null=False,blank=False)
    region= models.CharField(max_length=50,null=False,blank=False)
    #one to one field
    Estudiante= models.OneToOneField(Estudiante,related_name='direcciones',null=False,blank=False,on_delete=models.CASCADE)#fk uno a uno
    
    
       