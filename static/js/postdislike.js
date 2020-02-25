$(document).ready(function () {
    $('[data-id=dislike]').click(function (e) {
        e.preventDefault();
        console.log('grub')
        var ind = $('[data-id=dislike]').index(this)
        var postid = $(this).data()['postid']
        console.log(ind, postid)

        $.ajax({
            url: '../dislikepost',
            type: 'GET',
            data: {
                'postid': postid
            },
            success: function (data) {
                console.log(data)
                if (data['dislike-action'] == 'increase') {
                    $("[data-id=dislike]:eq(" + ind + ")").children()[0].innerText = data['dislike-count']
                    $("[data-id=dislike]:eq(" + ind + ")").removeClass('fa-thumbs-o-down')
                    $("[data-id=dislike]:eq(" + ind + ")").addClass('fa-thumbs-down')
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