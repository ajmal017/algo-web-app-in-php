<?php require("head.php"); ?>


<script type="text/javascript">
  $(document).ready(function(){
    $('.calls').css({"background-color": "lightblue", "font-size": "120%"});
  });
  </script>

    <!-- top menu -->
    <nav class="navbar navbar-default navbar-fixed-top  pagesetup">
      <?php require("dashboard_menu.php"); ?>
    </nav>

    <!-- bottom menu -->
    <nav class="navbar navbar-default navbar-fixed-bottom  pagesetup">
      <?php require("dashboard_menu.php"); ?>
    </nav>

    <div style="margin-top:50px; padding-top:10px;"></div>
    
    <!-- Ajax Menu   -->
<div class="container-fluid">
  <div class="row">
<div class="col-sm-12">
  <ul class="list-inline">
   <li><button class="btn btn-success" id="long_term_day">Long Day</button></li>
   <li><button class="btn btn-success" id="long_term_week">Long Week</button></li>
   <li><button class="btn btn-success" id="short_term_60min">Short 60min</button></li>
   <li><button class="btn btn-success" id="short_term_day">Short Day</button></li>
   <li><button class="btn btn-success" id="swing_trade_15min">Swing 15min</button></li>
   <li><button class="btn btn-success" id="swing_trade_60min">Swing 60min</button></li>
   <li><button class="btn btn-success" id="btst_5min">BTST 5min</button></li>
   <li><button class="btn btn-success" id="btst_15min">BTST 15min</button></li>
   <li><button class="btn btn-success" id="intraday_1min">Intra 1min</button></li>
   <li><button class="btn btn-success" id="intraday_5min">Intra 5min</button></li>
   <li><button class="btn btn-warning"><span id="clicked">None</span> </button></li>

  </ul>
</div>
</div>
</div>

<div class="container-fluid">
<div id="data">Please Click one of the above buttuon</div>
  
</div>


<!--ohlc data -->
<!-- <script src='jquery-3.3.1.js'></script> -->
<script src='./calls.js'></script>

<!-- space setup -->
<div style="margin-bottom:50px; padding-bottom:10px;"></div>
<link rel="stylesheet" href="https://kite.zerodha.com/static/build/css/publisher.min.css">
<script src="https://kite.trade/publisher.js?v=3"></script>
</body>
</html>