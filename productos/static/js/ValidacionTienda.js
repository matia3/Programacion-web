function validarTiendaAbierta() {
    fetch('https://express-vercel-backend-example.vercel.app/dias')
        .then(function (respuesta) {
            return respuesta.json();
        })
        .then(function (datos) {
            const diasDeLaSemana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
            const ahora = new Date();
            const diaActual = diasDeLaSemana[ahora.getDay() - 1];
            const horaActual = ahora.getHours() + ':' + ahora.getMinutes().toString().padStart(2, '0');
            console.log('Dia actual:', diaActual);
            console.log(ahora.getHours(), ahora.getMinutes());
            const horarioTienda = datos[0][diaActual];
            const horaApertura = horarioTienda.open;
            const horaCierre = horarioTienda.close;

            const estaAbierta = horaActual >= horaApertura && horaActual < horaCierre;

            const botonTienda = document.getElementById('botonTienda');
            const enlaceTienda = botonTienda.querySelector('a');
            
            if (estaAbierta) {
                botonTienda.classList.remove('btn-coral');
                botonTienda.classList.add('btn-success');
                enlaceTienda.textContent = 'Abierto';
            } else {
                botonTienda.classList.remove('btn-coral');
                botonTienda.classList.add('btn-danger');
                enlaceTienda.textContent = 'Cerrado';
            }
        })
        .catch(function (error) {
            console.error('Error al obtener el horario de la tienda:', error);
        });
}