$(document).ready(function () {
    $('[data-likestate=True]').removeClass('fa-thumbs-o-up')
    $('[data-likestate=True]').addClass('fa-thumbs-up')
    $('[data-dislikestate=True]').removeClass('fa-thumbs-o-up')
    $('[data-dislikestate=True]').addClass('fa-thumbs-up')
    $('[data-reportstate=True]').removeClass('fa-thumbs-o-up')
    $('[data-reportstate=True]').addClass('fa-thumbs-up')
});