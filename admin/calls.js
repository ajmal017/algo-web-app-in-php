$(document).ready(function() {
    $('#long_term_day').click(function() {
        // alert('gc55964');
        $.post('./Calls/long_term_day.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('long_term_day');
        });
    });

    $('#long_term_week').click(function() {
        // alert('gc55964');
        $.post('./Calls/long_term_week.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('long_term_week');
        });
    });

    $('#short_term_60miny').click(function() {
        // alert('gc55964');
        $.post('./Calls/short_term_60min.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('short_term_60min');
        });
    });

    $('#short_term_day').click(function() {
        // alert('gc55964');
        $.post('./Calls/short_term_day.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('short_term_day');
        });
    });

    $('#swing_trade_15min').click(function() {
        // alert('gc55964');
        $.post('./Calls/swing_trade_15min.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('swing_trade_15min');
        });
    });

    $('#swing_trade_60min').click(function() {
        // alert('gc55964');
        $.post('./Calls/swing_trade_60min.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('swing_trade_60min');
        });
    });

    $('#btst_5min').click(function() {
        // alert('gc55964');
        $.post('./Calls/btst_5min.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('btst_5min');
        });
    });

    $('#btst_15min').click(function() {
        // alert('gc55964');
        $.post('./Calls/btst_15min.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('btst_15min');
        });
    });

    $('#intraday_1min').click(function() {
        // alert('gc55964');
        $.post('./Calls/intraday_1min.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('intraday_1min');
        });
    });

    $('#intraday_5min').click(function() {
        // alert('gc55964');
        $.post('./Calls/intraday_5min.php', function(data, status) {
            // alert(data);
            $('#data').html(data);
            $('#clicked').html('intraday_5min');
        });
    });
});