from fpdf import FPDF
from math import ceil
import io


class PDF(FPDF):
    def __init__(self, **kwargs):
        super(PDF, self).__init__(**kwargs)
        self.add_font("prompt", "", "./fonts/Prompt-Regular.ttf", uni=True)
        self.add_font("th", "", "./fonts/THSarabunNew.ttf", uni=True)
        self.add_font("th", "B", "./fonts/THSarabunNewBold.ttf", uni=True)

    def header(self):
        # Logo
        self.set_font('th', '', 12)
        self.image('./logo/xlogo.jpg', 11, 20.8, 18)

        nx = 100000
        # Line break
        self.cell(0, 10, f'Job No. __{nx}__(สำหรับเจ้าหน้าที่)', 0, 1, 'R')
        self.set_font('th', 'B', 14)

        self.cell(w=20, h=20, txt="", border=1)
        self.cell(w=0, h=10, txt="การขอรับบริการ Virtual Private Server / domain",
                  border='T,R,B', ln=2, align='C')
        self.set_font('th', '', 14)
        self.cell(w=0, h=10, txt="สำนักเทคโนโลยีดิจิทัลและสารสนเทศ",
                  border='B, R', align='C', ln=1)
        # space(self)

    # Page footer

    def footer(self):
        # Position at 1.5 cm from bottom
        # self.cell(0, 0, "", 'T', 1)
        self.set_y(-15)
        # Arial italic 8
        self.set_font('th', '', 12)
        # Page number
        self.cell(0, 10, 'IDT-FM-IF-010 (05/05/2022) หน้า ' +
                  str(self.page_no()) + '/{nb}', 0, 0, 'R')


def get_xy(obj: FPDF):
    return f"x:{ceil(obj.get_x())}, y:{ceil(obj.get_y())}"


def space(obj: FPDF):
    return obj.cell(w=0, h=10, border='L, R', ln=1)


def GetPDF(object):
    pdf = PDF(orientation="P", unit="mm", format="A4")
    # pdf = PDF(orientation="P", unit="mm", format="Letter")
    pdf.alias_nb_pages()
    pdf.add_page()

    fontSize = 14

    # effective_page_width = pdf.w - 2*pdf.l_margin

    TextHeader2(pdf, "1. ส่วนงาน: ", 18, object["dept"])
    TextHeader1(pdf, "2. ข้อมูลผู้ดูแลระบบหรือผู้ประสานงานของหน่วยงาน")
    # for i in range(1, 5):
    Paragraph(pdf, "ชื่อ-นามสกุล", object["fullname"], 5, 8)
    Paragraph(pdf, "ตำแหน่ง", object["level"], 5, 8)
    Paragraph(pdf, "โทรศัพท์", object["tel"], 5, 8)
    Paragraph(pdf, "อีเมล", object["email"], 5, 8)

    pdf.cell(0, 5, "", 'L,R', 1)

    TextHeader1(pdf, "3. รายละเอียด Virtual Private Server")
    # for i in range(1, 5):
    Paragraph(pdf, "เพื่อใช้งาน", object["desc"], 5, 8)
    Paragraph(pdf, "เริ่มใช้งานวันที่", object["date"], 5, 8)
    Paragraph(pdf, "ระบบปฏิบัติการ", object["os"], 5, 8)
    # Paragraph(pdf, "server info", "ระบบ", 5, 8)
    cpu = object["vcpu"]
    memory = object["memory"]
    disk = object["disk"]

    pdf.cell(5, 8, "", 'L')
    pdf.cell(
        0, 8, txt=f"รายละเอียด: {cpu} vCPUs, Memory: {memory} GB, HDD: {disk} GB", ln=1, border="R")

    pdf.cell(
        0, 9, "หากมีข้อสงสัยในการกรอกข้อมูล ติดต่อสอบถามได้ที่ โทร 02-727-3246", 'L,R', 1)
    pdf.cell(0, 1, "", 'L,R, B', 1)

    TextHeader2(pdf, "4. ชื่อโดเมน: ", 20, object["domain"])

    pdf.set_font("th", 'B', fontSize)
    pdf.cell(0, 10, "5. ข้าพเจ้ารับทราบนโยบาย และยินดีจะรับผิดชอบต่อความเสียหายที่เกิดขึ้นตาม พระราชบัญญัติว่าด้วยการกระทำ", 'L, R, T', 1)
    pdf.cell(0, 3, "   ความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. 2550 และที่แก้ไขเพิ่มเติม อย่างเคร่งครัดทุกประการ", 'L,R', 1)
    pdf.cell(0, 5, "", 'L,R', 1)

    TextSigned(pdf)
    pdf.cell(0, 3, "", 'L,R', 1)

    TextStaff(pdf)

    # pdf.cell(w=0, h=5, txt="", border="L,R", ln=1)

    ret = pdf.output(dest='S')

    return io.BytesIO(ret)


