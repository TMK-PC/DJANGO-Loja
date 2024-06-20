from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
import os
from .models import Itens

@receiver(post_delete, sender=Itens)
def deletar_arquivo_foto(sender, instance, **kwargs):
    ''''''