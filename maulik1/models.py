from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, RegexValidator


# Create your models here.
# class shop(models.Model):
#     Title = models.CharField(_("Title"),max_length=254)
#     Client = models.CharField(_("Client"),max_length=254)
#     Skills = models.CharField(_("Skills"),max_length=254)
#     Link = models.CharField(_("Link"),max_length=254)
#     Date=models.DateField()
#     Portfolio_Image = models.ImageField(_("Portfolio Image"),upload_to="plify_image/Portfolio_image", default="")
#     Description = models.TextField(_("Description"),max_length=800)
#     feature = models.ForeignKey('Category',default="", on_delete=models.CASCADE)
#     id=models.AutoField(primary_key=True)
#     def __str__(self):
#         return self.Title
