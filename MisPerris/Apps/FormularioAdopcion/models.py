from django.db import models

# Create your models here.

class Mascota(models.Model):
	codigo = models.PositiveIntegerField()
	nombreMascota = models.CharField(max_length=30)
	op1=(('S', 'Pequeño'),('M', 'Mediano'),('L', 'Grande'))
	tamaño= models.CharField(max_length=1, choices=op1, default='M')
	peso= models.DecimalField(max_digits=4, decimal_places=2)
	color= models.CharField(max_length=20)
	descripcion= models.CharField(max_length=300)
	fechaRescate = models.DateField()
	op2=(('R','Rescatado'),('D','Disponible'),('A','Adoptado'))
	estado= models.CharField(max_length=1, choices=op2, default='D') 
	
	def __str__(self):
		cadena = "Codigo: {0} " " / Nombre: {1} " " / Estado: {2}"
		return cadena.format(self.codigo, self.nombreMascota, self.estado)
	