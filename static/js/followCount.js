$(document).ready(function () {
    $('[data-id=myAjaxFollow]').click(function () {
        if (($(this)[0].nextElementSibling.classList).length == 1) {
            $.ajax({
                url: 'http://127.0.0.1:8000/following/count/',
                type: 'GET',
                success: function (data) {
                    $('#follow-count').text(data)
                },
                error: function () {
                    console.log('error')
                }
            })
        }
    })
});