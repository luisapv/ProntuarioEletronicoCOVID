from config.db import Base, engine, app
from sqlalchemy import MetaData
from routes.app_routes import app

Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run('0.0.0.0', port=7000, debug=True)