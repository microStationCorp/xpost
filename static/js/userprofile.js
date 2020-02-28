$(document).ready(function () {
    $('[data-dashid]').click(function () {
        var dashId = $(this).data('dashid')
        var myHtml = ''

        $.ajax({
            url: '../profile/poststatus',
            type: 'GET',
            data: {
                'dashId': dashId
            },
            success: function (data) {
                sl = 0
                for (var post of data.posts) {
                    sl = sl + 1;
                    var title = post.title[0].toUpperCase() + post.title.slice(1);
                    var time = new Date(post.dop);
                    var months = [
                        "January",
                        "February",
                        "March",
                        "April",
                        "May",
                        "June",
                        "July",
                        "August",
                        "September",
                        "October",
                        "November",
                        "December"
                    ];
                    myHtml = myHtml +
                        `<tr>
                    <th scope="row">${sl}</th>
                    <td>${title}</td>
                    <td>${
                        months[
                        parseInt(time.toLocaleDateString("en-GB").split("/")[1]) - 1
                        ]
                        } ${time.toLocaleDateString("en-GB").split("/")[0]}, ${
                        time.toLocaleDateString("en-GB").split("/")[2]
                        } - ${time.toLocaleTimeString("en-US")}</td>
                    <td>${post.count}</td>
                </tr>`;
                }
                $('#mytablebody').html(myHtml)
                for (var keep of $('[data-dashid]')) {
                    if (keep.classList.contains('setHeadActive')) {
                        var ind = $('[data-dashid]').index(keep)
                        $("[data-dashid]:eq(" + ind + ")").removeClass('setHeadActive')
                    }
                }
                $('[data-dashid=' + dashId + ']').addClass('setHeadActive')
            }, error: function (error) {
                console.log(error)
            }
        })

    })
})
