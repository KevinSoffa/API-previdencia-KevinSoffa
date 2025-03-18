from fastapi.middleware.cors import CORSMiddleware
from controller import router
from fastapi import FastAPI


app = FastAPI(title="Kevin Soffa | Plano de previdência")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
