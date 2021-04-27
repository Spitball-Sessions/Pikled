from django.db import models

# Create your models here.
class Results(models.Model):
    recipe_name = models.CharField('recipe name', max_length=200,)
    add_D = models.DateField('date added')
    start_DT = models.DateTimeField('date & time recipe started')
    test_DT = models.DateTimeField('date & time of test', null=True) # at some point, should be able to have multiple of these per recipe.  If no tests other than post-ferment, Null == True
    end_DT = models.DateTimeField('date & time recipe ended')
    test_intervals = models.IntegerField('Number of times tested', null=True) # this should relate to test_DT.
    rating = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), unique=True)
    notes = models.CharField('thoughts or changes', max_length=900,)
