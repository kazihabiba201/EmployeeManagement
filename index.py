from fastapi import FastAPI
from routes.user import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(host="0.0.0.0", port=8080)
app.include_router(user)



from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://10.0.2.2"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
