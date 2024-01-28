// 댓글을 작성한 유저들의 email 주소를 중복없이 출력해보기
fetch("https://jsonplaceholder.typicode.com/comments")
    .then((response) => response.json())
    .then(getUniqueEmails);

// comments들이 담긴 Array를 전달받아 email을 Set 객체에 담아 중복 제거 후 Array로 바꾸어 출력
function getUniqueEmails(comments) {
    const emailSet = new Set();
    comments.forEach((comment) => {
        emailSet.add(comment.email);
    });
    const emailArr = Array.from(emailSet);
    emailArr.forEach((email) => console.log(email));
}
