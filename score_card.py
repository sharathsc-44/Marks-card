class Student:
    def __init__(self, name, usn):
        self.name = name
        self.usn = usn
        self.marks = []
        self.total = 0
        self.percentage = 0

    def getMarks(self):
        for j in range (sub_no):
            w = int(input(f"Enter marks for subject {j+1}: "))
            (self.marks).append(w)

    def calculateTotal(self):
        self.total = sum(self.marks)
        self.percentage = self.total / sub_no

    def display(self):
        cll = str("XXXXX Institute of technology & Management")
        print("Scorecard".rjust(81))
        print(
            '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(cll.center(150, ' '))
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')


        print(f"Name  :  ",self.name,"USN  :".rjust(140) , self.usn.rjust(0))
        # print(f"Name      : {self.name}")
        # print(f"USN       : {self.usn}")
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print("SI.no".rjust(10), "Subject".rjust(35), "Marks".rjust(90))
        for i in range (sub_no):
            print(f"{i+1}".rjust(10),sub[i].rjust(35),f"{self.marks[i]}".rjust(90))
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(f"Total     :  {self.total}".rjust(130))
        print(f"Percentage  : {self.percentage:.2f} %".rjust(130))
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('                                              PDF format of MARKS CARD is also created as  " NAME.PDF "')
        import PyPDF2
        from fpdf import FPDF

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('helvetica', size=16)
        pdf.cell(200, 0,
                 txt='--------------------------------------------------------------------------------------------------',
                 ln=1)
        n = "                          XXXXXX Institute of Technology & Mangement"

        pdf.cell(200, 20, txt=n, ln=2, align='c')
        pdf.cell(200, 0,txt='--------------------------------------------------------------------------------------------------', ln=3)
        pdf.set_font('Arial', size=12)
        pdf.cell(100, 30, txt=f'NAME : {self.name}'.rjust(10) + f'USN : {self.usn}'.rjust(110), ln=4)
        # pdf.cell(10,0,txt='Branch : ECE'.rjust(10),ln=5)
        pdf.set_font('helvetica', size=16)
        pdf.cell(200, 0,txt='--------------------------------------------------------------------------------------------------', ln=5)
        pdf.set_font('Arial', size=12)
        pdf.cell(100, 30, txt='SI. no.'.center(10) + 'Name'.rjust(35) + 'Marks'.rjust(90), ln=6)
        w = sub_no
        for i in range(sub_no):
            mrk = str(self.marks[i])
            pdf.cell(100, 10, txt=f'{i + 1}'.rjust(10) + sub[i].rjust(35) + mrk.rjust(90), ln=(i + 7))
        pdf.set_font('helvetica', size=16)
        pdf.cell(200, 0, txt='--------------------------------------------------------------------------------------------------',ln=((w + 7) + 1))
        pdf.set_font('Arial', size=12)
        pdf.cell(100, 20, txt='Total : '.rjust(10) + f'{self.total}'.rjust(130), ln=((w + 7) + 2))
        pdf.set_font('Arial', size=12)
        pdf.cell(100, 0, txt='Percentage : '.rjust(10) + f'{self.percentage} %'.rjust(120), ln=((w + 7) + 3))
        pdf.set_font('helvetica', size=16)
        pdf.cell(200, 20,txt='--------------------------------------------------------------------------------------------------', ln=13)
        pdf.set_font('helvetica', size=16)
        pdf.cell(200, 0, txt='                                       * * CONGRATULATIONS  * *', ln=14)
        pdf.set_font('helvetica', size=16)
        pdf.cell(200, 20,txt='--------------------------------------------------------------------------------------------------',ln=15)
        pdf.output(f'{self.name}.pdf')


# main program
name = input("Enter student name: ")
usn = input("Enter student USN: ")
global sub_no
sub_no = int(input('Enter the number of subjects : '))
global sub
sub= []
for j in range(sub_no):
    s = input(f"Enter name of sub {j+1} : ")
    sub.append(s)



student = Student(name, usn)
student.getMarks()
student.calculateTotal()
student.display()
