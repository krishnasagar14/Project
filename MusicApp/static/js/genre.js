/**
 * Created by krishnasagar on 7/9/16.
 */

$.fn.f1 = function(v) {
    $(this).on("scroll", function() {
        var gl = $(this);
        if(v == 1) {
            if(gl.scrollTop() + gl.innerHeight() >= gl[0].scrollHeight) {
                if(confirm('Want to move for next batch of list') == true) {
                    window.location.href = 'http://' + location.host + '/genres/' + 1 + '/';
                }
            }
        }
        if(v == 0) {
            if(gl.scrollTop() == 0) {
                if(confirm('Want to move for previous batch of list') == true) {
                    window.location.href = 'http://' + location.host + '/genres/' + 0 + '/';
                }
            }
        }
    });
};

function f2(v) {
    if(v == 1) {
        $("#msgDiv").fadeIn(1800).text('Reached end of list!!!').fadeOut(1800);
    }
    if(v == 0) {
        $("#msgDiv").fadeIn(1800).text('Reached start of list!!!').fadeOut(1800);
    }
}

function f3(ele) {
    var id = $(ele).attr('title').split(':')[1].split(' ')[1];
    var left = ($(window).width() / 2) - (900 / 2),
    top = ($(window).height() / 2) - (600 / 2),
    popup = window.open("http://"+location.host+"/editGenre/"+id+"/", "popup", "width=900, height=600, top=" + top + ", left=" + left);
}

$("#newGenreBttn").click(function() {
    var left = ($(window).width() / 2) - (900 / 2),
    top = ($(window).height() / 2) - (600 / 2),
    popup = window.open("http://"+location.host+"/addGenre/", "popup", "width=900, height=600, top=" + top + ", left=" + left);
});