const getImages = () => {
    $.ajax({
        type: "GET",
        url: "http://localhost:7000/get_images",
        data: {
        },
        dataType: "json",
        success: function (responsemsg) {
            showImages(responsemsg);
        },
        error: function (msg) {
            console.log("ersror");
        },
    });
}
const showImages = (images) => {
    images.forEach(element => {
        $("#images").append($(`<img src=${element}></img>`))
    });
}

$(document).ready(getImages);
