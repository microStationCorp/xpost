$(document).ready(function () {
    $('[data-id=dislike]').click(function (e) {
        e.preventDefault();
        var ind = $('[data-id=dislike]').index(this)
        var postid = $(this).data()['postid']

        $.ajax({
            url: '../dislikepost',
            type: 'GET',
            data: {
                'postid': postid
            },
            success: function (data) {
                if (data['dislike-action'] == 'increase') {
                    $("[data-id=dislike]:eq(" + ind + ")").children()[0].innerText = data['dislike-count']
                    $("[data-id=dislike]:eq(" + ind + ")").removeClass('fa-thumbs-o-down')
                    $("[data-id=dislike]:eq(" + ind + ")").addClass('fa-thumbs-down')
                } else if (data['dislike-action'] == 'increase-liked') {
                    $("[data-id=dislike]:eq(" + ind + ")").children()[0].innerText = data['dislike-count']
                    $("[data-id=dislike]:eq(" + ind + ")").removeClass('fa-thumbs-o-down')
                    $("[data-id=dislike]:eq(" + ind + ")").addClass('fa-thumbs-down')
                    $("[data-id=like]:eq(" + ind + ")").children()[0].innerText = data['like-count']
                    $("[data-id=like]:eq(" + ind + ")").removeClass('fa-thumbs-up')
                    $("[data-id=like]:eq(" + ind + ")").addClass('fa-thumbs-o-up')
                } else {
                    $("[data-id=dislike]:eq(" + ind + ")").children()[0].innerText = data['dislike-count']
                    $("[data-id=dislike]:eq(" + ind + ")").removeClass('fa-thumbs-down')
                    $("[data-id=dislike]:eq(" + ind + ")").addClass('fa-thumbs-o-down')
                }
            },
            error: function () {
                console.log('error')
            }
        })
    })
})