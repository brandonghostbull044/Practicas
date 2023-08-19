const anotherFunction = () => {
    return new Promise((resolve, reject) => {
        if (false) {
            resolve('Hey!!');
        } else {
            reject('Mehh');
        }
    })
}

anotherFunction()
    .then(response => console.log(response))   
    .catch(err => console.log(err));



    // Callback
    function funcion1(fn) {
        setTimeout(function() {
            console.log("Mensaje 10");
            fn();
        }, 2000);
    }

    function funcion2() {
        console.log("Mensaje 2");
    }

    funcion1(funcion2);