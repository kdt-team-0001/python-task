// photo마다 제목과 url을 출력하기
fetch("https://jsonplaceholder.typicode.com/photos")
    .then((response) => response.json())
    .then((photos) => photos.forEach((photo) => printTitleAndUrl(photo)));

function printTitleAndUrl(photo) {
    console.log(`제목: ${photo.title}\n링크: ${photo.url}`);
}
