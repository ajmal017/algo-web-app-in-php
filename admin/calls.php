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
   <li><button class="btn btn-success">Long T. Daily</button></li>
   <li><button class="btn btn-success">Long T. Weekly</button></li>
   <li><button class="btn btn-success">Short T. 60 min</button></li>
   <li><button class="btn btn-success">Short T. Daily</button></li>
   <li><button class="btn btn-success">Swing T. 15 min</button></li>
   <li><button class="btn btn-success">Swing T. 60 min</button></li>
   <li><button class="btn btn-success">BTST 5 min</button></li>
   <li><button class="btn btn-success">BTST 15 min</button></li>
   <li><button class="btn btn-success">Intraday 1 min</button></li>
   <li><button class="btn btn-success">Intraday 5 min</button></li>

  </ul>
</div>
</div>
</div>

<div class="container-fluid">
<div id="data">Please Click one of the above buttuon</div>
  
</div>


<!--ohlc data -->

<!-- space setup -->
<div style="margin-bottom:50px; padding-bottom:10px;"></div>

</body>
</html>