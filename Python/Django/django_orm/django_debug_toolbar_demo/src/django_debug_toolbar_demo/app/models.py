from django.db import models

class Student(models.Model):
    id: models.AutoField = models.AutoField(primary_key=True)
    name: models.CharField = models.CharField(max_length=50)

    def __repr__(self) -> str:
        return f'Student(Id -> {self.id} Name -> {self.name})'
