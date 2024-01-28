// users => geo => lat;

// fetch("https://jsonplaceholder.typicode.com/users")
//     .then((response) => response.json())
//     .then((json) => {
//         json.forEach((user) => {
//             let userGeo = [user.address.geo];
//             userGeo.forEach((geoLocation) => {
//                 // console.log(`lat: ${geoLocation["lat"]}`);
//             });
//         });
//     });

// /// todos => title
// fetch("https://jsonplaceholder.typicode.com/todos")
//     .then((response) => response.json())
//     .then((json) => {
//         json.forEach((content) => {
//             const { title } = content; // 구조분해 할당의 특징을 사용함
//             // getTitle(title);
//             // console.log(`id: ${content.id} / title: ${content.title}`);
//         });
//     });

// function getTitle(title, id) {
//     console.log(title);
// }

// /photos => thumnailUrl
// fetch("https://jsonplaceholder.typicode.com/photos")
//     .then((response) => response.json())
//     .then((json) => {
//         json.forEach((content) => {
//             const { thumbnailUrl } = content;
//             // getTumnail(thumbnailUrl);
//         });
//     });

// function getTumnail(thumbnailUrl) {
//     console.log(thumbnailUrl);
// }

// albums => title
// fetch("https://jsonplaceholder.typicode.com/albums")
//     .then((response) => response.json())
//     .then((json) => {
//         json.forEach((album) => {
//             const { title } = album;
//             getAlbum(title);
//         });
//     });

// function getAlbum(title) {
//     console.log(title);
// }

// comments => email
// fetch("https://jsonplaceholder.typicode.com/comments")
//     .then((response) => response.json())
//     .then((json) => {
//         json.map((field) => {
//             const { email } = field;
//             // getField(email);
//         });
//     });

// function getField(email) {
//     console.log(email);
// }

// photos => url

// fetch("https://jsonplaceholder.typicode.com/photos")
//     .then((response) => response.json())
//     .then((json) => {
//         for (i = 0; i < json.length; i++) {
//             const { url } = json[i];
//             getPhoto(url);
//         }
//     });
//
// function getPhoto(url) {
//     console.log(url);
// }
