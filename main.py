 

from fuzzy import *
import matplotlib.pyplot as plt

fuzzySis = Fuzzy(Agg_method="l",Dezz_method="c")



fuzzySis.new_Rule(("Voz is Pesima or Espectaculo is Aburrido","PP is Baja"))
fuzzySis.new_Rule(("Voz is Buena and Espectaculo is Bueno", "PP is Media"))
fuzzySis.new_Rule(("Voz is Espectacular or Espectaculo Magnifico", "PP is Alta"))


var1 = {}

var1["dominio"] = (0,10)
var1["Pesima"] = triangular(0,4,0)
var1["Buena"] = trapezoidal(3,4,7,8)
var1["Espectacular"] = triangular(7,10,10)

fuzzySis.new_Var(("Voz",var1))

var2 = {}

var2["dominio"] = (0,10)
var2["Aburrido"] = triangular(0,4,0)
var2["Bueno"] = trapezoidal(2,4,8,9)
var2["Magnifico"] = trapezoidal(7,8,10,10)

fuzzySis.new_Var(("Espectaculo",var2))

var3 = {}
var3["dominio"] = (0,100)
var3["Baja"] = trapezoidal(0,0,15,30)
var3["Media"] = triangular(0,100,50)
var3["Alta"] = trapezoidal(50,80,100,100)
#PP probabilidad de pase de oro
fuzzySis.new_Var(("PP",var3))


input_vals = {}
input_vals["Voz"] = 3
input_vals["Espectaculo"] = 8




print(fuzzySis.solve(input_vals))

