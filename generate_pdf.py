from fpdf import FPDF
import io


class PDF(FPDF):
    def __init__(self, **kwargs):
        super(PDF, self).__init__(**kwargs)
        self.add_font("prompt", "", "./fonts/Prompt-Regular.ttf", uni=True)
        self.add_font("th", "", "./fonts/THSarabunNew.ttf", uni=True)

    def header(self):
        # Logo
        b = 0

        self.set_font('prompt', '', 14)

        self.cell(0, 10, '', 0, 1)
        self.image('./logo/xlogo.jpg', 10, 15, 25)
        # Arial bold 15
        self.cell(0, 10, "No. 6123123", b, 1, 'R')
        self.cell(0, 10, "วันที่ 11 xxxx 2565", b, 1, 'R')
        # Move to the right
        # self.cell(80)
        # Title
        self.cell(0, 10, '', 0, 1)
        self.cell(30, 10, 'Title', 1, 0, 'C')
        self.cell(
            0, 10, "แบบฟอร์มการขอเปลี่ยนแปลงระบบ (Change Request Form)", 1, 1, 'C')
        self.cell(0, 10, "สํานักเทคโนโลยีดิจิทัลและสารสนเทศ", 1, 1, 'C')

        # Line break
        self.ln(5)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('th', '', 14)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def GetPDF():
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.alias_nb_pages()
    pdf.add_page()

    b = 1
    h = 15
    pdf.set_font("th", '', 18)

    loremipsum = """Lorem ipsum dolor sit amet, vel ne quando dissentias. \
    Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
    menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi \
    ut. At mea wisi dolorum contentiones, in malis vitae viderer mel.

    Vis at dolores ocurreret splendide. Noster dolorum repudiare vis ei, te \
    augue summo vis. An vim quas torquatos, electram posidonium eam ea, eros \
    blandit ea vel. Reque summo assueverit an sit. Sed nibh conceptam cu, pro \
    in graeci ancillae constituto, eam eu oratio soleat instructior. No deleniti \
    quaerendum vim, assum saepe munere ea vis, te tale tempor sit. An sed debet \
    ocurreret adversarium, ne enim docendi mandamus sea.
    """

    test_long_text = "oqewurpouerpoiuwerpouwperoiuqwriuwpourpqwieourpowieurpqourepoiuerpourepoiuwerpowqiueproiuwperiuqwpeirupwoiruqwpouerpiruqpwouerpwoeurpqwer"

    effective_page_width = pdf.w - 2*pdf.l_margin

    # Body
    # pdf.cell(0, 10, "body: ", 0, 0, 'L')

    pdf.multi_cell(effective_page_width, 10, test_long_text, ln=1)

    # pdf.cell(120, 10, "Hello world", border=1)
    pdf.cell(0, h, "Good bye world: testsetst", border=b, ln=1)
    # pdf.ln(5)
    pdf.cell(0, h, "Good bye world: testsetst", border=b, ln=1)

    pdf.cell(15, h, "Body:", border=b)
    pdf.cell(120, h, "eirtuporieutwpoiurtpoewrt", border=b, ln=1)

    pdf.cell(20, h, "long text:", border=b)
    pdf.multi_cell(effective_page_width, 20, test_long_text, ln=1, border=1)
 
    # pdf.cell(120, 10, "Hello world", border=1)
    # pdf.cell(70, 10, "Good bye world", border=1)

    # pdf.cell(190, 10, "center", align="C", ln=1)
    # pdf.cell(190, 10, "center", align="C")

    # pdf.line(0, 20, 190, 20)
    # pdf.dashed_line(10, 30, 110, 30, 1, 10)
    # for i in range(1, 100):
    #     pdf.cell(0, 10, f"ไทย บรรทัดที่: {i}", ln=1, border=1)

    # pdf.set_font("th", '', 18)
    # pdf.cell(30, 20, "สารบัญ", ln=1, border=1)

    ret = pdf.output(dest='S')

    return io.BytesIO(ret)
