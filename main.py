import math
#from johnfil import *
import eksterne_funktioner as extern
print( ( math.cos( math.radians( 90) )))

def my_function(x):
  print("Hello from a function, my argument was:",x)

my_function("test")
my_function("hest")
my_function("fest")
my_function("pest")
my_function("mest")


#Her er en kommentar.. den er ny.. TODO: PUSH IT.
def summeren(firstNumber, secondNumber):
    return firstNumber+secondNumber

def gange(x,y):
    print(x*y)

def opløft(x,y):
    print(x**y)

def gangemedto(x):
    return x*2


#resultatet = gangemedto(5)




print("	   a")
print("	********")
print("	*     *")
print("	*    *")
print("b	*   *   c")
print("  	*  *")
print("	* *")
print("	**")
print("	* ")

print()
print("	*")
print("	* *  c")
print("b	*   *")
print("	*     *")
print("	********")
print("	   a")
firstnumber = int( input("skriv et tal: ") )
print("Du har tastet: ",firstnumber)

secondnumber = int( input("skriv et tal mere: ") )
print("Du har tastet: ",secondnumber)


summen = summeren(firstnumber,secondnumber)
print(summen)