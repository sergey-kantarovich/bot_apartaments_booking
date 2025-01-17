from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, Request

from ..depandencies import admin_auth
from src.apmin_panel.conf_static import templates

from src.core.db_helper import db_helper
from src.apmin_panel.conf_static import templates

from ..services.booking_api_service import BookingApiRepo


router = APIRouter(
    prefix="/booking",
    tags=["booking"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(admin_auth)],
)


@router.get("/get-bookings")
async def get_bookings(
    request: Request,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.get_db),
    ],
    is_authenticated: bool = Depends(admin_auth),
):
    bookings = await BookingApiRepo(session).get_all_bookings()

    if isinstance(bookings, str):
        return templates.TemplateResponse(
            "bookings.html",
            {
                "request": request,
                "message": bookings,
            },
        )

    return templates.TemplateResponse(
        "bookings.html",
        {
            "request": request,
            "bookings": bookings,
            "user": is_authenticated,
        },
    )
