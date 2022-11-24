from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from generate_fpdf import GetPDF

app = FastAPI()


@app.get("/vps")
def main():

    payload = {
        "level": "Gundam Meister",
        "fullname": "Setsuna F. Seiei",
        "dept": "Celestial Being",
        "tel": "01-234-5678",
        "desc": "ทำการทดสอบระบบ",
        "email": "email@domain.com",
        "date": "2022-11-24",
        "os": "windows server 2012",
        "vcpu": "2",
        "memory": "4",
        "disk": "100",
        "domain": "www.celestial-being.org"
    }

    buffer = GetPDF(payload)

    response = StreamingResponse(buffer, media_type="application/pdf")
    response.headers["Content-Disposition"] = "inline; filename=pdfFile.pdf"
    # response.headers["Content-Disposition"] = "attachment; filename=pdfFile.pdf"
    return response