def Paragraph(pdf: PDF, key: str, value: str, indent: int, h: int):
    pdf.cell(w=indent, h=h, border='L', txt="")
    pdf.cell(w=0, h=h, txt=f"{key}: {value}", border='R', ln=1)


def TextHeader1(pdf: PDF, message: str):
    fontSize = 14
    hY = 10
    pdf.set_font("th", 'B', fontSize)
    pdf.cell(0, hY, message, 'L, R, T', 1, 'L')
    pdf.set_font("th", '', fontSize)


def TextHeader2(pdf: PDF, message: str, mSize: int, info: str):
    fontSize = 14
    hY = 10
    pdf.set_font("th", 'B', fontSize)
    pdf.cell(mSize, hY, message, 'L', 0, 'L')
    pdf.set_font("th", '', fontSize)
    pdf.cell(0, hY, info, 'R', 1, 'L')


def TextSigned(obj: PDF):
    hY = 8
    fontSize = 14
    border = 'L, R'
    obj.set_font("th", '', fontSize)
    obj.cell(0, hY, f"ลงชื่อ ________________________    ", border, 1, 'R')
    obj.cell(0, hY, "(______________________)    ", border, 1, 'R')
    obj.cell(0, hY, "ตำแหน่ง ____________________________    ", border, 1, 'R')
    obj.cell(0, hY, "( คณบดี / ผู้อำนวยการ หรือเทียบเท่า )    ", border, 1, 'R')
    obj.cell(0, hY, "วันที่ ________/________/________    ", border, 1, 'R')


def TextStaff(obj: PDF):
    fontSize = 14
    h = 8
    boxw = 80
    obj.set_font("th", 'B', 14)
    obj.cell(boxw, h, txt="6. ความเห็นเจ้าหน้าที่", border='L, T, R')
    obj.cell(0, h, txt="7. ความเห็นของ ผู้อำนวยการสำนักเทคโนโลยีดิจิทัลและสารสนเทศ",
             border='L,R, T', ln=1, align='C')

    obj.set_font("th", '', fontSize)
    obj.cell(boxw, h, txt="_______________________________________    ", border='L,R', align='R')
    obj.cell(0, h, txt="[ ] อนุมัติ   [ ] ไม่อนุมัติ",
             border='L,R', ln=1, align='C')

    obj.cell(boxw, h, txt="นัดส่งมอบวันที่ ________/________/________    ",
             border='L,R', align='R')
    obj.cell(0, h, txt="",
             border='L,R', ln=1, align='C')

    obj.cell(boxw, h, txt="ลงนาม __________________________    ",
             border='L,R', align='R')
    obj.cell(0, h, txt="ลงนาม _____________________________________",
             border='L,R', ln=1, align='C')

    obj.cell(boxw, h, txt="(_______________________)    ",
             border='L,R', align='R')
    obj.cell(0, h, txt="(_______________________)    ",
             border='L,R', ln=1, align='C')

    obj.cell(boxw, h, txt="วันที่ ________/________/________    ",
             border='L,R', align='R')
    obj.cell(0, h, txt="วันที่ ________/________/________ ", border='L,R', ln=1, align='C')

    obj.cell(boxw, h, txt="", border='L,R, B', align='R')
    obj.cell(0, h, txt="", border='L,R,B', align='C')
