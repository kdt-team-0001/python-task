// albums를 받아 가장 짧은 제목과 가장 긴 제목을 가진 객체를 각각 출력해보기
fetch("https://jsonplaceholder.typicode.com/albums")
    .then((response) => response.json())
    .then((albums) => getShortestAndLongest(albums));

function getShortestAndLongest(albums) {
    let longest = null;
    let shortest = null;
    let shortestLength = 2100000000;
    let longestLength = -1;
    let currentLength = 0;
    albums.forEach((album) => {
        currentLength = album.title.length;
        if (currentLength <= shortestLength) {
            shortest = album;
            shortestLength = currentLength;
        }
        if (currentLength >= longestLength) {
            longest = album;
            longestLength = currentLength;
        }
    });
    console.log("* 제목이 가장 긴 앨범 *");
    printAlbum(longest);
    console.log("==========================");
    console.log("* 제목이 가장 짧은 앨범 *");
    printAlbum(shortest);
}

function printAlbum(album) {
    console.log("{");
    for (let key in album) {
        console.log(`    ${key}: ${album[key]},`);
    }
    console.log("}");
}
