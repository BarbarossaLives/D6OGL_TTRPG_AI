from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import uuid

app = FastAPI()

# Set up the templates directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to D6OGL TTRPG AI!"})

@app.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.get("/create-character", response_class=HTMLResponse)
async def create_character(request: Request):
    character = {}  # Placeholder for now
    return templates.TemplateResponse("create_character.html", {"request": request, "character": character})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8800, reload=True) 