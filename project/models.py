from typing import TYPE_CHECKING
from django.db import models

TYPE_CHOICE = (
    ('project', 'project'),
    ('product', 'product'),
    ('application', 'application')
)

class project(models.Model):
    title = models.CharField(max_length=138)
    description = models.TextField(max_length=3000)
    type = models.CharField(choices=TYPE_CHOICE, max_length=138)
