from flask import Flask
from flask_cors import CORS

def createApp():
    app= Flask(__name__)
    CORS(app)
    from app.module.apiRouter.test import router
    from app.module.apiRouter.addData import router as addData
    app.register_blueprint(router, url_prefix='/')
    app.register_blueprint(addData, url_prefix='/addData')

    
    return app