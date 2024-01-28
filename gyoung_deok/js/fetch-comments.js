

fetch("https://jsonplaceholder.typicode.com/posts/100/comments")
    .then((response) => response.json())
    .then((json) => {
        printLength(json)
    });

function printLength(json){
    console.log(`post_id가 100인 댓글 수: ${json.length}개`);
}