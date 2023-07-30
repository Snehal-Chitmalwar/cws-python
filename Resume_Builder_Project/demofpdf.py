# # # # from fpdf import FPDF

# # # # pdf = FPDF()
# # # # pdf.add_page()
# # # # pdf.set_font('Arial', 'B', 16)
# # # # pdf.cell(40, 10, 'Hello World!')
# # # # pdf.output('tuto1.pdf', 'F')

# # # from fpdf import FPDF


# # # class PDF(FPDF):
# # #     def header(self):
# # #         # Logo
# # #         # self.image('logo_pb.png', 10, 8, 33)
# # #         # Arial bold 15
# # #         self.set_font('Arial', 'B', 15)
# # #         # Move to the right
# # #         self.cell(80)
# # #         # Title
# # #         self.cell(30, 10, 'Title', 1, 0, 'C')
# # #         # Line break
# # #         self.ln(20)

# # #     # Page footer
# # #     def footer(self):
# # #         # Position at 1.5 cm from bottom
# # #         self.set_y(-15)
# # #         # Arial italic 8
# # #         self.set_font('Arial', 'I', 8)
# # #         # Page number
# # #         self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


# # # # Instantiation of inherited class
# # # pdf = PDF()
# # # pdf.alias_nb_pages()
# # # pdf.add_page()
# # # pdf.set_font('Times', '', 12)
# # # for i in range(1, 41):
# # #     pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
# # # pdf.output('tuto2.pdf', 'F')
# # from fpdf import FPDF

# # title = '20000 Leagues Under the Seas'


# # class PDF(FPDF):
# #     def header(self):
# #         # Arial bold 15
# #         self.set_font('Arial', 'B', 15)
# #         # Calculate width of title and position
# #         w = self.get_string_width(title) + 6
# #         self.set_x((210 - w) / 2)
# #         # Colors of frame, background and text
# #         self.set_draw_color(0, 80, 180)
# #         self.set_fill_color(230, 230, 0)
# #         self.set_text_color(220, 50, 50)
# #         # Thickness of frame (1 mm)
# #         self.set_line_width(1)
# #         # Title
# #         self.cell(w, 9, title, 1, 1, 'C', 1)
# #         # Line break
# #         self.ln(10)

# #     def footer(self):
# #         # Position at 1.5 cm from bottom
# #         self.set_y(-15)
# #         # Arial italic 8
# #         self.set_font('Arial', 'I', 8)
# #         # Text color in gray
# #         self.set_text_color(128)
# #         # Page number
# #         self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

# #     def chapter_title(self, num, label):
# #         # Arial 12
# #         self.set_font('Arial', '', 12)
# #         # Background color
# #         self.set_fill_color(200, 220, 255)
# #         # Title
# #         self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
# #         # Line break
# #         self.ln(4)

# #     def chapter_body(self, name):
# #         # Read text file
# #         with open(name, 'rb') as fh:
# #             txt = fh.read().decode('latin-1')
# #         # Times 12
# #         self.set_font('Times', '', 12)
# #         # Output justified text
# #         self.multi_cell(0, 5, txt)
# #         # Line break
# #         self.ln()
# #         # Mention in italics
# #         self.set_font('', 'I')
# #         self.cell(0, 5, '(end of excerpt)')

# #     def print_chapter(self, num, title, name):
# #         self.add_page()
# #         self.chapter_title(num, title)
# #         self.chapter_body(name)


# # pdf = PDF()
# # pdf.set_title(title)
# # pdf.set_author('Jules Verne')
# # pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_c1.txt')
# # pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
# # pdf.output('tuto3.pdf', 'F')
# from fpdf import FPDF

# pdf = FPDF()
# pdf.set_font("helvetica", size=24)
# pdf.add_page()
# # pdf.cell(w=1, txt="Welcome on first page!", align="C")
# # pdf.add_page()
# # link = pdf.add_link(page=1)
# # pdf.cell(txt="Internal link to first page", border=1, link=link)
# # pdf.output("internal_link.pdf")

# link1 = pdf.link(x=0, y=0, w=9, h=1, link="https://github.com/PyFPDF/fpdf2")
# # pdf.cell(9, 0, txt="Internal link to first page", border=1, link=link1)
# pdf.output('tuto4.pdf', 'F')
# from fpdf import FPDF


# class MyFPDF(FPDF):
#     def hyperlink(self, link_text, url):
#         self.set_text_color(70, 150, 50)
#         self.set_font("helvetica", "B", 16)
#         self.write(5, link_text, url)


# def main() -> None:
# pdf = MyFPDF()
# pdf.add_page()
# str = pdf.hyperlink('pyfpdf.github.io/fpdf2/',
#                     'https://pyfpdf.github.io/fpdf2/')
# strDetailHeader = str+" mygkgckg"
# pdf.cell(0, 9, strDetailHeader, 0, 1, 'C')


# pdf.set_font('Arial', '', 14)
# pdf.write(5, 'Visit ')
# # Then put a blue underlined link
# pdf.set_text_color(0, 0, 255)
# pdf.set_font('', 'U')
# pdf.write(5, 'www.fpdf.org', 'http://www.fpdf.org')
# pdf.output("test1.pdf")
