from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from generate_pdf import GetPDF

import io

app = FastAPI()


@app.get("/")
def main():

    buffer = GetPDF()


    response = StreamingResponse(buffer, media_type="application/pdf")
    response.headers["Content-Disposition"] = "inline; filename=pdfFile.pdf"
    return response