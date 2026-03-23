inttype_datavariable = 10
floattype_datavariable = 10.1
booltype_datavariable = True
listtype_datavariable = [1, 2, 3, 4, 5, 6]
tupletype_datavariable = (1, 2, 3)
stringtype_datavariable = "this file is about data types and variables"
dictionarytype_datavariable = {"name": "john", "age": "30"}

print("val0: "+stringtype_datavariable)
print("this is ",type(stringtype_datavariable)," datatype")
print("val1: ",inttype_datavariable)
print("this is ",type(inttype_datavariable)," datatype")
print("val2: ",floattype_datavariable)
print("this is ",type(floattype_datavariable)," datatype")
print("val3: ",booltype_datavariable)
print("this is ",type(booltype_datavariable)," datatype")
print("val4: ",listtype_datavariable)
print("this is ",type(listtype_datavariable)," datatype")
print("val5: ",tupletype_datavariable)
print("this is ",type(tupletype_datavariable)," datatype")
print("val6: ",dictionarytype_datavariable)
print("this is ",type(dictionarytype_datavariable)," datatype")
print("printing list items in same line.")
for i in listtype_datavariable:
    print(i,end=" ")
print("printing list in reverse order")
# print(listtype_datavariable[::-1])
for i in reversed(listtype_datavariable):
    print(i)
print("adding new data to list variable using append, insert and extend.")
print("append will add the new data to the end of list.")
listtype_datavariable.append(10)
print(listtype_datavariable)
print("The extend() method adds elements (like a list) to the end of the list.")
listtype_datavariable.extend([11, 12, 13, 14])
print(listtype_datavariable)
print("insert(index, item) places the new item at the given index without replacing existing elements.")
listtype_datavariable.insert(6,7)
print(listtype_datavariable)
