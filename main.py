from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - 25-api-collections-coll-0bfe69e2729c433797c8d6394bc9808b',debug=False,docs_url='/nostalgic-omkar-0b98cde4c12911efa4030242ac1200055/docs',openapi_url='/nostalgic-omkar-0b98cde4c12911efa4030242ac1200055/openapi.json')

app.include_router(router, prefix='/nostalgic-omkar-0b98cde4c12911efa4030242ac1200055/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()