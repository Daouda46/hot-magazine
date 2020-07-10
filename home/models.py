from django.db import models

# Create your models here.

class Category(models.Model):
    titre = models.CharField(blank=True, max_length=50)
    description = models.CharField(blank=True, max_length=200)
    details = models.TextField(blank=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to="images/", blank=True)
    status = models.BooleanField(default=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categorie'

    def __str__(self):
        return  self.titre
		


class Produit(models.Model):
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    titre = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='produit/images', blank=True)
    prix = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True)
    status = models.BooleanField()
    slug = models.SlugField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'

    def __str__(self):
        return self.titre
		
    


	
	

	
	