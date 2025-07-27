days_dict={"First":"Monday", "Second":"Tuesday", "Third":"Wednesday", "Fourth": "Thursday", "Fifth":"Friday", "Sixth" : "Saturday", "Seventh":"Sunday"}
print("what day of the the week do you want me to print")
days_dict.keys.lower()

index=input().lower()
key1=days_dict[str(index)]
print("the "+str(index)+" day of the week is " + str(key1))
