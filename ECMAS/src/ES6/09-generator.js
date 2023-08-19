// El * es la clave para determinar que es un generator
function* iterate(array) {
    for (let value of array) {
        yield value;
    }
}


const it = iterate(['Oscar', 'David', 'Ana', 'Jennifer']);
console.log(it.next().value);
console.log(it.next().value);
console.log(it.next().value);

