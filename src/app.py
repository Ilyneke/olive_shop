import uvicorn
from fastapi import FastAPI, Request
from fastapi.openapi.docs import get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from settings import base as settings

from admin import init_admin_panel
from api import routers
from settings.db import Base, engine
from settings.base import STORAGE_DIR


def create_app() -> FastAPI:
    app = FastAPI(
        title='Olive shop',
        docs_url=None,
        openapi_url='/olive/openapi.json',
        root_path='/olive'
        # swagger_ui_parameters={'deepLinking': False, 'persistAuthorization': True},
    )

    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/api/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="/olive/static/swagger-ui-bundle.js",
            swagger_css_url="/olive/static/swagger-ui.css",
            swagger_ui_parameters={'deepLinking': False, 'persistAuthorization': True},
        )

    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOW_ORIGINS,
        allow_credentials=settings.ALLOW_CREDENTIALS,
        allow_methods=settings.ALLOW_METHODS,
        allow_headers=settings.ALLOW_HEADERS,
        expose_headers=settings.EXPOSE_HEADERS,
    )

    for router in routers:
        app.include_router(router)
    app.mount('/uploads', StaticFiles(directory=STORAGE_DIR), name="uploads")

    init_admin_panel(app=app, engine=engine)

    @app.on_event('startup')
    async def startup() -> None:
        # async with engine.begin() as conn:
        #     await conn.run_sync(Base.metadata.create_all)
        pass

    return app


app_ = create_app()


if __name__ == '__main__':
    uvicorn.run('app:app_', reload=True, port=8000)
