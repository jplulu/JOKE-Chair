from backend.webapi.routes.db_test_route import test_routes
from backend.webapi import app
from sqlalchemy import create_engine

app.register_blueprint(test_routes)

if __name__ == '__main__':
    app.run(debug=False)
