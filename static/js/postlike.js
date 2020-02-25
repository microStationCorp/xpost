$(document).ready(function () {
    $('[data-id=like]').click(function (e) {
        e.preventDefault();
        var ind = $('[data-id=like]').index(this)
        var postid = $(this).data()['postid']

        $.ajax({
            url: '../likepost',
            type: 'GET',
            data: {
                'postid': postid
            },
            success: function (data) {
                if (data['like-action'] == 'increase') {
                    $("[data-id=like]:eq(" + ind + ")").children()[0].innerText = data['like-count']
                    $("[data-id=like]:eq(" + ind + ")").removeClass('fa-thumbs-o-up')
                    $("[data-id=like]:eq(" + ind + ")").addClass('fa-thumbs-up')
                } else {
                    $("[data-id=like]:eq(" + ind + ")").children()[0].innerText = data['like-count']
                    $("[data-id=like]:eq(" + ind + ")").removeClass('fa-thumbs-up')
                    $("[data-id=like]:eq(" + ind + ")").addClass('fa-thumbs-o-up')
                }
            },
            error: function () {
                console.log('error')
            }
        })
    })
})