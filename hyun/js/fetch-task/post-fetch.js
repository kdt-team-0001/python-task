// fetch로 post 정보 json으로 받아온 후 userid별로 몇 개씩 올렸는지 개수 출력
fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((posts) => {
        printPostCount(getPostCount(posts));
    });

// post 객체로 구성된 posts Array에서 userId별로 개수를 세어 객체로 return하는 함수
function getPostCount(posts) {
    let countInfo = new Object();
    posts.forEach((post) => {
        if (countInfo.hasOwnProperty(post.userId.toString())) {
            countInfo[`${post.userId}`]++;
        } else {
            countInfo[`${post.userId}`] = 1;
        }
    });
    return countInfo;
}

// {유저id: 개수, ...}로 구성된 객체를 받아 출력해주는 함수
function printPostCount(countInfo) {
    for (let userId in countInfo) {
        console.log(`${userId}번 회원 : ${countInfo[userId]}개 작성함`);
    }
}
