from django.db import models
from django.core.exceptions import ValidationError


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Mounth(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='months')

    def __str__(self):
        return f"{self.course.name} - {self.name}"
    

class ClassAndHomeWork(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    homework = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                                related_name='classes', null=True, blank=True)

    mounth = models.ForeignKey(Mounth, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return f"{self.course.name} - {self.mounth.name} - {self.title}"
    

    def clean(self) -> None:
        if self.course.name == "Backend":
            if 'Backend' not in self.mounth.course.name:
                raise ValidationError("Invalid month for Backend course")
    

