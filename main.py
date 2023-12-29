from fastapi import FastAPI, HTTPException
from typing import List
from models import CashRegister, Model, Country, CashRegisterType, UpdateCashRegister
from uuid import UUID
from ipaddress import ip_address

app = FastAPI()

db: List[CashRegister] = [
  CashRegister(
    id=UUID('a687db82-c9b4-4815-a94d-ce70f03ad117'),
    store_code= 19,
    store_ip= '127.0.0.1',
    cash_register_code= 1,
    cash_register_ip= '127.0.0.1',
    cash_register_netmask='255.255.255.0',
    model=Model.toshiba,
    serial_number='123MMM',
    country=Country.uruguay,
    cash_register_type=CashRegisterType.common
    ),
  CashRegister(
    id=UUID('1b0a2563-2bda-49e7-a3bd-0869e19365e2'),
    store_code= 1,
    store_ip= '127.0.0.2',
    cash_register_code= 2,
    cash_register_ip= '127.0.0.2',
    model=Model.ibm,
    serial_number='465MMM',
    country=Country.uruguay,
    cash_register_type=CashRegisterType.vertical
    )
]

def valid_ip_address(objeto):
  try:
    ip_address(objeto.store_ip)
    ip_address(objeto.cash_register_ip)
    ip_address(objeto.cash_register_netmask)
    return True
  except ValueError:
    return False

@app.get('/')
def root():
  return {'Hi': 'World'}

@app.get('/api/v1/cash_register')
async def fetch_cash_register():
  return db

@app.post('/api/v1/cash_register/')
async def register_cash_register(cash_register: CashRegister):
  db.append(cash_register)
  return {'id': cash_register.id}

@app.delete('/api/v1/cash_register/{cash_register_id}')
async def delete_cash_register(cash_register_id: UUID):
  for cash_register in db:
    if cash_register_id == cash_register.id:
      db.remove(cash_register)
      return
  raise HTTPException(
    status_code=404,
    detail=f'cash_register with id: {cash_register_id} does not exist'
  )

@app.put('/api/v1/cash_register/{cash_register_id}')
async def update_cash_register(cash_register_update: UpdateCashRegister, cash_register_id: UUID):
    for i in db:
      if i.id == cash_register_id:
        if cash_register_update.store_code is not None:
          i.store_code = cash_register_update.store_code
        if cash_register_update.store_ip is not None:
          i.store_ip = cash_register_update.store_ip
        if cash_register_update.cash_register_code is not None:
          i.cash_register_code = cash_register_update.cash_register_code
        if cash_register_update.cash_register_ip is not None:
          i.cash_register_ip = cash_register_update.cash_register_ip
        if cash_register_update.cash_register_gateway is not None:
          i.cash_register_gateway = cash_register_update.cash_register_gateway
        if cash_register_update.cash_register_netmask is not None:
          i.cash_register_netmask = cash_register_update.cash_register_netmask
        if cash_register_update.model is not None:
          i.model = cash_register_update.model
        if cash_register_update.serial_number is not None:
          i.serial_number = cash_register_update.serial_number
        if cash_register_update.cash_register_type is not None:
          i.cash_register_type = cash_register_update.cash_register_type
        i.cash_register_type = i.cash_register_type
        return
    raise HTTPException(
      status_code=404,
      detail=f'cash_register with id: {cash_register_id} does not exist'
    )