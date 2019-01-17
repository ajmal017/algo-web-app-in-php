$(document).ready(function() {
    $('#btst').click(function() {
        // alert('gc55964');
        $.get('./filters/btst.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('BTST');
        });
    });

    $('#intraday').click(function() {
        // alert('gc55964');
        $.get('./filters/intraday.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('INTRADAY');
        });
    });


});