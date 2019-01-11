from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, db_index=True, related_name='actions')
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType, related_name='target_obj', on_delete=models.CASCADE, blank=True, null=True)
    target_id = models.PositiveIntegerField(blank=True, null=True, db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

