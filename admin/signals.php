<?php require("head.php"); ?>

<script type="text/javascript">
  $(document).ready(function(){
    $('.signals').css({"background-color": "lightblue", "font-size": "120%"});
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
   <li><button class="btn btn-success" id="month">Monthly</button></li>
   <li><button class="btn btn-success" id="week">Weekly</button></li>
   <li><button class="btn btn-success" id="day">Daily</button></li>
   <li><button class="btn btn-success" id="hour">60 Min</button></li>
   <li><button class="btn btn-success" id="15min">15 Min</button></li>
   <li><button class="btn btn-success" id="5min">5 Min</button></li>
   <li><button class="btn btn-success" id="1min">1 Min</button></li>
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
<script src='./signals.js'></script>
<!-- space setup -->
<div style="margin-bottom:50px; padding-bottom:10px;"></div>


</body>
</html>