

from math import fabs
from numpy import linspace
from rule import Rule

def currying(f):
    def curried(*args):
        if len(args) >= f.__code__.co_argcount:
            return f(*args)
        return lambda *args2: curried(*(args+args2))
    return curried

@currying
def triangular(l,r,mid , val):
     #l < mid < r
    if val <= l or val >= r:
        return 0
    elif val > l and val <= mid:
        return (val- l) / (mid - l)
    return (r - val) / (r - mid)

@currying
def trapezoidal(a,b,c,d , val):
    #a < b < c < d
    if val < a or val > d:
        return 0
    elif val>= b and val <= c:
        return 1
    elif val >= a and val < b:
        return (val - a) / ( b- a)
    return (d - val) / (d - c) 


def centroide(x,y):
    num = 0
    dem = 0
    for i in range(0,len(x)):
        num += x[i] * y[i]
        dem += y[i] 
    
    return num/dem

def getArea(y,l,r):
    res = 0
    for i in range(l,r):
        res += y[i]
    return res

def bisectriz(x,y):
    l = 0
    l = 0
    r = len(x)

    for _ in range(100):
        m = (l + r)/2
        m = int(m)
        a1 = getArea(y,0,m)
        a2 = getArea(y,m,len(x))
        
        if fabs( a1 - a2 ) <  10**-6:
            return m
        if a1 > a2 :
            r = m
        else:
            l= m
    return x[m]

def getMax(x,y):
    maxx = -10**9
    ind_max = []
    for i  in range(0,len(y)):
        if y[i] > maxx :
            maxx = y[i]
            ind_max = []
            ind_max.append(i)
        elif fabs(y[i] - maxx) < 10**-6:
            ind_max.append(i)
    return ind_max     

def maxMax(x,y):
    maxx = getMax(x,y)
    return x[maxx[len(maxx)- 1]]

def minMax(x,y):
    return x[getMax(x,y)[0]]

def middleMax(x,y):
    maxx = getMax(x,y)
    s = 0
    for i in range(0,len(maxx)):
        s += x[maxx[i]]
    return s/len(maxx)

def Mamdani(rules,funcs,vals,dom):
    res = []
    x = []
    y = []

    for i in rules:
        aux = Rule(i,funcs,dom)
        res.append((aux.evaluate(vals),aux.post))
    

    for item in res:
        ruleVal,rulePost = item
        f  = funcs[rulePost[0]][rulePost[2]]
        line = linspace(dom[rulePost[0]][0], dom[rulePost[0]][1], 10**4)
        #for i in range(dom[rulePost[0]][0], dom[rulePost[0]][1] + 1):
        for i in line:

            val = f(i)

            val = min(val,ruleVal)
            
            if not i in x:
                x.append(i)
                y.append(val)
            else:
                index = x.index(i)
                y[index] = max(val,y[index])
    return x,y

def Larsen(rules,funcs,vals,dom):
    res = []
    x = []
    y = []

    for i in rules:
        aux = Rule(i,funcs,dom)
        res.append((aux.evaluate(vals),aux.post))
    

    for item in res:
        ruleVal,rulePost = item
        f  = funcs[rulePost[0]][rulePost[2]]
        line = linspace(dom[rulePost[0]][0], dom[rulePost[0]][1], 10**4)

        for i in line:

            val = f(i) * ruleVal
            
            if not i in x:
                x.append(i)
                y.append(val)
            else:
                index = x.index(i)
                y[index] = max(val,y[index])
    return x,y



#def my_plot(fig,line,label,func,color = None):
#    x = []
#    y = []
#    for i in line:
#        x.append(i)
#        y.append(func(i))
#    if color != None:    
#        return fig.plot(x,y,label = label,color = color)[0]
#    else:
#        return fig.plot(x,y,label = label)[0]


#f,ax = plt.subplots(1,1)

#line = linspace(0, 10, 10**2)

# ax.set_title("Calidad de la Voz",fontsize = 15) 

# my_plot(ax,line,"Pesima",triangular(0,4,0))
# my_plot(ax,line,"Buena",trapezoidal(3,4,7,8))
# my_plot(ax,line,"Espectacular",triangular(7,10,10))



#ax.set_title("Calidad del Espectaculo",fontsize = 15) 
#my_plot(ax,line,"Aburrido",triangular(0,4,0))
#my_plot(ax,line,"Bueno",trapezoidal(2,4,8,9))
#my_plot(ax,line,"Magnifico",trapezoidal(7,8,10,10))

#line = linspace(0, 100, 10**3)
#ax.set_title("Probabilidad de Pase de ORO",fontsize = 15) 
#my_plot(ax,line,"Baja",trapezoidal(0,0,15,30))
#my_plot(ax,line,"Media",triangular(0,100,50),"red")
#my_plot(ax,line,"Alta",trapezoidal(50,80,100,100))


#l = ax.legend(loc = 'center rigth', bbox_to_anchor=(1,0.5))
#l1 = ax.legend(loc = 'center rigth', bbox_to_anchor=(1,0.5))
#l2 = ax.legend(loc = 'center rigth' , bbox_to_anchor=(1,0.5))

# plt.subplots_adjust(right = 0.85)
# plt.tight_layout()

#plt.savefig('h.png',dpi = 300,format = 'png',bbox_extra_artists = (l,l1,l2,),bbox_inches = 'tight')
#plt.savefig('pase.png',dpi = 300,format = 'png',bbox_extra_artists = (l2,),bbox_inches = 'tight')

