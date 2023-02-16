#To-do app

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

#Root
@app.get("/")
def root():
    return "Hi"


Todos = {
    1 : {
        "title": "DBMS CASE STUDY",
        "compeleted" : False,
    },
    2 : {
        "title": "Complete todo app",
        "completed" : False,
    }
}


#Request body schema
class TodoItem(BaseModel):
    title: str
    completed: bool


#Endpoints

#1. view all the existing todo items
@app.get("/todos", status_code=status.HTTP_200_OK)
def get_all_todo_items(title: str = ""):
    results = {}
    if title != "" or title != None:
        for id in Todos:
            if title in Todos[id]["title"]:
                results[id] = Todos[id]
    else:
        results = Todos

    return results


#viewing single item
@app.get("/todos/{id}", status_code=status.HTTP_200_OK)
def get_todo_item(id: int):
    if id in Todos:
        return Todos[id]
    
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item is not found")


#2. creating todo items
@app.post("/todos", status_code=status.HTTP_200_OK)
def create_todo_items(todo_item: TodoItem):
    id=max(Todos)+1
    Todos[id] = todo_item.dict()
    return Todos[id]


#3. Update todo item
@app.put("/todos/{id}", status_code=status.HTTP_200_OK)
def update_todo_item(id: int, todo_item: TodoItem):
    if id in Todos:
        Todos[id] = todo_item.dict()
        return Todos[id]
    
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item is not found")
    


#4. Delete todo item
@app.delete("/todos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_items(id: int):
    if id in Todos:
        Todos.pop(id)
        return

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item is not found")
