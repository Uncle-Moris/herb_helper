from django.db import models
from django.utils.text import slugify


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
                            , editable=False
                            )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
