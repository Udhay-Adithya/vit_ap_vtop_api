from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from .routers import (
    auth,
    calendar,
    course_page,
    digital_assignments,
    faculty,
    student_data,
)

app = FastAPI(
    title="VIT-AP VTOP API",
    description="A FastAPI wrapper for the vitap-vtop-client library, designed to help students access their academic information programmatically",
    version="0.3.0",
    contact={
        "name": "Know more about VITAP Student Project",
        "url": "https://vitap.udhay-adithya.me",
    },
)

# allow_credentials=True with allow_origins=["*"] is not a valid combination:
# browsers reject a wildcard on a credentialed request, so Starlette drops the
# header and every cross-origin call fails. Nothing here uses cookies -- the
# session travels in the request body and the key in a header -- so the
# wildcard is what we actually want, without credentials.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(student_data.router)
app.include_router(calendar.router)
app.include_router(faculty.router)
app.include_router(course_page.router)
app.include_router(digital_assignments.router)


@app.get("/")
async def read_root():
    return {
        "message": f"Welcome to VITAP VTOP API. Check out {app.docs_url} to get started."
    }
