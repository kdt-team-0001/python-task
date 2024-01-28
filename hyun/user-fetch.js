fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) =>
        users.forEach((user) => {
            console.log(user.address.geo.lat);
        })
    );
