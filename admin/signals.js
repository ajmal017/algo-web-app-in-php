$(document).ready(function() {
    $('#month').click(function() {
        // alert('gc55964');
        $.get('./signals/month.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('MONTH');
        });
    });

    $('#week').click(function() {
        // alert('gc55964');
        $.get('./signals/week.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('WEEK');
        });
    });

    $('#day').click(function() {
        // alert('gc55964');
        $.get('./signals/day.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('DAY');
        });
    });

    $('#hour').click(function() {
        // alert('gc55964');
        $.get('./signals/hour.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('HOUR');
        });
    });

    $('#15min').click(function() {
        // alert('gc55964');
        $.get('./signals/15min.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('15MIN');
        });
    });

    $('#5min').click(function() {
        // alert('gc55964');
        $.get('./signals/5min.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('5MIN');
        });
    });

    $('#1min').click(function() {
        // alert('gc55964');
        $.get('./signals/1min.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('1MIN');
        });
    });
});