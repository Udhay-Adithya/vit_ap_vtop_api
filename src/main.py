from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

# Import the routers and config
from routers import student_data
from config import settings

app = FastAPI(
    title="VITAP VTOP API",
    description="A FastAPI wrapper for the vitap-vtop-client library. Requires API Key and VTOP credentials per request.",
    version="0.1.0",
)

# Include routers
app.include_router(student_data.router)


@app.get("/")
async def read_root():
    return {"message": "VITAP VTOP API is running. Access docs at /docs"}


# Add a simple startup print to confirm config loading
@app.on_event("startup")
async def startup_event():
    print(
        "API Key loaded:", settings.API_KEY
    )  # Don't print the key in production logs!
