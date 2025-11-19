from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session as get_db
from app.schemas.auth import LoginRequest, LoginResponse
from app.services.auth_service import login_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=LoginResponse)
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)):
    user = await login_user(db, data)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return user
