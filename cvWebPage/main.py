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

@app.get("/assets/index-f1aa1be4.js")
def returnJsAsset():
    return FileResponse(f'./assets/index-f1aa1be4.js')

@app.get("/assets/index-d2edbefd.css")
def returnCssAsset():
    return FileResponse(f'./assets/index-d2edbefd.css')

