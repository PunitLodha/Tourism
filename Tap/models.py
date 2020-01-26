from django.db import models
from jsonfield import JSONField

class City:
    name = models.CharField(max_length=20)
    costperday = models.IntegerField()
    places = JSONField()
    hotels = JSONField()

'''
City = {
    'name' : 'abc',
    'places' : {
        'review1' : {
            'text' : 'balskcjasvsjs',
            'rating' : 8,
        }
        'review2' : {
            'text' : 'balskcjasvsjs',
            'rating' : 8,
        }
    }
    'hotels' : {
        'review1' : {
            'text' : 'balskcjasvsjs',
            'rating' : 8,
        }
        'review2' : {
            'text' : 'balskcjasvsjs',
            'rating' : 8,
        } 
    }
}
'''
