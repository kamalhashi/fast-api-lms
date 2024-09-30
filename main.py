from fastapi import FastAPI
from api import users, courses, sections
from db.models import user, course
from db.db_setup import engine



user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
