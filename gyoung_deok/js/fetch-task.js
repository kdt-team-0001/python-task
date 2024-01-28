fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => response.json())
    .then((json) => {
        json.forEach((user) => {
            // idPrint(user);
            // addressPrint(user);
            // streetPrint(user);
            // geoPrint(user);
            // latPrint(user);
            // bsPrint(user);
        });
    });

function idPrint(info) {
    console.log(info.id);
}

function addressPrint(info) {
    console.log(info.address);
}

function streetPrint(info) {
    console.log(info.address.street);
}

function geoPrint(info) {
    console.log(info.address.geo);
}

function latPrint(info) {
    console.log(info.address.geo.lat);
}

function bsPrint(info) {
    console.log(info.company.bs);
}

// fetch("https://jsonplaceholder.typicode.com/users")
//     .then((response) => response.json())
//     .then((users) => users.map((user) => user.address.zipcode))
//     .then(console.log);

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
