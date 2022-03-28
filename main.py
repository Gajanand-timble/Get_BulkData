from fastapi import FastAPI, status, HTTPException
from GBase import GBase , Query
from json import load

app = FastAPI()
db    = GBase("database.json")
table = db.table("employee")

@app.get("/{name}")
def get_name(name: str):
    employee = Query()
    if table.contains((employee.FName==name)):
        return table.search((employee.FName==name))[0]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with name: {name} not found.")
