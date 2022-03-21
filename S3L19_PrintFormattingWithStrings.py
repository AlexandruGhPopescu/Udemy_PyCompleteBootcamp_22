# 'String here {} then also {}'.format('something1','something2')

string_1="This is a {} string"

print(string_1.format("quite long"))
print("The {0} {0} {0}".format("fox","brown","quick"))
print("The {1} {0} {2}".format("fox","brown","quick"))
print("The {q} {b} {f}".format(b="brown", f="fox", q="quick"))
print("\n")

#Float formatting follows "{value:width.precision f}"

result=100/77
print(result)
print("The result was {}".format(result))
print("The result was {r:1.4f}".format(r=result))
print("The result was {r:7.4f}".format(r=result))
print ("\n")

#Python 3.6 new format method - common into other programing languages : f"<a_string>{the_variable}"

name_1 = "Jose"
name_2 = "Sam"
age = 4
print(f"Hello my name is {name_1}")
print(f"{name_2} is {age} years old.")
