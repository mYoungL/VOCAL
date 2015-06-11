'''
Created on Jun 11, 2015

@author: nqian
'''
# import antigravity
import json


class PolygonWriter(object):
    '''
    classdocs
    '''


    def __init__(self, fileName="polygons.json"):
        '''
        Constructor
        '''
        self.__fileName = fileName
        self.__plotType = 0
        self.__hdf = ''
        self.__dict = {}
        
    def add(self, key, value):
        self.__dict[key] = value
        
    def setJsonFile(self, fileName):
        self.__fileName = fileName
        
    def setPlotType(self, plotType):
        self.__plotType = plotType
        
    def setHDFFile(self, hdf):
        self.__hdf = hdf
        
    def getJsonFile(self):
        return self.__fileName
    
    def getPlotType(self):
        return self.__plotType
    
    def getHDFFile(self):
        return self.__hdf
        
    def getDictionary(self):
        return self.__dict
    
    def encode(self):
        f = open(self.__fileName, 'w')
        json.dumps(self.__dict, f)
        f.close()
        
    def decode(self):
        f = open(self.__fileName, 'r')
        self.__dict = json.load(f)