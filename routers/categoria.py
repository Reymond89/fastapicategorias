from weakref import ref
from fastapi import APIRouter, Response
from config.db import coon
from models.categoria import categories
from schemas.categoria import Category
from starlette.status import HTTP_204_NO_CONTENT

category = APIRouter()

@category.get('/categorias')
def get_cateries():
    return coon.execute(categories.select()).fetchall()

@category.post('/categorias')
def create_categoria(category: Category):
    new_category = {"ref":category.ref, "name": category.name}
    result = coon.execute(categories.insert().values(new_category))
    return coon.execute(categories.select().where(categories.c.id == result.lastrowid)).first()

@category.get('/categorias/{id}')
def get_category(id : str):
    return coon.execute(categories.select().where(categories.c.id == id)).first()

@category.put('/categorias/{id}')
def update_category(id: str, category: Category):
    coon.execute(categories.update().values(ref = category.ref, name = category.name).where(categories.c.id == id))
    return "updated"

@category.delete('/categorias/{id}')
def get_delete(id: str):
    coon.execute(categories.delete().where(categories.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
    


