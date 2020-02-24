$(document).ready(function () {
    $('[data-id=myAjaxPost]').click(function () {
        if (($(this)[0].nextElementSibling.classList).length == 1) {
            $.ajax({
                url: 'http://127.0.0.1:8000/posts/countPost/',
                type: 'GET',
                success: function (data) {
                    // console.log(data)
                    $('#post-count').text(data)
                },
                error: function () {
                    console.log('error')
                }
            })
        }
    })
});