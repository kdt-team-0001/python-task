fetch("https://jsonplaceholder.typicode.com/albums")
    .then((response) => response.json())
    .then((json) => {
        json.forEach((album) => {
            albumPrintIncludingByQui(album);
        });
    });

function albumPrintIncludingByQui(album){
    let target = "qui"
    if(album.title.includes(target)){
        console.log(album);
    }
}