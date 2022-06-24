# from calendar import week 


week1={"Kaya":["Verite","Judy","Benadate"],"Serving Area":["Zipporah","Salma","Shamim","Phelisia"],"Washroom":["RoseMary","Zuennah","Cudra"]}
week2={"Kaya":["Rosemary","Zuennah","Phelisia"],"Serving Area":["Verite","Judy","Benadate","Cudra"],"Washroom":["Zipporah","Shamim","Salma"]}
week3={"Kaya":["Zipporah","Cudra","Salma"],"Serving Area":["Phelisia","Rosemary","Shamim","Zuennah"],"Washroom":["Verite","Benadate","Judy"]}
# week4={"Kaya":["Verite","Judy","Benadate"],"Serving Area":["Zipporah","Salma","Shamim","Phelisia"],"Washroom":["RoseMary","Zuennah","Cudra"]}
print("This is a duty roaster containing the places of students their respective places of work")
week=week1 or week2 or week3
week=(input("Enter the week type:"))
b=(input("Enter the respective place of work:"))

# while week == "week1" or "week2":
#     students = [week1.values()]
#     for stds in students:
#         index = students.index(stds)
#         b=(input("Enter the respective place of work:"))
#         print(students[index],f'are working this week')
#         week=(input("Enter the week type:"))
#         index+=1
        
if (week=='week1') and (b=="Kaya"):
    print(week1["Kaya"],f'are working this week')
elif((week=='week1') and (b=="Serving Area")):
    print(week1["Serving Area"],f'are working this week')
elif (week=='week1') and (b=="Washroom"):
    print(week1["Washroom"],f'are working this week')
elif (week=='week2') and (b=="Kaya"):
    print(week2["Kaya"],f'are working this week')
elif((week=='week2') and (b=="Serving Area")):
        print(week2["Serving Area"],f'are working this week')
elif (week=='week2') and (b=="Washroom"):
    print(week2["Washroom"],f'are working this week')
elif (week=='week3') and (b=="Kaya"):
        print(week3["Kaya"],f'are working this week')
elif((week=='week3') and (b=="Serving Area")):
    print(week3["Serving Area"],f'are working this week')
elif (week=='week3') and (b=="Washroom"):
    print(week3["Washroom"],f'are working this week')


   

   