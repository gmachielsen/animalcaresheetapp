from django.db import models
from django.utils import timezone

class Animal(models.Model):
    # ANIMALS = (
    #     ('X', 'Choose animalfamily')
    #     (REPTILES(), 'Reptiles'),
    # )
    REPTILES = (
        ('X', 'choose type of reptile: crocodile, lizard, snake, turtle'),
        ('C', 'Crocodile'),
        ('L', 'Lizard'),
        ('S', 'Snake'),
        ('T', 'Turtle'),
    )

    CITES_SPECIES = (
        ('X', 'Cites of animal'),
        ('A', 'Cites A or I'),
        ('B', 'Cites B or II'),
        ('C', 'Cites C or III'),
        ('D', 'Cites D or none'),
    )

    latinName = models.CharField(blank=True, null=True, max_length=120)
    # TypeofAnimal = models.CharField(blank=True, null=True, default='X', choises=ANIMALS)
    reptiletype = models.CharField(blank=True, null=True, max_length=1, default='X', choices=REPTILES)
    image = models.ImageField(blank=True, null=True, upload_to="images")
    cites = models.CharField(blank=True, null=True, max_length=1, default='X', choices=CITES_SPECIES)
    habitat = models.CharField(blank=True, null=True, max_length=120)
    feeding = models.TextField(blank=True, null=True, max_length= 500)
    enclosure = models.TextField(blank=True, null=True, max_length= 500)
    temperature = models.TextField(blank=True, null=True, max_length=300)
    sex= models.TextField(blank=True, null=True, max_length= 500)
    male = models.ImageField(blank=True, null=True, upload_to="images")
    female = models.ImageField(blank=True, null=True, upload_to="images")
    breeding = models.TextField(blank=True, null=True, max_length= 500)
    incubation = models.TextField(blank=True, null=True, max_length= 500)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)








    def __str__(self):
        return self.latinName
