from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4
from enum import Enum

class Model(str, Enum):
  toshiba = 'toshiba',
  ibm = 'ibm'

class Country(str, Enum):
  uruguay = 'Uruguay',
  panama = 'Panama'

class CashRegisterType(str, Enum):
  common = 'common',
  vertical = 'vertical',
  horizontal = 'horizontal'

class UpdateCashRegister(BaseModel):
  store_code: Optional[int] = None
  store_ip: Optional[str] = None
  cash_register_code: Optional[int] = None
  cash_register_ip: Optional[str] = None
  cash_register_gateway: Optional[str] = None
  cash_register_netmask: Optional[str] = None
  model: Optional[Model] = None
  serial_number: Optional[str] = None
  cash_register_type: Optional[CashRegisterType] = None
  
class CashRegister(BaseModel):
  id: Optional[UUID] = uuid4()
  store_code: int
  store_ip: str
  cash_register_code: int
  cash_register_ip: str 
  cash_register_gateway: Optional[str] = None
  cash_register_netmask: str = '255.255.255.0'
  model: Model
  serial_number: str
  country: Country
  cash_register_type: CashRegisterType