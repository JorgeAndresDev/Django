document.getElementById('btn-logout').addEventListener('click', function (event) {
    event.preventDefault(); // Evita la acción por defecto del enlace

    // Obtiene la URL de logout desde el atributo data-logout-url
    var logoutUrl = this.getAttribute('data-logout-url');

    Swal.fire({
        title: '¿Estás seguro?',
        text: "Esta acción cerrará su sesión actual.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sí, cerrar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            localStorage.removeItem('isLogged'); // Remueve el ítem de localStorage
            window.location.href = logoutUrl; // Redirige a la URL de logout
        }
    });
});