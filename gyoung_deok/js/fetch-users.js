fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((json) => {
        json.forEach((user) => {
            // idPrint(user);
            // addressPrint(user);
            // streetPrint(user);
            // geoPrint(user);
            // latPrint(user);
            // bsPrint(user);
        });
    });

function idPrint(info) {
    console.log(info.id);
}

function addressPrint(info) {
    console.log(info.address);
}

function streetPrint(info) {
    console.log(info.address.street);
}

function geoPrint(info) {
    console.log(info.address.geo);
}

function latPrint(info) {
    console.log(info.address.geo.lat);
}

function bsPrint(info) {
    console.log(info.company.bs);
}
