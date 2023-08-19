var listaAutos = [];

function auto(marca, modelo, annio) {
    this.marca = marca;
    this.modelo = modelo;
    this.annio = annio;
}

function agregarAuto(marca, modelo, annio) {
    var nuevoAuto = new auto(marca, modelo, annio);
    listaAutos.push(nuevoAuto);
}

function registrarAutoNuevo() {
    var marca = prompt ("ingresar la marca");
    var modelo = prompt ("ingresar el modelo");
    var annio = prompt ("ingresar el año");
    agregarAuto(marca, modelo, annio);
    console.log("¡Agregaste tu nuevo auto!";)
}