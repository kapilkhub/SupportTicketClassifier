import logging

import azure.functions as func
from fastapi import FastAPI
from .router import router

app = FastAPI()
# Add the router to the FastAPI app
app.include_router(router,prefix="/apis")

def main(req: func.HttpRequest) -> func.HttpResponse:
    func.AsgiMiddleware(app).handle(req)