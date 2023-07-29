from django.db import models

class Resident(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    building_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    token_amount = models.DecimalField(max_digits=10, decimal_places=2)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    move_in_date = models.DateField()
    move_out_date = models.DateField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    assigned_groups = models.ManyToManyField('Group')

    def __str__(self):
        return self.name

class CommunityEvent(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name