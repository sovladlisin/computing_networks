from django.db import models

# Create your models here.


class List(models.Model):
    master = models.ForeignKey(
        'self', blank=True, null=True, related_name='unit_parent', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='')
    text = models.TextField(default='')

    def __str__(self):
        return self.name


# Ontology
class Person(models.Model):
    name = models.CharField(default='', max_length=300)

    def __str__(self):
        return self.name


class System(models.Model):
    name = models.CharField(default='', max_length=300)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


# Markup
class Markup_Person(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    list = models.ForeignKey(List, blank=False, null=False,
                             related_name='markup_person_list', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, blank=True, null=True,
                               related_name='markup_person_person', on_delete=models.CASCADE)


class Markup_System(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    list = models.ForeignKey(List, blank=False, null=False,
                             related_name='markup_system', on_delete=models.CASCADE)
    system = models.ForeignKey(System, blank=True, null=True,
                               related_name='markup_system', on_delete=models.CASCADE)
