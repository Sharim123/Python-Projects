#import another_variable
#from another_variable import another_number
#print(another_variable.another_number)

#from turtle import Turtle, Screen
#turtle = Turtle()
#print(turtle)
#turtle.shape('turtle')
#turtle.color('coral')
#turtle.fd(100)


#scr = Screen
#print(scr)

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = 'l'



print(table)