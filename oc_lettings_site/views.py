import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    logger.info("Home page requested")
    return render(request, "index.html")
