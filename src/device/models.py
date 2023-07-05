from pydantic import BaseModel
from typing import Optional


class DeviceType(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class DeviceModel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class DeviceState(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class DeviceAdditionalState(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class DeviceBase(BaseModel):
    name: str


class DeviceCreate(DeviceBase):
    type_id: int
    model_id: Optional[int]
    state_id: Optional[int]
    additional_state_id: Optional[int]


class Device(DeviceCreate):
    id: int
    serial_number: int

    class Config:
        orm_mode = True


class DeviceRelatedCreate(DeviceBase):
    type_name: str
    model_name: Optional[str]
    state_name: Optional[str]
    additional_state_name: Optional[str]


class DeviceRelated(DeviceRelatedCreate):
    id: int
    serial_number: int


class Channel(BaseModel):
    id: int
    name: str
