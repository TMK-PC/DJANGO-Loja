from django.db import models

# Create your models here.

class Tipo(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length= 100)

    def __str__(self):
        return self.nome

class Itens(models.Model):
    id = models.AutoField(primary_key = True)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    nome = models.CharField(blank=False, null=False, max_length= 100)
    descricao = models.TextField(blank=True, null=True,)
    preco = models.FloatField(blank=True, null=True)
    foto = models.ImageField(upload_to='media/')
    

    def delete(self, *args, **kwargs):
        self.foto.delete(save=False)
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.nome

    

    
