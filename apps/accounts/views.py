import requests
from django.shortcuts import redirect, render
from core.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.

class Login(TemplateView):
    template_name = 'login/login.html'

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # URL de la API
        url = 'http://127.0.0.1:9000/auth/login/'

        # Hacemos la solicitud POST a la API con los datos
        response = requests.post(url, data={'username': username, 'password': password})

        if response.status_code == 200:
            # Si la respuesta es exitosa, obtenemos los tokens
            tokens = response.json()

            # Aquí puedes guardar los tokens en la sesión de Django
            request.session['access_token'] = tokens['access_token']
            request.session['refresh_token'] = tokens['refresh_token']

            # Redirige a una página de inicio o dashboard después del login
            return redirect('index')

        else:
            # Si las credenciales son incorrectas
            return render(request, self.template_name, {'error_message': 'Usuario o contraseña incorrectos.'})

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
class LogOut(LoginRequiredMixin, TemplateView):

    def get(self, request):
        url = 'http://127.0.0.1:9000/auth/logout/'

        # Hacemos la solicitud POST a la API con los datos
        response = requests.get(url)

        if response.status_code == 200:
            
            request.session['access_token'] = ''
            request.session['refresh_token'] = ''

        return redirect('/')