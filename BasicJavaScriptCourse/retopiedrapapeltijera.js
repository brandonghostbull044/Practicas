//if, else if, else

var Brandon= "";
var Machine= "";

function Juego(Brandon, Machine) {
    if (Brandon == "tijera" && Machine == "papel") {
        console. log ("Ganaste");
    }
    else if (Brandon == "piedra" && Machine == "tijera") {
        console. log ("Ganaste");
    }
    else if (Brandon == "papel" && Machine == "piedra") {
        console. log ("Ganaste");
    }
    else if (Brandon == "tijera" && Machine == "tijera") {
        console. log ("Empate");
    }
    else if (Brandon == "piedra" && Machine == "piedra") {
        console. log ("Empate");
    }
    else if (Brandon == "papel" && Machine == "papel") {
        console. log ("Empate");
    }
    else {
        console. log ("Perdiste");
    }
}

//switch

var Brandon = "";
var Machine = "";

function Juego(Brandon, Machine) {
    switch (true) {
        case Brandon == "piedra" && Machine == "tijera":
            console.log ("¡Ganaste!");
            break;
        case Brandon == "papel" && Machine == "piedra":
            console.log ("¡Ganaste!");
            break;
        case Brandon == "tijera" && Machine == "papel":
            console.log ("¡Ganaste!");
            break;
        case Brandon == "piedra" && Machine == "piedra":
            console.log ("Empate");
            break;
        case Brandon == "papel" && Machine == "papel":
            console.log ("Empate");
            break;
        case Brandon == "tijera" && Machine == "tijera":
            console.log ("Empate");
            break;
        case Brandon == "piedra" && Machine == "papel":
            console.log ("Perdiste");
            break;
        case Brandon == "papel" && Machine == "tijera":
            console.log ("Perdiste");
            break;
        case Brandon == "tijera" && Machine == "piedra":
            console.log ("Perdiste");
            break; 
        default:
            console.log ("¡Juega!");
    }
} 