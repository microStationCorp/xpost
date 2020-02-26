$(document).ready(function () {
    $('[data-id=report]').click(function (e) {
        e.preventDefault();
        var ind = $('[data-id=report]').index(this)
        var postid = $(this).data()['postid']

        $.ajax({
            url: '../reportpost',
            type: 'GET',
            data: {
                'postid': postid
            },
            success: function (data) {
                console.log(data)
                if (data['report-action'] == 'increase') {
                    $("[data-id=report]:eq(" + ind + ")").children()[0].innerText = data['report-count']
                    $("[data-id=report]:eq(" + ind + ")").addClass('myreport')
                } else {
                    $("[data-id=report]:eq(" + ind + ")").children()[0].innerText = data['report-count']
                    $("[data-id=report]:eq(" + ind + ")").removeClass('myreport')
                }
            },
            error: function () {
                console.log('error')
            }
        })
    })
})