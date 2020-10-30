from fastapi import FastAPI

from lib.apps.pharmacies.router import router as pharmacies_router

app = FastAPI()

# register pharmacies app routes
app.include_router(
    pharmacies_router,
    prefix="/pharmacies",
    tags=["pharmacies"],
)
