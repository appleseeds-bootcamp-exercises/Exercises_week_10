currentFeed = 'reuters'
function getFeed() {
    $.ajax({
        type: "GET",
        url: ("/get_RSS_feed/" + currentFeed),
        data: {},
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (result) {
            $('#content').empty()
            for (let index = 0; index < result['entries'].length; index++) {
                $('#content').append($(`<br><a href="${result['entries'][index]['link']}">${result['entries'][index]['title']}</a>'`))
            }
        }

    })
}
function updateFeed(e) {
    currentFeed = e.target.value;
}


$(document).ready(getFeed)
$('#feedSelect').on('change', updateFeed)
$('#refresh').on('click', getFeed)
