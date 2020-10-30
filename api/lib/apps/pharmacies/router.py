from fastapi import APIRouter, HTTPException, Depends
from mongoengine.connection import ConnectionFailure

from ...database import connect_to_mongo_service, disconnect_from_mongo_service, is_mongo_service_connected, DatabaseEmptyError
from .schemas import Location, Pharmacy
from .handlers import locate_nearest_pharmacy


router = APIRouter()


async def mongo_service():
    """dependency to share mongo service connection amongst routes"""
    connect_to_mongo_service()
    try:
        yield is_mongo_service_connected()
    finally:
        # close db connection after response
        disconnect_from_mongo_service()


@router.post("/", response_model=Pharmacy)
async def find_nearest_pharmacy(location: Location, mongo_service_connected: bool = Depends(mongo_service)):
    """Find nearest pharmacy from provided coordinates"""
    # verify successful connection to mongo service before proccessing request
    if not mongo_service_connected:
        raise HTTPException(status_code=500, detail="Database service not connected")
    # pass valid coordinates to locate_nearest_pharmacy handler
    try:
        location = location.dict()
        pharmacy = locate_nearest_pharmacy(**location)
        return pharmacy
    except DatabaseEmptyError:
        raise HTTPException(status_code=500,
                            detail="No pharmacies in the database. Did you run the seeder script?")
