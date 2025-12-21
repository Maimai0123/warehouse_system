from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.staff import Staff
from app.models.supplier import Supplier

# --- Seed Staff ---
INITIAL_STAFF = [
    {"StaffID": 1, "stName": "Admin", "stDept": "管理部"},
    {"StaffID": 2, "stName": "張倉管", "stDept": "倉庫部"},
    {"StaffID": 3, "stName": "李採購", "stDept": "採購部"},
]

async def create_initial_data(db: AsyncSession):
    result = await db.exec(select(Staff))
    first_staff = result.first()
    
    if not first_staff:
        print("🌱 Seeding Staff data...")
        for data in INITIAL_STAFF:
            staff = Staff(
                StaffID=data["StaffID"], 
                stName=data["stName"], 
                stDept=data["stDept"]
            )
            db.add(staff)
        await db.commit()
    
# --- Seed Supplier ---
INITIAL_SUPPLIERS = [
    {"SupplierID": 1, "suName": "A公司", "suPhone": "02-2345-6789", "suAddress": "台北市信義區..."},
    {"SupplierID": 2, "suName": "B公司", "suPhone": "04-8765-4321", "suAddress": "台中市西屯區..."},
]

async def create_initial_data(db: AsyncSession):
    result = await db.exec(select(Supplier))
    if not result.first():
        print("🌱 Seeding Supplier data...")
        for data in INITIAL_SUPPLIERS:
            supplier = Supplier(**data) # 使用 unpacking 快速賦值
            db.add(supplier)
        await db.commit()