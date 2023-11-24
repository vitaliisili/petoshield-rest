from django.db import models


class BaseModel(models.Model):
    """An abstract base model with created_at and updated_at fields.

    Attributes:
        created_at (DateTimeField): The date and time when the model instance was created.
        updated_at (DateTimeField): The date and time when the model instance was last updated.

    Meta:
        abstract (bool): Specifies that this model is abstract and cannot be instantiated directly.
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
