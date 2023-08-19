var display = document.querySelector('.console');
var one = document.querySelector('#one');
var two = document.querySelector('#two');
var three = document.querySelector('#three');
var four = document.querySelector('#four');
var five = document.querySelector('#five');
var six = document.querySelector('#six');
var seven = document.querySelector('#seven');
var eight = document.querySelector('#eight');
var nine = document.querySelector('#nine');
var cero = document.querySelector('#cero');
var division = document.querySelector('#division');
var multiplication = document.querySelector('#multiplication');
var subtraction = document.querySelector('#subtraction');
var addition = document.querySelector('#addition');
var equal = document.querySelector('#equal');
var point = document.querySelector('#point');
var valor = display.value;

if (division.addEventListener(''))

function mult (valor, valorr) {
    var multiplicacion = valor*valorr;
}
function div (valor, valorr) {
    var divission = valor/valorr;
}
function sum (valor, valorr) {
    var suma = valor + valorr;
}
function rest (valor, valorr) {
    var resta = valor - valorr;
}

division.addEventListener('click', mult);



switch (operacion) {
    case "mult": 
        var resultado = mult;
        break;
    case "div":
        var resultado = div;
        break;
    case "sum":
        var resultado = sum;
        break;
    case "rest":
        var resultado = rest;
        break;
}

function result (resulta) {
    display.innerText = resultado;
}

