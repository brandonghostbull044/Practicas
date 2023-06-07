const users = {
    brandon: {
        country: "MX"  
    },
    ana: {
        country: "CO"
    }
};

console.log(users.brandon.country);
//Los signos de pregunta sirven para preguntar si existe, y en dado caso que no exista en vez de devolver error que nos devuelva un dato indefinido
console.log(users?.bebeloper?.country);