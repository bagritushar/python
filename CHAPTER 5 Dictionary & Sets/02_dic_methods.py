marks = {
    "Tushar": 100,
    "Rohan": 90,
    "Rahul": 80

}

# print(marks, type(marks))

# print(marks["Tushar"], marks["Rohan"])
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# print(len(marks))
# marks.update({"Tushar": 95})
# print(marks)    
# marks.pop("Rohan")
# print(marks)

print(marks.get("sahil"))
print(marks)
print(marks.setdefault("sahil", 70)) # if key not present then add key with value 70
print(marks)

