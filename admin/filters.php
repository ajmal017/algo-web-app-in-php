<?php require("head.php"); ?>

<script type="text/javascript">
  $(document).ready(function(){
    $('.filters').css({"background-color": "lightblue", "font-size": "120%"});
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
<div class="container">
  <div class="row">
<div class="col-sm-8 col-sm-offset-2">
  <ul class="list-inline">
   <li><button class="btn btn-success" id="long">Long Term</button></li>
   <li><button class="btn btn-success" id="short">Short Term</button></li>
   <li><button class="btn btn-success" id="short">Swing Trade</button></li>
   <li><button class="btn btn-success" id="btst">BTST</button></li>
   <li><button class="btn btn-success" id="intraday">Intraday</button></li>
   <li>button Clicked : </li>
   <li><button class="btn btn-warning"><span id="clicked">None</span> </button></li>
  </ul>
</div>
</div>
</div>


    <!-- main contents   -->
<div class="container">
  <div id="data">
    <h1>Please click one of above button</h1>
  </div>
</div>

<script src='jquery-3.3.1.js'></script>
<script src='./filters.js'></script>

<!-- space setup -->
<div style="margin-bottom:50px; padding-bottom:10px;"></div>


</body>
</html>