from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## Static Assets
@app.get("/")
def returnIndex():
    return FileResponse('./assets/index.html')

@app.get("/assets/index-fbf8f891.js")
def returnJsAsset():
    return FileResponse(f'./assets/index-fbf8f891.js')

@app.get("/assets/index-2a0eab78.css")
def returnCssAsset():
    return FileResponse(f'./assets/index-2a0eab78.css')

