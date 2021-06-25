my_dict={"a":1,"b":2,"c":3}
try:
    value=my_dict["d"]
except IndexError:
    print("Key doesnt exist!")
except KeyError:
    print("Such Index doesn't exist")
except:
    print("Another error")



my_list=[1,2,3,4,5]
try:
    my_list[6]
except IndexError:
    print(" There's no such index in list!")