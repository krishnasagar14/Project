/**
 * Created by krishnasagar on 8/9/16.
 */

$("#cancelBttn").click(function() {
    window.close();
});

function f1(id) {
    $("#form2").submit(function(e) {
        e.preventDefault();
        if($("#id_gname").val().length <= 0) {
            $('#ErrorSpan').text('Error : Genre Name is required !!!').fadeIn(300).fadeOut(3800);
        }
        else {
            var v1 = $(this).serialize() + '&id=' + id;
            $.ajax({
                type:"POST",
                url:$(this).attr('action'),
                data:v1,
                success: function(result) {
                    alert('Success');
                    window.close();
                },
            });
        }
    });
}
