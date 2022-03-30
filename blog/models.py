from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #modeli tanımlıyor. Class bir nesne tanımladıgımızı belirtir.
    #Post modelimizin ismi
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #foreignkey baska bir modele referans tanımlar
    title = models.CharField(max_length=200) #belirli bir uzunluktaki metinleri tanımlamak için kullanılır
    text = models.TextField() #uzun sınırsız metinleri tanımlar
    created_date = models.DateTimeField(
            default=timezone.now) #DateTimeField gün ve saati tanımlar
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #gönderiyi yayınlayan metod
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title