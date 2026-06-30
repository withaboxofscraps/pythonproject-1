import json
try:
    with open("tryagainn.json")as f:
        lst=json.load(f)
except:
    lst=[]
student={
    'name':'',
    'age':'',
    'grade':''
    }
def adddata():
    student['name']=input("enter the name of the student: ")
    student['age']=input("enter the age of the student: ")
    student['grade']=input("what grade is he/she in? ")
    lst.append(student.copy())
    print("data added successfully")
    with open("tryagain.json","w") as f:
        json.dump(lst,f)

def update():
    name=input("whose data you wan't to change? ")
    olddata=input(f"what do you want to change?")
    newdata=input("enter the new data")
    for i in lst:
      if i['name']==name:
          i[olddata]=newdata
   
    with open("tryagain.json","w") as f:
      json.dump(lst,f)


def deletedata():
    jay=input("what do you want to delete? ")
    for j in lst:
        if j['name']==jay:
            lst.remove(j)
    with open("tryagain.json","w") as f:
        json.dump(lst,f)

def view():
    for i in lst:
      print(f"{i['name']}\t{i['age']}\t{i['grade']}")

def search():

    jk=input("whose data you want to delete? ")

    for k in lst:
        if k['name']==jk:
            print(f"{k['name']}\t{k['age']}\t{k['grade']}")



print("-------STUDENT MANAGEMENT SYSTEM-------\n",
      "1-add data\n"
      "2-delete data\n"
      "3-search data\n"
      "4-update data\n"
      "5-view data")

while True:
    ans=input("what we doing today bro?")
    if ans=='1':
       adddata()
    elif ans=='2':
       deletedata()
    elif ans=='3':
       search()
    elif ans=='4':
       update()
    elif ans=='5':
       view()
    else:
       print("thank you broskies")
       break