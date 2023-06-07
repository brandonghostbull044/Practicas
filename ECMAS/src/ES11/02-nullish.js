const anotherNumber = null;
//Los signos de interrogación nos ayudan a preguntar si la variable tiene un valor nulo y en caso de que sea así atribuirle el valor por defecto.
const validate = anotherNumber ?? 5;
console.log(validate);