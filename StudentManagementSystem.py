import json
try:
    with open("managementsystem.json","r") as f:
        lst=json.load(f)
except:
    lst=[]

stu={
    'name': '',
    'age': '',
    'grade': ''
 }
def addstudent():
    stu['name']=input("Enter student name:")
    stu['age']=input("Enter student age:")
    stu['grade']=input("Enter student grade:")
    lst.append(stu.copy())
    with open("managementsystem.json","w") as f:
        json.dump(lst,f)
    print('successfully')

def search():
    srh=input("what do you want to search?")
    for x in lst:
     if srh == x['name']:
      print(f"{x['name']}\t{x['age']}\t{x['grade']}")

def update():
    req=input("what do you want to update?")
    for y in lst:
     if req == "name":
         req_2=input('whose name?')
         if req_2 == y['name']:
          y['name']=input("enrter new name")
         with open("managementsystem.json","w") as f:
            json.dump(lst,f)

def delete():
    wasp = input("Whose data you want to delete? ")

    for a in lst:
      if wasp == a['name']:
        lst.remove(a)
        print("Deleted")
        break
    with open("managementsystem.json","w") as f:
        json.dump(lst,f)

def view():
    for i in lst:
     print(f"{i['name']}\t{i['age']}\t{i['grade']}")
    

print("---STUDENT MANAGEMENT SYSTEM---\n"
      "1. Add student\n"
      "2. View student\n"
      "3.search\n"
      "4.updatee\n"
      "5.delete")


while True:

 get_choice=input("what we doing today?")
 if get_choice=="1":
    addstudent()
 elif get_choice=="2":
    view()
 elif get_choice=="3":
     search()
 elif get_choice=="4":
     update()
 elif get_choice=="5":
     delete()
 else:
    break
