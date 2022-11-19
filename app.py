#!/usr/bin/python3
# """ POST ENDPOINT FOR ACCOUNT STATEMENT """
# from fastapi import FastAPI, File, UploadFile
# # from models import Account_statement

# app = FastAPI()


# @app.post("/upload")
# def upload(file: UploadFile = File(...)):
#     """ Uploads file to database """
#     try:
#         contents = file.file.read()
#         with open(file.filename, 'wb') as f:
#             f.write(contents)
#     except Exception:
#         return {"message": "There was an error uploading the file"}
#     finally:
#         file.file.close()
#     return {"message": f"Successfully uploaded {file.filename}"}
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

allow_headers=["*"]
)

@app.get("/", status_code=200)
def html_response():
    html_content = """ 
        <html>
        <head>
            <title>Account Pal</title>
        </head>
        <body>
            <h1>Welcome to Account Pal 🙂</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/", status_code=200, response_class=HTMLResponse)
def landing_page():
    return html_response()
