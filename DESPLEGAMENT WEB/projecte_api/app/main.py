from fastapi import FastAPI
from datetime import date, datetime
app = FastAPI()

@app.get("/")
def hola():
    return {"message": "Raul Garcia Magro"}


@app.get("/edat1")
def edat():
    n = datetime.strptime("2006-09-18","%Y-%m-%d").date(); a=date.today()
    return {"edat": a.year-n.year-((a.month,a.day)<(n.month,n.day))}

@app.get("/edat2")
def edat():
    n = datetime.strptime("1967-02-01","%Y-%m-%d").date(); a=date.today()
    return {"edat": a.year-n.year-((a.month,a.day)<(n.month,n.day))}