/**
 * Created by krishnasagar on 7/9/16.
 */

$.fn.stars = function() {
    return $(this).each(function() {
        var rating = $(this).data("rating");
        var numStars = $(this).data("numStars");
        var fullStar;
        if(parseInt(rating) == rating) {
            fullStar = new Array(Math.ceil(rating + 1)).join('<i class="fa fa-star"></i>');
        }
        else if(parseFloat(rating) == rating) {
            fullStar = new Array(Math.floor(rating + 1)).join('<i class="fa fa-star"></i>');
        }
        var halfStar = ((rating%1) !== 0) ? '<i class="fa fa-star-half-empty"></i>': '';
        var noStar = new Array(Math.floor(numStars + 1 - rating)).join('<i class="fa fa-star-o"></i>');
        $(this).html(fullStar + halfStar + noStar);
    });
};
$('.stars').stars();

var popup;
$('#newTrackBttn').click(function (){
    var left = ($(window).width() / 2) - (900 / 2),
    top = ($(window).height() / 2) - (600 / 2);
    popup = window.open("http://"+location.host+"/addTrack/", "popup", "width=900, height=600, top=" + top + ", left=" + left);
});

$('#page1').click(function() {
    var v = parseInt($(this).attr('title'));
    window.location.href = 'http://' + location.host + '/tracks/' + v.toString() + '/';
    /*$.ajax({
        url: 'http://' + location.host + '/tracks/' + v.toString() + '/',
        type: "get",
    });*/
});
$('#page2').click(function() {
    var v = parseInt($(this).attr('title'));
    window.location.href = 'http://' + location.host + '/tracks/' + v.toString() + '/';
});
$('#page3').click(function() {
    var v = parseInt($(this).attr('title'));
    window.location.href = 'http://' + location.host + '/tracks/' + v.toString() + '/';
});

$( document ).ready(function() {
    $("#msgDiv").fadeIn(300).text('Instruction : Scroll up/down in the below list').fadeOut(3000);
});

function f1(ele) {
    var id = $(ele).attr('title').split(':')[1].split(' ')[1];
    var left = ($(window).width() / 2) - (900 / 2),
    top = ($(window).height() / 2) - (600 / 2);
    popup = window.open("http://"+location.host+"/editTrack/"+id+"/", "popup", "width=900, height=600, top=" + top + ", left=" + left);
}
function f2(nextPage) {
    $("#Ptab").click(function() {
        if (nextPage == undefined) {
            $("#msgDiv").fadeIn(300).text('Reached first page, no previous !!!').fadeOut(3000);
        }
        else {
            if ((nextPage[0]-2)>0) {
                window.location.href = 'http://' + location.host + '/tracks/' + (nextPage[0]-2) + '/';
            }
            else {
                $("#msgDiv").fadeIn(300).text('Reached first page !!!').fadeOut(3000);
            }
        }
    });
    $("#Ntab").click(function() {
        if (nextPage == undefined) {
            $("#msgDiv").fadeIn(300).text('On first page, use below tabs !!!').fadeOut(3000);
        }
        else {
            window.location.href = 'http://' + location.host + '/tracks/' + nextPage[0] + '/';
        }
    });
}