var modelo = ["Sunfire", "Aveo", "Ikon", "March"];
var marca = ["Pontiac", "Chevrolet", "Ford", "Nissan"];
var annio = [2001, 2016, 2014, 2018];
function auto(marca, modelo, annio) [
    this.marca = marca;
    this.modelo = modelo;
    this.annio = annio;
    ]

for (var i = 0; i < modelo.length; i++) {
    var modelo[i] = new auto(marca[i], modelo[i], annio[i]);
    console.log(modelo[i]);   
}