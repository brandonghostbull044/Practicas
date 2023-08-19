if (true) {
    var fruit1 = 'Apple';
    let fruit2 = 'Orange';
    const fruit3 = 'Lemon';
}

//La function arrow
const eatFruit = (acc) => {
    let accion = acc || 'pela';
    switch (accion) {
        case 'muerde': 
            console.log(`El personaje ${accion} la ${fruit1}`);
            break;
        case 'pela':
            console.log(`El personaje ${accion} la ${fruit1}`);
            break;
        default:
            console.log('No hay acción');
    }
}

eatFruit('muerde');
//La function scope de var sólo funciona en primer nivel, es decir sólo fuera de una anidación
console.log('Hola \n' + fruit1);


const otraAccion = () => {
    return new Promise((resolve, reject) => {
        //La palabra reservada let no tiene function scope
        const opcion2 = fruit2;
        if (false) {
            resolve('Hola \n' + 'No hay fruta definida');
        } else {
            //La palabra reservada const no tiene function scope
            reject('Hola \n' + fruit3); 
    }
    })
}

otraAccion();