from fastapi import FastAPI
from routers import todos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(todos.router)
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8888)
