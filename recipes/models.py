from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65)
    
    # Ao invés de "Category object (1)" vai ser agora -> "Carnes", por exemplo, quando for criado no /admin
    def __str__(self) -> str:
        return self.name

class Recipe(models.Model):
    
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    # Atualiza a data apenas na criação do objeto (auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Atualiza a data toda vez que o objeto é modificiado (auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    
    def __str__(self) -> str:
        return self.title
    
    

    
    