from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import require_roles
from app.core.enums import UserRole
from app.database.connection import get_db
from app.repositories.provider_repository import ProviderRepository
from app.repositories.user_repository import UserRepository
from app.schemas.provider_schema import ProviderApprovalRequest, ProviderProfileResponse
from app.schemas.user_schema import UserResponse
from app.services.provider_service import ProviderService

router = APIRouter(prefix="/admin", tags=["Admin"])
admin = require_roles(UserRole.ADMIN)

@router.get("/users", response_model=list[UserResponse])
async def users(db=Depends(get_db), _: object=Depends(admin)):
    return await UserRepository.get_all(db)

@router.get("/providers", response_model=list[ProviderProfileResponse])
async def providers(db=Depends(get_db), _: object=Depends(admin)):
    return await ProviderRepository.get_all(db)

@router.patch("/providers/{provider_id}/approval", response_model=ProviderProfileResponse)
async def approve_provider(provider_id, data: ProviderApprovalRequest, db=Depends(get_db), _: object=Depends(admin)):
    provider = await ProviderRepository.get_by_id(db, provider_id)
    if not provider:
        raise HTTPException(404, "Provider not found")
    return await ProviderService.approve(db, provider, data.approved)
