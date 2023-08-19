const h1 = document.querySelector('h1');
const input1 = document.querySelector('#calculo1')
const input2 = document.querySelector('#calculo2')
const btn = document.querySelector('#btnCalcular')
const resultado = document.querySelector('#result')
const ovacion = document.querySelector('#ovacion')
function btnOnClick() {
    resultado.innerText = `Resultado: ${((+input1.value) + (+input2.value))}`;
}
function ova() {
    ovacion.innerText = "¡Felicidades!"
}

btn.addEventListener('click', btnOnClick);

input1.addEventListener('change', ova);