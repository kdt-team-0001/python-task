fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((json) => {
        json.filter((post) => post.title.includes('ve') && post.body.includes('ve')).forEach((post) => {
            console.log(post);
        });
    });