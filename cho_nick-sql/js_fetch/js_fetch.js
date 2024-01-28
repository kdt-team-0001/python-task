// posts 에서 title 뽑기

// fetch("https://jsonplaceholder.typicode.com/posts")
//     .then((response) => response.json())
//     .then((posts) => {
//         posts.forEach((posts) => {
//             const { title } = posts;
//             console.log(title);
//         });
//     });

// comments 에서 name 뽑기

// fetch("https://jsonplaceholder.typicode.com/comments")
//     .then((response) => response.json())
//     .then((comments) => {
//         comments.forEach((comments) => {
//             console.log(comments);
//         });
//     });

// fetch("https://jsonplaceholder.typicode.com/comments")
//     .then((response) => response.json())
//     .then((comments) => {
//         comments.forEach((comments) => {
//             const { name } = comments;
//             console.log(name);
//         });
//     });


// albums에서 title 뽑기

// fetch("https://jsonplaceholder.typicode.com/albums")
//     .then((response) => response.json())
//     .then((albums) => {
//         albums.forEach((albums) => {
//             const { title } = albums;
//             console.log(title);
//         });
//     });

// photos에서 url 뽑기

// fetch("https://jsonplaceholder.typicode.com/photos")
//     .then((response) => response.json())
//     .then((photos) => {
//         photos.forEach((photos) => {
//             const { url } = photos;
//             console.log(url);
//         });
//     });

// todos에서 title,id 뽑기

// fetch("https://jsonplaceholder.typicode.com/todos")
//     .then((response) => response.json())
//     .then((todos) => {
//         todos.forEach((todos) => {
//             const { title, id } = todos;
//             console.log(title, id);
//         });
//     });

// 밑에 posts 에서 id, body 뽑기

// fetch("https://jsonplaceholder.typicode.com/posts")
//     .then((response) => response.json())
//     .then((posts) => {
//         posts.forEach((posts) => {
//             const { id, body } = posts;
//             console.log(id, body);
//         });
//     });

// 밑에꺼 posts에서... title 뽑기 ///  오류납니다 뭘까요??

// fetch("https://jsonplaceholder.typicode.com/posts/1")
//     .then((response) => response.json())
//     .then((posts) => {
//         posts.forEach((posts) => {
//             const { title } = posts;
//             console.log(title);
//         });
//     });

// comments 에서 name,email 뽑기

// fetch("https://jsonplaceholder.typicode.com/posts/1/comments")
//     .then((response) => response.json())
//     .then((comments) =>
//         comments.forEach((commenst) => {
//             const { name, email } = commenst;
//             console.log(name, email);
//         })
//     );

// comments 에서 id, email 뽑기

// fetch("https://jsonplaceholder.typicode.com/comments?postId=1")
//     .then((response) => response.json())
//     .then((comments) => {
//         comments.forEach((comments) => {
//             const { id, email } = comments;
//             console.log(id, email);
//         });
//     });

// fetch("https://jsonplaceholder.typicode.com/comments?postId=1")
//     .then((response) => response.json())
//     .then((comments) => {
//         comments.forEach((comments) => {
//             console.log(comments);
//         });
//     });
