const user = {username: 'Brandon', age: 22, country: 'MX'};
const {username, ...values} = user;
console.log(username);
console.log(values);