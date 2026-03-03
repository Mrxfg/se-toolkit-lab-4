"""Router for learner endpoints."""

from fastapi import APIRouter
from datetime import datetime
from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.learners import read_learners, create_learner
from app.models.learner import Learner, LearnerCreate

router = APIRouter()


@router.get("/learners", response_model=list[Learner])
async def get_learners(
    enrolled_after: datetime | None = None,
    session: AsyncSession = Depends(get_session),
):
    return await read_learners(session, enrolled_after)


@router.post("/learners", response_model=Learner, status_code=201)
async def post_learner(
    body: LearnerCreate,
    session: AsyncSession = Depends(get_session),
):
    return await create_learner(
        session,
        name=body.name,
        email=body.email,
    )
