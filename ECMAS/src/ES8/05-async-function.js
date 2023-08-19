const fnAsync = () => {
    return new Promise((resolve, reject) => {
        //Podemos crear un if con el operador ternario, donde ? es la sentencia verdadera y : la sentencua else, dentro no se puede cerrar con punto y coma sino hasta terminar la sentencia else
        (true)
            ? setTimeout(() => resolve('AsynC!!'), 2000)
            : reject(new Error('Error'));
    });
}

const anotherFunction = async () => {
    const something = await fnAsync();
    console.log(something);
    console.log('Hello');
}

console.log('Before');
anotherFunction();
console.log('After');
