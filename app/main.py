from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(title="Simple WMS API", version="1.0.0")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/api/suppliers", tags=["Supplier"])
async def get_suppliers():
    return [{"id": 1, "name": "供應商 A", "phone": "0912345678"}]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", reload=True)