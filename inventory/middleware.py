from django.http import HttpResponseForbidden

class IPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ALLOWED_IPS = ['192.168.0.111', '26.195.139.3', '192.168.80.1', '192.168.85.252', '127.0.0.1']  # İcazə verilən IP ünvanları
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))

        # İstifadəçinin IP ünvanını konsola çap et
        print(f"User IP: {user_ip}")

        if user_ip not in ALLOWED_IPS:
            return HttpResponseForbidden("Giriş qadağandır!")  # İcazə verilməyən IP üçün cavab

        return self.get_response(request) 