from pydantic import BaseModel
import enum


class Status(str, enum.Enum):
    in_queue = "in_queue"
    in_progress = "in_progress"
    done = "done"
    rejected = "rejected"


class TaskBase(BaseModel):
    title: str
    responsible: str
    status: Status


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
