class cashieringsystem:

    def __init__(self, a=0, r=0,receive=0,change=0,temp=0):

        print("\n\n*****WELCOME TO SAM'S CASHIERING SYSTEM*****\n")

        self.a = a
        self.r = r
        self.recieve = receive
        self.change = change
        self.temp = temp


    def foods(self):

        print("*****SAM'S RESTAURANT MENU*****")

        print("1.Chapati----->20", "\n2.Rice----->40", "\n3.Mukimo--->80", "\n4.Beans/Ndengu---->40","\n5.Pork 1/4----->100","\n6.Ugali----->30","\n7.Minji----->70","\n8.Cabbage----->20","\n9.Kienyeji----->40", "\n10.Done ", "\n11.Exit")

        while (1):

            c = int(input("Choose:\n"))

            if (c == 1):

                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 20 * d

            elif (c == 2):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 40 * d

            elif (c == 3):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 80 * d

            elif (c == 4):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 40 * d

            elif (c == 5):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 100 * d

            elif (c == 6):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 30 * d

            elif (c == 7):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 70 * d

            elif (c == 8):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 20 * d

            elif (c == 9):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 40 * d

            elif (c == 10):
                print("Total:", self.r)
                if (self.r > 0):
                    receive = int(input("Input Money Paid:\n"))
                    change = receive - self.r
                    while change >= 0:

                        print("Change: KShs. {} \n\n *****Thank You & Please Come Again!!!*****".format(change))
                        quit()

            elif (c == 11):
                quit()
            else:
                print("Invalid option")
                c = int(input("Choose:\n"))

def main():
    a = cashieringsystem()

    while (1):

            a.foods()

main()
