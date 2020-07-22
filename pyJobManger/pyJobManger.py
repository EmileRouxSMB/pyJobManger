# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:44:50 2020

@author: rouxemi
"""
import numpy as np
import pandas as pd
import glob

def dummy_fun(x,label):
    print('Run Simu : ', label)
    return (x**2).sum()

class pyJobManager:
    def __init__(self, fun = None,
                 type_simu = 'Dummy',                 
                 param_names = ['p1','p2'],
                 param2opt = None,
                 paramValDefault = None,
                 ResFile=r"Optim_res.csv"):
        
        self.id_simu = 0
        self.type_simu = type_simu
        self.par_names = param_names
        self.ResFile=ResFile
        if fun is None:
            self.fun = dummy_fun
        else:
            self.fun = fun
            
        if param2opt is None:
            self.param2opt = np.ones(len(param_names), dtype=np.bool)
        else:
            self.param2opt = param2opt
        
        if paramValDefault is None:
            self.paramValDefault = np.zeros(len(param_names))
        else:
            self.paramValDefault = paramValDefault

    
    def save_to_csv(self,x,fc):

        # Ouverture du fichier resultats si il existe, sinon ouverture d'un fichier vide avec uniquement les entêtes
        if len(glob.glob(self.ResFile))==0:
            df = pd.DataFrame( columns = ['Id_simu','Type','fc'] + self.par_names )
        else:
            df = pd.read_csv(self.ResFile,delimiter=";")
            
        print(df.head())
        print(self.par_names)
        print(x)
        Id_end = len(df)+1
        df.loc[Id_end,self.par_names] = x
        df.loc[Id_end,'Type'] = self.type_simu
        df.loc[Id_end,'fc'] = fc
        df.loc[Id_end,'Id_simu'] = self.id_simu
        df.to_csv(path_or_buf= self.ResFile, sep= ';', index= False)
        

    def run(self,x=None):
        """
        Call be the optimizer
        """
        if x is None:
            x = self.paramValDefault

        x = np.atleast_2d(x)
        n,dim = x.shape 
        print('n=',n)
        print('dim=',dim)
        print('id_simu=',self.id_simu)
        y = np.atleast_2d(np.zeros((n,1)))
        for i in range(n):
            label_simu = str(self.id_simu) +'_'+ self.type_simu
            x_to_run = self.paramValDefault
            x_to_run[np.where(self.param2opt)]=x[i]
            y[i]=self.fun(x_to_run, label_simu)
            self.save_to_csv(x_to_run,y[i])
            self.id_simu += 1   
        return y
    
if __name__=='__main__':

    
    jm = pyJobManager(param2opt=np.array([0, 1, 1]),
                     param_names = ['p1','p2','p3'],)
    x=np.array([[1,1],[2,2]])
    print(jm.run(x))   

    
