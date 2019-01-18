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
   <li><a href="" class="btn btn-info">Long Day</a></li>
   <li><a href="" class="btn btn-info">Long Week</a></li>
   <li><a href="" class="btn btn-info">Short 60min</a></li>
   <li><a href="" class="btn btn-info">Short Day</a></li>
   <li><a href="" class="btn btn-info">Swing 15mi</a></li>
   <li><a href="" class="btn btn-info">Swing 60mi</a></li>
   <li><a href="./calls/btst_15min.php" class="btn btn-info">BTST 5min</a></li>
   <li><a href="./calls/btst_15min.php" class="btn btn-info">BTST 15min</a></li>
   <li><a href="./calls/intraday_1min.php" class="btn btn-info">Intra 1min</a></li>
   <li><a href="./calls/intraday_5min.php" class="btn btn-info">Intra 5min</a></li>
  

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