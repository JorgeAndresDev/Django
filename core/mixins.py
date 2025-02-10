import requests
from django.shortcuts import redirect

class LoginRequiredMixin(object):
    """ Este mixin valida que el usuario esté autenticado dentro de la aplicación """

    def dispatch(self, request, *args, **kwargs):

        # Obtén el token de acceso de la sesión de Django
        access_token = request.session.get('access_token')

        # Si no hay token, redirige al login
        if not access_token:
            return redirect('accounts:login')

        # URL para verificar el usuario autenticado
        url = 'http://127.0.0.1:9000/auth/get_user/'

        # Pasamos el token en el encabezado de la solicitud
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        # Realizamos la solicitud GET con el token de autorización
        response = requests.get(url, headers=headers)

        # Si el token no es válido o el servidor responde con un error
        if response.status_code != 200:
            return redirect('accounts:login')

        # Si todo está bien, continua con la ejecución de la vista
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
