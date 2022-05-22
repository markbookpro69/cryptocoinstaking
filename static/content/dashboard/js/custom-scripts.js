// Notification Alert timeout
$(document).ready(function() {
        // messages timeout for 10 sec 
        setTimeout(function () {
            $('.message').fadeOut('slow');
        }, 3000); // time in milliseconds, 1000 =  1 sec

        // delete message
    $('.del-msg').live('click',function(){
        $('.del-msg').parent().attr('style', 'display:none;');
    })
});
// Notification Alert timeout

//

$(document).ready(function () {
    $('#example').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ]
    });
});
