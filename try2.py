my_dict={"a":1,"b":2,"c":3}
try:
    value=my_dict["c"]
except (IndexError,KeyError):
    print("Mistake occured IndexError or KeyError!")
else:
    print("Nothing happened")
finally:
    print("Operation is finished")
