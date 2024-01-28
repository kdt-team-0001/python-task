// fetch로 유저 정보 json 으로 받아온 후 latitude(lat) 출력하기
fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((users) =>
        users.forEach((user) => {
            printLatitude(user.address.geo.lat);
        })
    );

function printLatitude(lat) {
    console.log(lat);
}
