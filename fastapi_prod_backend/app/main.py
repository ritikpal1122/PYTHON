from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import user


app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include the user router
app.include_router(user.router, prefix="/api/users", tags=["Users"])