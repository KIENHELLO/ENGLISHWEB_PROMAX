# webtienganh/views.py

import os
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

class FrontendAppView(View):
    def get(self, request):
        try:
            # Đường dẫn tuyệt đối đến index.html
            file_path = os.path.join(settings.BASE_DIR, 'front_end', 'build', 'index.html')
            with open(file_path, 'r') as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse("index.html not found!", status=501)
