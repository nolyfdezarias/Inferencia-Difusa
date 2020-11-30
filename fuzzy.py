

from funcs import *
import matplotlib.pyplot as plt

class Fuzzy():

    


    def __init__(self,Agg_method = "m",Dezz_method = "c"):
        self.Agg_methods = {}
        self.Agg_methods["m"] = Mamdani
        self.Agg_methods["l"] = Larsen

        self.Dezz_methods = {}
        self.Dezz_methods["c"] = centroide
        self.Dezz_methods["b"] = bisectriz
        self.Dezz_methods["maxm"] = maxMax
        self.Dezz_methods["minm"] = minMax
        self.Dezz_methods["midm"] = middleMax

        self.agg_method = self.Agg_methods[Agg_method]
        self.dezz_method = self.Dezz_methods[Dezz_method]
        self.funcs = {}
        self.doms = {}
        self.rules = []


    def solve(self,input_values):
        x,y = self.agg_method(self.rules,self.funcs,input_values,self.doms)
        
        res = self.dezz_method(x,y)
        
        return res
    
    def proccesRule(self,rule):
        pre,post = rule
        post = post.split(',')
        if len(post) > 1:
            newRules = []
            for item in post:
                newRules.append((pre,item))
            return False , newRules
        return True,None

    def new_Rule(self,rule):
        val , newRules = self.proccesRule(rule)
        if val:
            self.rules.append(rule)
        else:
            for item in newRules:
                self.rules.append(item)

    def new_Var(self,var):
        _name , dic = var
        self.funcs[_name] = {}
        
        for k,v  in dic.items():
            if k == "dominio":
                self.doms[_name] = v
            else:
                self.funcs[_name][k] = v 