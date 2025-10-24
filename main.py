# Importing FastAPI module
from fastapi import FastAPI

# creating an instance of FastAPI called app
app = FastAPI()

# GET method is used to get the informatin available in the directory "/" (root directory)
@app.get("/")
async def root(): # Can also use just def root():
    return {"message": "hello world"} # This is the message we see when the file is hosted in LocalHost