class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///./test.db')

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()