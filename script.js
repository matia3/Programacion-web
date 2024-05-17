fetch('/js/data.json')

.then(function(response){
    return response.json();
})

.then(function(envios){
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let envio of envios)
        out+= `
    <tr>
    <td>${envio.id_usuario} </td>
    <td>${envio.usuario} </td>
    <td>${envio.fecha_compra} </td>
    <td>${envio.fecha_entrega} </td>
    <td>${envio.lista_productos} </td>
    <td>${envio.precio} </td>
    </tr>
    `

    placeholder.innerHTML = out;
})

function validarRegistro() {
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    if (email.trim() === '') {
        alert('Por favor ingrese su correo electrónico.');
        return false;
    }

    if (password.trim() === '') {
        alert('Por favor ingrese su contraseña.');
        return false;
    }
    return true;
}