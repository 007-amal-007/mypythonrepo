employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
    {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
    {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
    {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},

]
#1.MAP
#EACH OBJECT HAS CURRESPONDING OUTPUT

#?# print e_names only
for employee in employees:
    #employee={"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1}
    print(employee["e_name"])

# e_names=list(map(lambda employee:employee["e_name"],employees))
# print(e_names)

#? #print employee in upper case
for employee in employees:
    print(employee["e_name"].upper())

# e_upper=list(map(lambda emp:emp["e_name"].upper(),employees))
# print(e_names)

#2.FILTER
#THERE IS A CONDITION .FILTER

#?#employee name who is work as developer
for employee in employees:      #condition
    if(employee["department"]=="developer"):
        print("developer",employee["e_name"])

# developers=list(filter(lambda emp:emp["department"]=="developer",employees))
# # print(developers)
# developer_name=list(filter(lambda dev:dev["e_name"],developers))
# print(developer_name)

#3.REDUCE
#PROCESS all ,AND RESULT AS A SINGLE VALUE .we get a single value
#list having only numbers
#not directly available we have to import that module functools
#" from functools import reduce "

#?#total of salary
total=0
for employee in employees:
    total=total+employee["salary"]
print(total)

#salaries of all employees MAP
# salaries=list(map(lambda emp:emp["salary"],employees))
# print(sum(salaries))
# print(max(salaries))
# print(min(salaries))


#print employee names ,names starting with a : filter
#print highest salary : reduce
#print lowest salary  : reduce
#add bonus for all employees : map
#add bonus of 5000 rs for developers : filter

