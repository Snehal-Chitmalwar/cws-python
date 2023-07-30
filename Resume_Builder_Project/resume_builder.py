from fpdf import FPDF
from math import *
from array import *


class PDF(FPDF):
    def resumeName(self):
        # Arial bold-underlined 15
        self.set_font('Arial', 'BU', 18)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_text_color(0, 0, 0)
        # Title
        self.cell(w, 20, title, 0, 1, 'C')
        # Line break
        self.ln(1)

    def detailHeader(self, current_location, emailId, phoneNo, linkedIn):
        self.location = current_location
        self.email = emailId
        self.phone = phoneNo
        self.linkedInLink = linkedIn
        strDetailHeader = self.location+" | "+self.email + \
            " | "+self.phone+" | "+self.linkedInLink
        # Arial 9
        self.set_font('Arial', '', 9)
        # Calculate width of title and position
        w = self.get_string_width(strDetailHeader)+6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_text_color(0, 0, 0)
        # Title
        self.write(9, self.location+" | ")
        # Then put a blue underlined link
        pdf.set_text_color(0, 0, 255)
        pdf.set_font('Arial', 'U', 9)
        # pdf.write(9, self.email, self.email)
        pdf.write(9, self.email, f"mailto:{self.email}")
        # Arial 9
        self.set_font('Arial', '', 9)
        # Colors of frame, background and text
        self.set_text_color(0, 0, 0)
        self.write(9, " | "+self.phone+" | ")
        # Then put a blue underlined link
        pdf.set_text_color(0, 0, 255)
        pdf.set_font('Arial', 'U', 9)
        pdf.write(9, self.linkedInLink, "https://www."+self.linkedInLink+"/")
        pdf.set_text_color(0, 0, 255)
        pdf.set_font('Arial', '', 9)
        # Line break
        self.ln(10)

    def appreciationComment(self, strAppreciation, strPresenter, strDesignation, strCompany):
        self.appreciation = strAppreciation
        self.presenter = strPresenter
        self.designation = strDesignation
        self.company = strCompany
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'I', 10)
        self.multi_cell(0, 9, self.appreciation)
        # Line break
        self.ln(1)
        self.set_font('Arial', '', 10)
        self.cell(0, 9, "~ "+self.presenter+", " +
                        self.designation+", "+self.company, 0, 1, 'R')
        # Line break
        self.ln(10)

    def resumeHeadings(self, label):
        self.headingLabel = label
        # Arial 12
        self.set_font('Arial', 'B', 11)
        # Background color
        self.set_text_color(0, 0, 139)
        # Title
        self.cell(0, 6, self.headingLabel, 0, 1, 'L')
        self.set_draw_color(0, 0, 139)
        self.line(self.get_x(), self.get_y(), self.get_x()+170, self.get_y())
        # Line break
        self.ln(10)

    def printSkillDetail(self, category, skill):
        self.skillCategory = category
        self.skillName = skill
        # Arial 12
        self.set_font('Arial', 'B', 10)
        self.set_text_color(0, 0, 0)
        # Title
        self.write(2, self.skillCategory + ": ")
        self.set_font('Arial', '', 10)
        self.write(2, self.skillName)
        # Line break
        self.ln(10)

    def companyExperience(self, expCompany, expCity, expCountry, expDesignation, fDate, tDate):
        self.companyExp = expCompany
        self.countryExp = expCountry
        self.cityExp = expCity
        self.designationExp = expDesignation
        self.fromDate = fDate
        self.toDate = tDate
        self.set_font('Arial', 'B', 10)
        self.set_text_color(0, 0, 139)
        strwidth = 170 - \
            self.get_string_width(
                self.companyExp+self.cityExp+","+self.countryExp)
        strspace = ""
        for i in range(floor(strwidth)):
            strspace = strspace+" "
        self.write(2, self.companyExp+strspace)
        self.write(2, self.cityExp+","+self.countryExp)
        # line break
        self.ln(7)
        self.set_font('Arial', '', 10)
        self.set_text_color(0, 0, 0)
        strwidth = 170 - \
            self.get_string_width(
                self.designationExp+self.fromDate+" - "+self.toDate)
        strspace = ""
        for i in range(floor(strwidth)):
            strspace = strspace+" "
        self.write(2, self.designationExp+strspace)
        self.write(2, self.fromDate+" - "+self.toDate)
        # line break
        self.ln(10)

    def educationDetails(self, strDegree, strCity, strCountry, strCollege, strUniversity, fDate, tDate):
        self.degree = strDegree
        self.city = strCity
        self.country = strCountry
        self.college = strCollege
        self.university = strUniversity
        self.fromDate = fDate
        self.toDate = tDate
        self.set_font('Arial', 'B', 10)
        self.set_text_color(0, 0, 139)
        strwidth = 170 - \
            self.get_string_width(
                self.degree+self.city+", "+self.country)
        strspace = ""
        for i in range(floor(strwidth)):
            strspace = strspace+" "
        self.write(2, self.degree+strspace)
        self.write(2, self.city+","+self.country)
        # line break
        self.ln(7)
        self.set_font('Arial', '', 10)
        self.set_text_color(0, 0, 0)
        strwidth = 170 - \
            self.get_string_width(
                self.college+", "+self.university+self.fromDate+" - "+self.toDate)
        strspace = ""
        for i in range(floor(strwidth)-2):
            strspace = strspace+" "
        self.write(2, self.college+", "+self.university+strspace)
        self.write(2, self.fromDate+" - "+self.toDate)
        # line break
        self.ln(13)

    def displayInternship(self, arrInternship):
        for i in arrInternship:
            self.set_text_color(0, 0, 0)
            new_xcord = self.get_x()
            self.cell(0, 5, chr(127), 0, 0, 'L')
            self.set_x(new_xcord+5)
            self.set_font("Arial", '', 10)
            self.write(5, i)
            # line break
            self.ln(10)

    def displayAchievements(self, arrAchievement):
        for i in arrAchievement:
            self.set_text_color(0, 0, 0)
            new_xcord = self.get_x()
            self.cell(0, 5, chr(127), 0, 0, 'L')
            self.set_x(new_xcord+5)
            self.set_font("Arial", '', 10)
            self.write(5, i)
            # line break
            self.ln(10)

    def displayExtraCurricular(self, arrExtraCurricular):
        for i in arrExtraCurricular:
            self.set_text_color(0, 0, 0)
            new_xcord = self.get_x()
            self.cell(0, 5, chr(127), 0, 0, 'L')
            self.set_x(new_xcord+5)
            self.set_font("Arial", '', 10)
            self.write(5, i)
            # line break
            self.ln(10)


