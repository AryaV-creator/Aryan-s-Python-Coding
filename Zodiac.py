"""
author: <Aryan Vemulapalli>
course: ICS3UC
date: 2024/11/15
"""

"""
This is a compatibility simulator based on asian zodiac signs! Enjoy :)
"""
#sub code 1
def zodiac(year,month,day):
    years=[1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
    yearZodiac={1998:"Tiger",1999:"Rabbit", 2000:"Dragon",2001:"Snake",2002:"Horse",2003:"Sheep",2004:"Monkey",2005:"Rooster", 2006:"Dog",2007:"Pig",2008:"Rat",2009:"Ox",}
    months=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

    if month in months[2: ]:
        for i in range(12):
            remainder=(year-years[i])%12
            if remainder==0:
                index=years[i]
                stringYear=str(year)
                listYear=list(stringYear)
                if listYear[3]=="0"or listYear[3]=="1":
                    sign=f"Air {yearZodiac[index]}"
                elif listYear[3]=="2"or listYear[3]=="3":
                    sign=f"Water {yearZodiac[index]}"
                elif listYear[3]=="4"or listYear[3]=="5":
                    sign=f"Fire {yearZodiac[index]}"
                elif listYear[3]=="6"or listYear[3]=="7":
                    sign=f"Earth {yearZodiac[index]}"
                elif listYear[3]=="8"or listYear[3]=="9":
                    sign=f"Wind {yearZodiac[index]}"
    else:
        if day<20:
            year=year-1
            for i in range(12):
                remainder=(year-years[i])%12
                if remainder==0:
                    index=years[i]
                    stringYear=str(year)
                    listYear=list(stringYear)
                    if listYear[3]=="0"or listYear[3]=="1":
                        sign=f"Air {yearZodiac[index]}"
                    elif listYear[3]=="2"or listYear[3]=="3":
                        sign=f"Water {yearZodiac[index]}"
                    elif listYear[3]=="4"or listYear[3]=="5":
                        sign=f"Fire {yearZodiac[index]}"
                    elif listYear[3]=="6"or listYear[3]=="7":
                        sign=f"Earth {yearZodiac[index]}"
                    elif listYear[3]=="8"or listYear[3]=="9":
                        sign=f"Wind {yearZodiac[index]}"
    return sign
##Main
done=False
zodiacPlacement=[]
names=[]
while done!=True:
    name=input("Enter the person's name: ")
    userAnswer=input("Enter date of birth(yyyy/mmm/dd): ")
    addedSign=zodiac(year=int(userAnswer.split("/")[0]),month=userAnswer.split("/")[1],day=int(userAnswer.split("/")[2]))
    names.append(name)
    zodiacPlacement.append(str(addedSign))
    zodiacCompatability={personName:"" for personName in names}
    userChoice=input("if you want to continue playing, type 'continue', or type 'finish' to end the game: ")
    if userChoice.lower()=="finish":
        done=True
    zodiacCompatability={names[i]:zodiacPlacement[i] for i in range(len(names))}
print("")
print(f"Here are their signs: ")
for i in range(len(names)):
    print(names[i],":",zodiacCompatability[names[i]])
#Sub code 3
animalAppend=[]
for i in range(len(names)):
    animalAppend.append(zodiacCompatability[names[i]].split())
    print(animalAppend.append(zodiacCompatability[names[i]].split()))
element=[]
animalZodiac=[]
for i in range(len(animalAppend)):
    for j in range(len(animalAppend[i])):
        if j==0:
            element.append(animalAppend[i][j])
        else:
            animalZodiac.append(animalAppend[i][j])

#Comparing Zodiacs and Elements
type1=0
type2=0
type3=0
type4=0
elementType1=0
elementType2=0
elementType3=0
elementType4=0
elementType5=0
compatabilityCheck=len(animalZodiac)
for i in range(len(animalZodiac)):
    if animalZodiac[i-1]=="Rat" or animalZodiac[i-1]=="Dragon" or animalZodiac[i-1]=="Monkey":
            type1=type1+1

    if animalZodiac[i-1]=="Ox" or animalZodiac[i-1]=="Snake" or animalZodiac[i-1]=="Rooster":
        type2=type2+1

    if animalZodiac[i-1]=="Tiger" or animalZodiac[i-1]=="Horse" or animalZodiac[i-1]=="Dog":
        type3=type3+1

    if animalZodiac[i-1]=="Rabbit" or animalZodiac[i-1]=="Goat" or animalZodiac[i-1]=="Pig":
        type4=type4+1
for i in range(len(element)):
    if element[i-1]=="Metal":
            elementType1=elementType1+1
    if element[i-1]=="Air":
            elementType2=elementType2+1
    if element[i-1]=="Fire":
            elementType3=elementType3+1
    if element[i-1]=="Water":
            elementType4=elementType4+1
    if element[i-1]=="Earth":
            elementType5=elementType5+1       
if type1==compatabilityCheck or type2==compatabilityCheck or type3==compatabilityCheck or type4==compatabilityCheck:
    if elementType1==len(element) or elementType2==len(element) or elementType3==len(element) or elementType4==len(element) or elementType5==len(element):
#Results
        print()
        print(*names,sep=' and ', end=" ")
        print("are Compatible!")
    else:
        print()
        print(*names,sep=' and ', end=" ")
        print("are not Compatible")
else:
    print()
    print(*names,sep=' and ', end=" ")
    print("are not Compatible")
     