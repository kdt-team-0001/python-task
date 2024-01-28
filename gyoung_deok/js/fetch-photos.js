// photos 중 albumId가 4인 것들을 가져와 url, fileName, filePath 출력
// fileName과 filePath는 url에서 추출하여 구분
fetch("https://jsonplaceholder.typicode.com/photos?albumId=4")
    .then((response) => response.json())
    .then((json) => {
        json.forEach((photo) => {
            urlService.print(photo);
        });
    });

const urlService = (() => {
    function print(photo) {
        fileInfos = findName(photo);

        console.log(
            `url: ${photo.url}, fileDirectory: ${fileInfos[1]}, fileName: ${fileInfos[0]}`
        );
    }

    function findName(photo) {
        let photoUrls = photo.url.split("/");
        let fileName = photoUrls.pop();
        let fileDirectory = "";

        fileDirectory = findDirectory(photoUrls, fileDirectory);

        return [fileName, fileDirectory];
    }

    function findDirectory(photoUrls, fileDirectory) {
        photoUrls.forEach((data) => {
            if (data) {
                fileDirectory += `${data}/`;
            } else {
                fileDirectory += `/`;
            }
        });

        return fileDirectory;
    }

    return { print: print };
})();
