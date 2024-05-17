function listarProductos(categoria) {
    fetch('https://apibenja3.vercel.app/productos')

        .then(function (response) {
            console.log(response);
            return response.json();
        })

        .then(function (productos) {
            let placeholder = document.querySelector("#data-output");
            let out = "";
            
            for (let producto of productos){
                console.log(producto);
              if (producto.categoria == categoria){
        out += `
        <div class="col-xxl-3 col-lg-4 col-md-6 col-sm-12 d-flex justify-content-center mb-3">
                <button class="card" role="button" tabindex="0">
                    <img src="${producto.imagen}" class="card-img-top" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title">${producto.nombre}</h5>
                        <p class="card-text">${producto.precio}</p>
                        <a href="#" class="btn btn-coral">Añadir al carrito</a>                        
                    </div>
                </button>
            </div>
        `
        console.log(producto.nombre);  
   };
    placeholder.innerHTML = out;
}
})
}
