$(document).ready(function () {
  $("li.user").click(function () {
    var usr = $(this).children()[0].dataset.id;
    var url = "http://127.0.0.1:8000/following/post/" + usr;
    var myHtml = "";
    $.ajax({
      url: url,
      type: "get",
      success: function (data) {
        for (var post of data.allposts) {
          var title = post.title[0].toUpperCase() + post.title.slice(1);
          var time = new Date(post.time);
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

          myHtml =
            myHtml +
            `<div class="card mx-auto my-2 p-2"
        style="box-shadow: 1px 1px 1px rgba(13, 54, 54, 0.507);background-color: #0a7a865e;">
        <div class="card-text">
            <h3>${title}</h3>
            <small class="text-muted">${
            months[
            parseInt(time.toLocaleDateString("en-GB").split("/")[1]) - 1
            ]
            } ${time.toLocaleDateString("en-GB").split("/")[0]}, ${
            time.toLocaleDateString("en-GB").split("/")[2]
            } - ${time.toLocaleTimeString("en-US")}</small>
        </div>
        <div class="card pl-2 py-2 my-2" style="box-shadow: 1px 1px 1px rgba(13, 54, 54, 0.507);">
            ${post.post}
        </div>
        <div class="row justify-content-end icons">
            <div class="col-1">
                <i data-postid="${post.id}" data-likestate="${
            post.likeState
            }" data-id="like" class="fa fa-thumbs-o-up fa-2" aria-hidden="true"> <span>${
            post.like
            }</span></i>
            </div>
            <div class="col-1">
                <i data-postid="${post.id}" data-dislikestate="${
            post.dislikeState
            }" data-id="dislike" class="fa fa-thumbs-o-down fa-2" aria-hidden="true"> <span>${
            post.dislike
            }</span></i>
            </div>
            <div class="col-1">
                <i data-postid="${post.id}" data-reportstate="${
            post.reportState
            }" data-id="report" class="fa fa-bug fa-2" aria-hidden="true"> <span>${
            post.report
            }</span></i>
            </div>
        </div>
    </div>`;
        }
        $("[data-id=myfollowpost]").html(myHtml);
        $("[data-likestate=true]").removeClass("fa-thumbs-o-up");
        $("[data-likestate=true]").addClass("fa-thumbs-up");
        $("[data-dislikestate=true]").removeClass("fa-thumbs-o-down");
        $("[data-dislikestate=true]").addClass("fa-thumbs-down");
        $("[data-reportstate=true]").addClass("myreport");

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
      },
      error: function (data) {
        console.log("error");
      }
    });
  });
});