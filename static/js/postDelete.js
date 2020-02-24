$(document).ready(function () {

    $('[data-class=delete]').click(function (e) {
        e.preventDefault();
        var response = confirm('Are you want to delete?')
        if (response == true) {
            location.href = '/deletePost/' + $(this)[0].dataset.postid
            // console.log($(this)[0].dataset)
        }
    })
    $('[data-class=edit]').click(function (e) {
        e.preventDefault();
        var response = confirm('Are you want to edit?')
        if (response) {
            location.href = '/updatepost/' + $(this)[0].dataset.postid
        }
    })
})