$(document).ready(function () {
    $('[data-likestate=True]').removeClass('fa-thumbs-o-up')
    $('[data-likestate=True]').addClass('fa-thumbs-up')
    $('[data-dislikestate=True]').removeClass('fa-thumbs-o-down')
    $('[data-dislikestate=True]').addClass('fa-thumbs-down')
    $('[data-reportstate=True]').addClass('myreport')
});