# import required libraries
from fastapi import FastAPI
from starlette import status
from starlette.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import uvicorn

# Import controller files
from controllers.home_controller import home_router

# Initialize app to use FastAPI
app = FastAPI()
app.include_router(home_router)

# Folder to look for static files
app.mount("/static", StaticFiles(directory="./frontend/static"), name = "static")

# Redirect for home page
@app.get("/")
async def root():
    return RedirectResponse(url="/home", status_code=status.HTTP_302_FOUND)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)