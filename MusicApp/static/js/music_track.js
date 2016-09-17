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

$("#formS").submit(function(e) {
    e.preventDefault();
    if($("#searchBox").val().length == 0) {
        alert("Enter track name in below search box.");
    }
    else {
        var v = $("#searchBox").val(), 
        url = "http://104.197.128.152:8000/v1/tracks?title=";
        $.ajax({
            url : url + v,
            type : "GET",
            success : function(result) {
                var searchRes = $("#results");
                searchRes.empty();
                if(result.count > 0) {
                    //below steps can be done jquery and is easy.
                    for(var i = 0;i < result.count; i++) {
                        searchRes.append("<br>"+result.results[i]['title'] + "-" + result.results[i]['id'] + ", rating-" + result.results[i]['rating']+",[genres: ");
                        if(result.results[i]['genres'].length > 0) {
                            if(result.results[i]['genres'].length > 1) {
                                for(var j = 0; j<result.results[i]['genres'].length;j++) {
                                    console.log(result.results[i]['genres'][j]);
                                    searchRes.append(result.results[i]['genres'][j]['id']+"-"+result.results[i]['genres'][j]['name']+",");
                                }
                            }
                            else {
                                searchRes.append(result.results[i]['genres'][0]['id']+"-"+result.results[i]['genres'][0]['name']+",");
                            }
                        }
                        else {
                            searchRes.append("none");
                        }
                        searchRes.append("]</br>");
                    }
                }
                else {
                    searchRes.append("Search not found !!!");
                }
            }
        });
    }
});
