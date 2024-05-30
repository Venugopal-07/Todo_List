from django.db import models

# Create your models here.
class todo_list(models.Model):
    task=models.CharField(max_length=150)
    status=models.BooleanField(default=False)
    start_date=models.DateTimeField(auto_now_add=True)
    target_date=models.DateTimeField()

    def __str__(self):
        return self.task+" "+ str(self.status)