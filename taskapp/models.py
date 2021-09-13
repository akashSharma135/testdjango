from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    
    assigned_task = models.CharField(max_length=2000, default="")
    status = (
        (0, _('Not Completed')),
        (1, _('Completed'))
    )
    
    task_status = models.IntegerField(choices=status, default=0, verbose_name='task status')
    
    
    def __str__(self) -> str:
        return self.assigned_task