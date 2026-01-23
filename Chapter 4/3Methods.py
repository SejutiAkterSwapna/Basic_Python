student = {
    "name" : "Abir",
    "subjects":{
        "ENG": 70,
        "MAT": 69,
        "EEE": 88,
    }
}
# print(student.keys())
# print(len(list(student.keys())))
# print(len(student))

# print(list(student.values()))
# print(list(student.items()))
# pairs = list(student.keys())
# print(pairs[1])

# print(student["name2"]) #Error
# print(student.get("name2")) #Not Error -> None

new_dict ={"location":"natore"}
student.update(new_dict)
print(student)
# student.update({"location":"natore"})
# print(student)