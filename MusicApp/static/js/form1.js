/**
 * Created by krishnasagar on 7/9/16.
 */

/*if (window.opener == undefined) {window.top.close();}*/
$("#cancelBttn").click(function() {
    window.close();
});

/*$( document ).ready(function() {
    alert($('select option').length);
});*/

function f1(id) {
    $("#form1").submit(function(e) {
        e.preventDefault(); // form submission overruled with ajax call on same action url of form, getting control on submit event
        if($("#id_tname").val().length <= 0) {
            $('#ErrorSpan').text('Error : Track Name is required').fadeIn(300).fadeOut(3800);
        }
        else {
            var v1 = $(this).serialize().split('&'), res = [], result= 'id=' + id + '&';
            for (var x =0; x<v1.length;x++) {
                if(v1[x].includes('gname')) {
                    res.push(v1[x].split('=')[1]);
                }
                else if('rating=' == v1[x]) {
                    result += 'rating=0.0&';
                }
                else {
                    result += v1[x] + '&';
                }
            }
            result += 'gname='+res;
            $.ajax({
                type:"POST",
                url:$(this).attr('action'),
                data:result,
                success: function(result) {
                    alert('Success.... reload page after 30 seconds.');
                    window.close();
                },
            });
        }
    });
}

