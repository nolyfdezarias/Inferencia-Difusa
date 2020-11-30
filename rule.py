
class Rule():
    def __init__(self,rule,func_dic,dom):
        self.pre = rule[0].split()
        
        self.post = rule[1].split()
        self.funcs = func_dic
        self.dom = dom
        
    

    def evaluate(self,in_vals):

        res = 0
        op = ""
        neg = False
        var = []
        for x in self.pre:

            if x == "is":
                continue
            
            if x == "not":
                neg = True
            elif x == "and":
                op = "min"
            elif x == "or":
                op = "max"
            else:
                var.append(x)
            

            if len(var) == 2 : 
                f = self.funcs[var[0]][var[1]]
                fval = f(in_vals[var[0]])

                var = []
                if neg:
                    fval = 1 - fval
                    neg = False
                if op == "":
                    res = fval
                else:
                    res = eval(op+"("+ str(res) + "," + str(fval) +")")
        
        return res
                
                    


