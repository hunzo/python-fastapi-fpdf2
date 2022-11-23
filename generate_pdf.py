from fpdf import FPDF
import io


class PDF(FPDF):
    def __init__(self, **kwargs):
        super(PDF, self).__init__(**kwargs)
        self.add_font("prompt", "", "./fonts/Prompt-Regular.ttf", uni=True)
        self.add_font("th", "", "./fonts/THSarabunNew.ttf", uni=True)
        self.add_font("th", "B", "./fonts/THSarabunNewBold.ttf", uni=True)

    def header(self):
        # Logo
        b = 0

        self.set_font('th', '', 16)

        # self.cell(0, 10, '', 0, 1)
        self.image('./logo/xlogo.jpg', 12, 20, 15)
        # Arial bold 15
        # self.cell(0, 10, "No. 6123123", b, 1, 'R')
        # self.cell(0, 10, "วันที่ 11 xxxx 2565", b, 1, 'R')
        # Move to the right
        # self.cell(80)
        # Title
        # self.cell(0, 10, '', 0, 1)
        # self.cell(30, 10, 'Title', 1, 0, 'C')
        # self.cell(
        #     0, 10, "แบบฟอร์มการขอเปลี่ยนแปลงระบบ (Change Request Form)", 1, 1, 'C')
        # self.cell(0, 10, "สํานักเทคโนโลยีดิจิทัลและสารสนเทศ", 1, 1, 'C')

        nx = 100000
        # Line break
        self.cell(0, 10, f'Job No. __{nx}__(สำหรับเจ้าหน้าที่)', 0, 1, 'R')
        self.set_font('th', 'B', 16)
        self.cell(w=20, border=0)
        self.cell(
            0, 10, "การขอรับบริการ Virtual Private Server / domain", 1, 1, 'C')
        self.set_font('th', '', 14)
        self.cell(w=20, border=0)
        self.cell(0, 7, "สำนักเทคโนโลยีดิจิทัลและสารสนเทศ", 1, 1, 'C')
        # self.ln(10)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('th', '', 12)
        # Page number
        self.cell(0, 10, 'IDT-FM-IF-010 (05/05/2022) หน้า ' +
                  str(self.page_no()) + '/{nb}', 0, 0, 'R')


