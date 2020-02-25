$(document).ready(function () {
    $('[data-id=like]').click(function (e) {
        e.preventDefault();
        console.log('sujan grub')
        var postid = $(this).data()['postid']
        console.log('ready for ajax call')

        $.ajax({
            url: '../likepost',
            type: 'GET',
            data: {
                'postid': postid
            },
            success: function (data) {
                console.log(data)
            },
            error: function () {
                console.log('error')
            }
        })
    })
})