pdf = PDF()
# add margins first
pdf.l_margin = pdf.l_margin*2.0
pdf.r_margin = pdf.r_margin*2.0
pdf.t_margin = pdf.t_margin*2.0
pdf.b_margin = pdf.b_margin*2.0
pdf.line_width = pdf.line_width*2.0

# pdf.set_auto_page_break(True, 2)

# pdf.accept_page_break()

# take inputs frm user
title = input("Enter your Name:")
location = input("Enter your current location:")
emailId = input("Enter your email Id:")
phoneNo = int(input("Enter your mobile number:"))
linkedIn = input("Enter your Linked In ID:")
strAppreciation = input(
    "Enter appreciation you received from your earlier project if any:")
if strAppreciation != "":
    strPresenter = input("Enter the Appreciation Presenter's name:")
    strDesignation = input("Enter presenter's Designation:")
    strPresenterCompany = input("Enter your company:")
pdf.add_page()
pdf.resumeName()
pdf.detailHeader(location, emailId,
                 phoneNo, linkedIn)
# strAppreciation = "Hi Snehal, thanks for your continuous support and contribution in the team. You are a quick learner; in a short span of time, you have become reliable and proactive member in the team."
# strPresenter = "Karthik Sankaran"
# strDesignation = "Automation Test Engineering Associate Manager"
# strPresenterCompany = "Accenture"
pdf.appreciationComment(strAppreciation, strPresenter,
                        strDesignation, strPresenterCompany)

pdf.resumeHeadings("SKILLS")
pdf.printSkillDetail("Certified Programming Languages", "Python, C, C++")
pdf.printSkillDetail("Database Technologies", "SQL")
pdf.printSkillDetail("Developer Environment Tool", "VS Code")
pdf.printSkillDetail("Languages Trained in",
                     "Java (Basics), VBScript, ASP .Net (MVC)")
pdf.printSkillDetail("Automation Tools",
                     "UFT, Test Complete (Execution Basics)")
pdf.printSkillDetail("Others", "OOPS, DSA")

pdf.resumeHeadings("EXPERIENCE")
pdf.companyExperience("ACCENTURE", "HYDERABAD", "INDIA",
                      "Quality Engineering Analyst", "01/21", "Ongoing")

pdf.resumeHeadings("EDUCATION")
pdf.educationDetails("BE - ELECTRONICS & TELECOMMUNICATION", "LONAVALA", "INDIA",
                     "Sinhgad Institutes of Technology", "Savitribai Phule Pune University", "Aug 2016", "Nov 2020")
pdf.educationDetails("INTERMEDIATE EDUCATION (12TH)", "HYDERABAD", "INDIA",
                     "Sri Chaitanya Junior College", "Telangana State Board", "June 2014", "April 2016")

pdf.resumeHeadings("INTERNSHIP")
# pdf.cell(0, 5, chr(127), 0, 0, 'L')
arrInternship = ["Undergone an In-Plant Training at Ordnance Factory Chanda, an ISO 9001-2008 Organization, under the human resource and development cell, basically trained to satisfy and meet the needs under electronics area."]
pdf.displayInternship(arrInternship)

pdf.resumeHeadings("ACHIEVEMENTS")
arrAchievement = [
    "Awarded 1st prize from Tadoba Nature Conservation Club at a drawing competition regarding Wildlife Week Celebration, 2013."]
pdf.displayAchievements(arrAchievement)

pdf.resumeHeadings("EXTRA - CURRICULAR ACTIVITIES")
arrExtraCurricular = ["Recognized by Head of Department for Co-ordinating various events held at college level, organized as a student branch.",
                      "Served as Department Representative in IEEE SIT Student Branch (IIT Bombay Section) for year 2018 at college.", "Served as Human resource in IEEE SIT SB (IIT Bombay Section) for year 2019 at college level."]
pdf.displayExtraCurricular(arrExtraCurricular)
# line break
pdf.ln(10)
pdf.set_font('Arial', '', 11)
pdf.set_draw_color(0, 0, 0)
pdf.line(pdf.get_x()+65, pdf.get_y(),
         pdf.get_x()+105, pdf.get_y())

pdf.output('resume.pdf', 'F')
