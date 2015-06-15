'''
Created on Jun 11, 2015

@author: nqian
@author: Grant Mercer

'''
# import antigravity
import json
from Tkinter import Message, Toplevel, Button
#from CALIPSO_Visualization_Tool import dbBase

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from dbPolygon import dbBase, dbPolygon

class PolygonWriter(object):
    '''
    classdocs
    '''

    __dbEngine = create_engine('sqlite:///../db/CALIPSOdb.db', echo=True)

    def __init__(self, fileName="objs/polygons.json"):
        '''
        Constructor
        '''
        self.__fileName = fileName
        self.__plotType = 0
        self.__hdf = ''
        self.__dict = {}
        
        dbBase.metadata.create_all(self.__dbEngine)
        
        self.__Session = sessionmaker(bind=self.__dbEngine)
        #self.addTest()
        self.getTest()

        
    def addTest(self):
        self.__session = self.__Session()
        
        test = dbPolygon(vertices="1,2,3", color="#FFFFF")
        self.__session.add(test)
        self.__session.commit()
        self.__session.close()
        print ("added")
        
    def getTest(self):
        session = self.__Session()
        poly = session.query(dbPolygon).filter_by(color="#FFFFF").first()
        print poly
        
        
    def set(self, key, value):
#         try:
#             lst = self.__dict[key]
#             if type(value) is not list:
#                 lst.append(value)
#             else:
#                 for item in value:
#                     lst.append(item)
#         except KeyError:
#             self.__dict[key] = value
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
    
    def encode(self, data):
        with open(self.__fileName, 'w') as outfile:
            json.dump(data, outfile)
        
    def reset(self):
        for key in self.__dict:
            if key is not "HDFFile" or key is not "plotype":
                del key