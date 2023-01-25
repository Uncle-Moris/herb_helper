from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=100,
                            blank=False,
                            null=False,
                            unique=True
                            )
    slug = models.SlugField(max_length=100,
                            blank=False,
                            null=False,
                            unique=True
                            )

    class Meta:
        abstract = True