def GetPDF():
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.alias_nb_pages()
    pdf.add_page()

    fontSize = 14
    hY = 10

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

    pdf.set_font("th", 'B', fontSize)
    pdf.cell(20, hY, "1. ส่วนงาน", 1, 0, 'L')
    pdf.cell(5)
    pdf.set_font("th", '', fontSize)
    pdf.cell(0, hY, "__xx__", 1, 1, 'L')

    pdf.set_font("th", 'B', fontSize)
    pdf.cell(0, hY, "2. ข้อมูลผู้ดูแลระบบหรือผู้ประสานงานของหน่วยงาน", 1, 1, 'L')
    pdf.set_font("th", '', fontSize)

    pdf.cell(5)
    pdf.cell(23, 10, "ชื่อ-นามสกุล", 1, 0, 'L')
    pdf.cell(5)
    pdf.cell(0, 10, f"{pdf.w}", 1, 1, 'L')

    pdf.cell(5)
    pdf.cell(20, 10, "ตำแหน่ง", 1, 0, 'L')
    pdf.cell(5)
    pdf.cell(0, 10, "----", 1, 1, 'L')

    pdf.cell(5)
    pdf.cell(20, 10, "โทรศัพท์", 1, 0, 'L')
    pdf.cell(5)
    pdf.cell(0, 10, "----", 1, 1, 'L')

    pdf.cell(5)
    pdf.cell(20, 10, "อีเมล", 1, 0, 'L')
    pdf.cell(5)
    pdf.cell(0, 10, "----", 1, 1, 'L')

    pdf.set_font("th", 'B', fontSize)
    pdf.cell(0, hY, "3. รายละเอียด Virtual Private Server", 1, 1, 'L')
    pdf.set_font("th", '', fontSize)

    # pdf.cell(5)
    # pdf.cell(17, 10, "เพื่อใช้งาน", 1, 0, 'L')
    # pdf.cell(5)
    # pdf.cell(0, 10, "______", 1, 1, 'L')

    TestMessage(pdf, "เพื่อใช้งาน", "website คณะ", 0)
    TestMessage(pdf, "ระบบปฏิบัติการ", "windows", 0)
    TestMessage(pdf, "เริ่มใช้งานวันที่",
                "20/11/2022 (ต้องแจ้งล่วงหน้าอย่างน้อย 3 วันทำการ)", 0)

    # pdf.cell(5)
    # pdf.cell(23, 10, "เริ่มใช้งานวันที่", 1, 0, 'L')
    # pdf.cell(5)
    # pdf.cell(30, 10, "______", 1, 0, 'L')
    # pdf.cell(0, 10, "ต้องแจ้งล่วงหน้าอย่างน้อย 3 วันทำการ", 1, 1, 'L')

    # pdf.cell(5)
    # pdf.cell(25, 10, "ระบบปฏิบัติการ", 1, 0, 'L')
    # pdf.cell(5)
    # pdf.cell(0, 10, "______", 1, 1, 'L')

    pdf.cell(10)
    pdf.cell(30, 10, "CPU: 1", 1, 0, 'L')
    pdf.cell(10)
    pdf.cell(30, 10, "Memory: 1G", 1, 0, 'L')
    pdf.cell(10)
    pdf.cell(30, 10, "HDD: 10G", 1, 1, 'L')

    pdf.cell(
        0, 10, "หากมีข้อสงสัยในการกรอกข้อมูล ติดต่อสอบถามได้ที่ โทร 02-727-3246", 1, 1, 'L')

    pdf.set_font("th", 'BU', fontSize)
    pdf.cell(20, hY, "4. ชื่อโดเมน", 1, 0, 'L')
    pdf.cell(5)
    pdf.cell(0, hY, "www.google.com", 1, 1, 'L')

    pdf.ln(5)

    pdf.set_font("th", 'B', fontSize)
    pdf.cell(0, 7, "5. ข้าพเจ้ารับทราบนโยบาย และยินดีจะรับผิดชอบต่อความเสียหายที่เกิดขึ้นตาม พระราชบัญญัติว่าด้วยการกระทำ", 0, 1, 'L')
    pdf.cell(5)
    pdf.cell(0, 7, "ความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. 2550 และที่แก้ไขเพิ่มเติม อย่างเคร่งครัดทุกประการ", 0, 1, 'L')

    pdf.ln(10)

    TestHeader(pdf, "7. ทดสอบ header")
    TestHeader(pdf, "8. ทดสอบ header")
    TestHeader(pdf, "9. ทดสอบ header")

    TestOBJ(pdf)

    ret = pdf.output(dest='S')

    return io.BytesIO(ret)


def TestMessage(pdf: PDF,  k: str, v: str, border: int):
    pdf.cell(5)
    pdf.cell(pdf.get_x() + 1, 10, k, border, 0, 'L')
    pdf.cell(5)
    pdf.cell(0, 10, v, border, 1, 'L')


def TestHeader(pdf: PDF, message: str):
    fontSize = 14
    hY = 10
    pdf.set_font("th", 'BU', fontSize)
    pdf.cell(0, hY, message, 1, 1, 'L')
    pdf.set_font("th", '', fontSize)


def TestOBJ(obj: PDF):
    hY = 10
    fontSize = 14
    border = 0
    obj.set_font("th", '', fontSize)
    obj.cell(0, hY, f"ลงชื่อ ________________________{obj.get_x()}", border, 1, 'R')
    obj.cell(0, hY, "(______________________)", border, 1, 'R')
    obj.cell(0, hY, "ตำแหน่ง ________________________", border, 1, 'R')
    obj.cell(0, hY, "( คณบดี / ผู้อำนวยการ หรือเทียบเท่า )", border, 1, 'R')
