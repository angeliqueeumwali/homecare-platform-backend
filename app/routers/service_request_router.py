from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_current_user, require_roles
from app.core.enums import UserRole
from app.database.connection import get_db
from app.models.user import User
from app.schemas.service_request_schema import ServiceRequestCreate, ServiceRequestResponse, ServiceRequestStatusUpdate
from app.services.service_request_service import ServiceRequestService

router = APIRouter(prefix="/service-requests", tags=["Service Requests"])
customer = require_roles(UserRole.CUSTOMER)

@router.post("", response_model=ServiceRequestResponse, status_code=201)
async def create_request(data: ServiceRequestCreate, db=Depends(get_db), current_user: User=Depends(customer)):
    try:
        return await ServiceRequestService.create(db, current_user.id, data)
    except ValueError as e:
        raise HTTPException(400, str(e))

@router.get("/me", response_model=list[ServiceRequestResponse])
async def my_requests(db=Depends(get_db), current_user: User=Depends(get_current_user)):
    return await ServiceRequestService.customer_list(db, current_user.id)

@router.get("/{request_id}", response_model=ServiceRequestResponse)
async def get_request(request_id, db=Depends(get_db), current_user: User=Depends(get_current_user)):
    try:
        request = await ServiceRequestService.get(db, request_id)
        if current_user.role != UserRole.ADMIN and request.customer_id != current_user.id:
            raise HTTPException(403, "You do not have access to this request")
        return request
    except ValueError as e:
        raise HTTPException(404, str(e))

@router.patch("/{request_id}/status", response_model=ServiceRequestResponse)
async def update_status(request_id, data: ServiceRequestStatusUpdate, db=Depends(get_db), current_user: User=Depends(get_current_user)):
    try:
        request = await ServiceRequestService.get(db, request_id)
        if current_user.role != UserRole.ADMIN and request.customer_id != current_user.id:
            raise HTTPException(403, "You do not have access to this request")
        return await ServiceRequestService.update_status(db, request, data.status)
    except ValueError as e:
        raise HTTPException(400, str(e))

@router.get("", response_model=list[ServiceRequestResponse])
async def all_requests(db=Depends(get_db), _: object=Depends(require_roles(UserRole.ADMIN))):
    return await ServiceRequestService.all(db)
