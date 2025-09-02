from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL 数据库连接字符串
# 格式为：mysql+pymysql://<user>:<password>@<host>:<port>/<dbname>
# 请将 <...> 替换为你自己的数据库信息
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/game_guide"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
