var estadoValidacion = {
    'nombre': false,
    'email': false,
    'telefono': false,
    'password': false,
    'password2': false,
    'direccion': false,
    'codigoPostal': false
  };
  
  $(document).ready(function () {
  
    $("#nombre, #email, #telefono, #password, #password2, #direccion, #codigoPostal").on("focusout", function () {
  
      var valor = $(this).val();
      var id = $(this).attr("id");
      var esValido = false;
      switch (id) {
        case "nombre":
          esValido = validarNombre(valor);
          $("#valNombre").text(esValido ? "" : "Error en el Nombre");
          break;
        case "email":
          esValido = validarEmail(valor);
          $("#valEmail").text(esValido ? "" : "Error en el Correo.");
          break;
        case "telefono":
          esValido = validarTelefono(valor);
          $("#valTelefono").text(esValido ? "" : "Error en el teléfono. (9 Digitos)");
          break;
        case "password":
          esValido = validarPassword(valor);
          $("#valPassword").text(esValido ? "" : "Error en la contraseña. Debe tener almenos, 8 caracteres, 1 letra en mayuscula y 1 numero");
          break;
        case "password2":
          var password = $("#password").val();
          esValido = validarPassword2(password, valor);
          $("#valPassword2").text(esValido ? "" : "Error en la contraseña. Debe ser igual que la anterior");
          break;
        case "direccion":
          esValido = validarDireccion(valor);
          $("#valDireccion").text(esValido ? "" : "Error en la direccion.");
          break;
        case "codigoPostal":
          esValido = validarCodigoPostal(valor);
          $("#valCodigo").text(esValido ? "" : "Error en el Codigo postal. (Debe tener 7 digitos.)");
          break;
      }
      estadoValidacion[id] = esValido;
      actualizarEstadoBoton();
    });
  });
  
  function validarNombre(nombre) {
    if (nombre != "") {
      return /^[a-zA-Z\s]+$/.test(nombre);
    }
    return false;
  }
  
  function validarEmail(email) {
    if (email != "") {
      return /^[^\s@]+@[^\s@]+.[^\s@]+$/.test(email);
    }
    return false;
  }
  
  function validarTelefono(telefono) {
    if (telefono != "") {
      return /^[0-9]{9}$/.test(telefono);
    }
    return false;
  }
  
  function validarPassword(password) {
    if (password != "") {
      return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/.test(password);
    }
    return false;
  }
  
  function validarPassword2(password, password2) {
    if (password2 != "") {
      return password === password2;
    }
    return false;
  }
  
  function validarDireccion(direccion) {
    if (direccion != "") {
      return /^[a-zA-Z0-9\s,'-]+$/.test(direccion);
    }
    return false;
  }
  
  
  function validarCodigoPostal(codigoPostal) {
    if (codigoPostal != "") {
        return /^\d{7}$/.test(codigoPostal);
      }
    return false;
  }
  
  function actualizarEstadoBoton() {
    var validarTodos = Object.values(estadoValidacion).every(function (estado) {
      return estado;
    });
  
    $("#botonValidar").prop('disabled', !validarTodos);
    }

    function alertaBoton(){
        alert("Registro exitoso");
    }