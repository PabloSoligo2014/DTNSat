'''
Created on 19 de ago. de 2016

@author: pabli
'''
from django.db import models
import orekit

class Orbit(models.Model):
    '''
    classdocs
    '''
    
    
    @classmethod
    def create(cls):        
        orekit.initVM()
        result = cls()
        
        return result
    
    def __str__(self):
        return None

