# malikchika86@gmail.com
from fastapi import FastAPI
from routers import fullname_router

app = FastAPI()

app.include_router(fullname_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run()




