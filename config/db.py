from sqlalchemy import create_engine, MetaData

# engine = create_engine("mysql+pymysql://gabriel:123456@localhost:3306/biz_points")
engine = create_engine("sqlite:///foo.db")

meta_data = MetaData()
