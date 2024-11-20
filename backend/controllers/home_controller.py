# import required packages
import sys
sys.path.append("../frontend/")
from fastapi.responses import RedirectResponse
# from typing import Optional
# from bson import ObjectId
from starlette import status
# from controllers.auth_controller import get_current_user
# from pymongo import MongoClient
from fastapi import APIRouter, Form, Request, HTTPException, Body
from fastapi.templating import Jinja2Templates
import os
# from dotenv import load_dotenv
import json
# from utils.get_geo_object import get_geo_object
# import datetime
# import uuid

# Connect to database
# conn = MongoClient()
# db = conn.startdb()
# places = db.get_collection("places")
# users = db.get_collection("users")
# comments = db.get_collection("comments")
# load_dotenv()
# token = os.environ['API_KEY']

# Create router for '/home'
home_router = APIRouter(
    prefix="/home", tags=["home"], responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)

# Jinja templates path
templates = Jinja2Templates(directory="./frontend/templates")

# Get /home
@home_router.get("/", response_model_by_alias=False, status_code=status.HTTP_200_OK)
async def read_home(request: Request):
    try:
        print("hi")
        return templates.TemplateResponse("home.html", {"request": request})
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="server error")