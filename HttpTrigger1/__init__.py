import logging

import azure.functions as func
import HttpTrigger1.app as app


def main(req: func.HttpRequest) -> func.HttpResponse:
    print("Received Request")
    app.start_app()
    return func.HttpResponse(f"The fetching of data has started")
    
