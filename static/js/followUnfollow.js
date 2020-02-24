$(document).ready(function () {
    $('.myAuthor').click(function (e) {
        e.preventDefault();
        var auth_id = $(this)[0].dataset.id
        var indicator = $(this).text()
        if (indicator == 'follow') {
            ajaxCall(auth_id, indicator)
        } else if (indicator == 'unfollow') {
            ajaxCall(auth_id, indicator)
        }
    })

    function ajaxCall(id, indicator) {
        $.ajax({
            url: '../following/follow',
            type: 'GET',
            data: {
                'id': id,
                'indicator': indicator
            },
            success: function (data) {
                $("[data-id='" + id + "']").removeClass(data.rmc)
                $("[data-id='" + id + "']").addClass(data.ac)
                $("[data-id='" + id + "']").text(data.text)
            },
            error: function (error) {
                alert('error')
            }
        })
    }
})