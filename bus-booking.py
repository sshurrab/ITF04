class bus:
    def __init__(self, fname, lname, age, dis, id):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.dis = dis
        self.id = id

    def getfname(self):
        return self.fname

    def getlname(self):
        return self.lname

    def getage(self):
        return self.age

    def getdis(self):
        return self.dis

    def getid(self):
        return self.id

class b_book:
    print("Welcom To Bus Booking Python Program")

    tikd=[]
    def addtickt(self,tikd):
        fname= input("Please Enter your first Name ")
        lname= input("Please Enter your Last Name  ")
        age= int(input("Please Enter your age      "))
        print(""" please chose your Destiniation (from 1 to 8) by enter No from the list 
                          1= "Bus Travel From Gaza To South Gov "
                          2= "Bus Travel From Gaza To Middle Gaza "
                          3= "Bus Travel From South Gov To Gaza "
                          4= "Bus Travel From South Gov To North Gaza "
                          5= "Bus Travel From North Gaza To South Gov  "
                          6= "Bus Travel From North Gaza To Middle Gaza"
                          7= "Bus Travel From Middle Gaza To South Gov "
                          8= "Bus Travel From Middle Gaza To North Gaza """)
        dis= int(input("Please choose your dis from 1 to 8      "))
        id= int(input("Please select seat No. select from 100 to 500       "))

        tik= bus(fname,lname,age,dis,id)
        tikd.append(tik)

    def check_tickt(self,tikd):
        exisit=False
        id= int(input("Please Enter your booked Seat No from 100 to 500  "))
        for i in range(len(tikd)):
            if (tikd[i].getid()==id):
                print("your tickt id is, Please Save it   ",tikd[i].getid() )
                print("your tickt details   ", tikd[i].getfname(), "",tikd[i].getlname(), "", tikd[i].getage() )
                print("your tickt destiniation No is   ", tikd[i].getdis())
                exisit=True
        if(exisit==False):
            print("Tickt Not Found!! ")

    def confirm_tickt(self,tikd):
        if(len(tikd)==0):
            print("You didnt book Yet")
        else:
            for i in range(len(tikd)):
                print(" Confirmation tick id details is listed Below " )
                print("your tickt id is   ", tikd[i].getid())
                print("your tickt details   ", tikd[i].getfname(), "", tikd[i].getlname(), "", tikd[i].getage())
                print("your tickt destiniation is   ", tikd[i].getdis())
t=b_book()
def menue():
    print("""**********Bus Booking*********
                 1.Book ticket
                 2.Search Booked Tickt Status
                 3.Confirm  booking ticket""")
    global choice
    choice = int(input("Enter your option 1 or 2 or 3 : "))

menue()

while (True):
    if (choice==1):
        t.addtickt(t.tikd)
        n=input("Do you want to quit y/n? ")
        if(n=="y"):
            break
        else:
            menue()

    elif (choice==2):
        t.check_tickt(t.tikd)
        n=input("Do you want to quit y/n? ")
        if (n=="y"):
            break
        else:
            menue()

    elif (choice==3):
        t.confirm_tickt(t.tikd)
        n=input("Do you want to quit y/n? ")
        if (n=="y"):
            break
        else:
            menue()
    else:
        print("Wrong choice, chosse 1 or 2 or 3")
        menu()



