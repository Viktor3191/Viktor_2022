from django.db import models


# Create your models here.
# python manage.py makemigrations project команда для миграции
# python manage.py migrate project сохраняет таблицы в базе данных
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FileField(upload_to='img/')
