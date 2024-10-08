document.addEventListener('DOMContentLoaded', function(){
    const inputBusqueda = document.getElementById('search-input');
    const botonesVet = document.querySelectorAll('.vet-locations');

    inputBusqueda.addEventListener('input',function() {
        filtroVetLocalidad();
    });

function filtroVetLocalidad() {
    const texto = imputBusqueda.value.tolowerCase();
    botonesVet.forEach(boton => {
        const localidad = boton.getAttribute('data-localidad').tolowerCase();
        if (localidad.includes(texto)) {
        boton.style.display = '';
        } else {
            boton.style.display = 'none';
            }
        });
    }
});
