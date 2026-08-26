# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto corregido y listo para compilar.

---

```
Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
import os
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List
import jwt
from datetime import datetime, timedelta

# === ARCHIVO: app/core/config.py ===

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///./test.db')

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()


# === ARCHIVO: app/dependencies/security.py ===

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        user_id: str = payload.get('sub')
        if user_id is None:
            raise HTTPException(status_code=400, detail='Invalid authentication credentials')
        return user_id
    except jwt.PyJWTError:
        raise HTTPException(status_code=400, detail='Invalid authentication credentials')


# === ARCHIVO: app/models/account.py ===

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    balance = Column(Float)
    owner = Column(String)


# === ARCHIVO: app/schemas/account.py ===

from pydantic import BaseModel
from typing import Optional

class AccountBase(BaseModel):
    account_number: str
    balance: float
    owner: str

class AccountCreate(AccountBase):
    pass

class AccountUpdate(AccountBase):
    balance: Optional[float] = None
    owner: Optional[str] = None

class AccountResponse(AccountBase):
    id: int

    class Config:
        orm_mode = True


# === ARCHIVO: app/services/account_service.py ===

from sqlalchemy.orm import Session
from..models.account import Account
from..schemas.account import AccountCreate, AccountUpdate, AccountResponse

def get_account_by_id(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first()

def create_account(db: Session, account: AccountCreate):
    db_account = Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def update_account(db: Session, account_id: int, account: AccountUpdate):
    db_account = db.query(Account).filter(Account.id == account_id).first()
    if db_account is None:
        return None
    for key, value in account.dict(exclude_unset=True).items():
        setattr(db_account, key, value)
    db.commit()
    db.refresh(db_account)
    return db_account

def delete_account(db: Session, account_id: int):
    db_account = db.query(Account).filter(Account.id == account_id).first()
    if db_account is None:
        return None
    db.delete(db_account)
    db.commit()
    return db_account


# === ARCHIVO: app/routers/account.py ===

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from..core.config import SessionLocal
from..dependencies.security import get_current_user
from..services.account_service import get_account_by_id, create_account, update_account, delete_account
from..schemas.account import AccountCreate, AccountUpdate, AccountResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/accounts/', response_model=AccountResponse)
def create_account_endpoint(account: AccountCreate, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    return create_account(db, account)

@router.get('/accounts/{account_id}', response_model=AccountResponse)
def read_account(account_id: int, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    db_account = get_account_by_id(db, account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return db_account

@router.put('/accounts/{account_id}', response_model=AccountResponse)
def update_account_endpoint(account_id: int, account: AccountUpdate, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    db_account = update_account(db, account_id, account)
    if db_account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return db_account

@router.delete('/accounts/{account_id}', response_model=AccountResponse)
def delete_account_endpoint(account_id: int, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    db_account = delete_account(db, account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return db_account


# === ARCHIVO: tests/test_account.py ===

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from..core.config import Config, Base
from..models.account import Account
from..schemas.account import AccountCreate
from..services.account_service import create_account

engine = create_engine(Config.SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

def test_create_account():
    db = TestingSessionLocal()
    account = AccountCreate(account_number='1234567890', balance=100.0, owner='John Doe')
    new_account = create_account(db, account)
    assert new_account.account_number == account.account_number
    assert new_account.balance == account.balance
    assert new_account.owner == account.owner


# === ARCHIVO: tests/test_main.py ===

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}

def test_create_account():
    response = client.post('/accounts/', json={'account_number': '1234567890', 'balance': 100.0, 'owner': 'John Doe'})
    assert response.status_code == 200
    assert response.json()['account_number'] == '1234567890'
    assert response.json()['balance'] == 100.0
    assert response.json()['owner'] == 'John Doe'

def test_read_account():
    response = client.get('/accounts/1')
    assert response.status_code == 200
    assert response.json()['account_number'] == '1234567890'
    assert response.json()['balance'] == 100.0
    assert response.json()['owner'] == 'John Doe'

def test_update_account():
    response = client.put('/accounts/1', json={'balance': 200.0})
    assert response.status_code == 200
    assert response.json()['balance'] == 200.0

def test_delete_account():
    response = client.delete('/accounts/1')
    assert response.status_code == 200
    assert response.json()['account_number'] == '1234567890'
    assert response.json()['balance'] == 200.0
    assert response.json()['owner'] == 'John Doe'


# === ARCHIVO: main.py ===

from fastapi import FastAPI
from.routers import account

app = FastAPI()

app.include_router(account.router)

@app.get('/')
def read_root():
    return {'message': 'Hello World'}

```
