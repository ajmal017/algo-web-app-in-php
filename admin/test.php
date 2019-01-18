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

<?php

$string = file_get_contents('../data/calls/btst_5min.json');
$arr = json_decode($string,true);?>



<!-- BTST BUY  Confirmed Calls -->
<table class="table table-bordered table-hover table-responsive table-striped">
<caption class="bg-primary text-center">BTST BUY <strong> Confirmed  </strong>Calls</caption>
<tr >
<th>Exchange</th>
<th>Symbol</th>
<th>token</th>
<th>Zerodha</th>
<th>Chart</th>
</tr>
<?php   
$nse_conf_buy = $arr['NSE']['confirmed']['BUY'];
foreach($nse_conf_buy as $data){
    $symbol= $data['symbol'];
    $token = $data['token'];      ?>
        <tr>
            <td><?php echo "NSE";?></td>
            <td class="bg-success"><?php echo $symbol;?></td>
            <td><?php echo $token;  ?></td>
            <!-- zerodha button -->
            <td class="btn"><form action="#"> <kite-button href="#" data-kite="z8lgeb6fk65uargj"
            data-exchange="NSE"
            data-product="MIS"
            data-tradingsymbol="<?php echo $symbol;  ?>"
            data-transaction_type="BUY"
            data-quantity="10"
            class="kite-buy"
            title="BUY <?php echo $symbol; ?>"
            data-order_type="MARKET">Buy <strong> <?php echo $symbol; ?></strong> stock</kite-button></form></td>
            <!-- chart link -->
            <td><?php echo "chartlink";  ?></td>
        </tr>
<?php } ?>
</table>


<!-- BTST SELL  Confirmed Calls -->
<table class="table table-bordered table-hover table-responsive table-striped">
<caption class="bg-danger text-center">BTST SELL <strong> Confirmed  </strong> Calls</caption>
<tr >
<th>Exchange</th>
<th>Symbol</th>
<th>token</th>
<th>Chart</th>
</tr>
<?php   
$nse_conf_buy = $arr['NSE']['confirmed']['SELL'];
foreach($nse_conf_buy as $data){
    $symbol= $data['symbol'];
    $token = $data['token'];     ?>
        <tr>
            <td><?php echo "NSE";?></td>
            <td class="bg-danger"><?php echo $symbol;?></td>
            <td><?php echo $token;  ?></td>
            <td><?php echo "chartlink";  ?></td>
        </tr>
<?php } ?>
</table>



<!-- BTST BUY Unonfirmed Calls -->
<table class="table table-bordered table-hover table-responsive table-striped">
<caption class="bg-primary text-center">BTST BUY <strong> Unonfirmed  </strong> Calls</caption>
<tr >
<th>Exchange</th>
<th>Symbol</th>
<th>token</th>
<th>Chart</th>
</tr>
<?php   
$nse_conf_buy = $arr['NSE']['unconfirmed']['BUY'];
foreach($nse_conf_buy as $data){
    $symbol= $data['symbol'];
    $token = $data['token'];      ?>
        <tr>
            <td><?php echo "NSE";?></td>
            <td class="bg-danger"><?php echo $symbol;?></td>
            <td><?php echo $token;  ?></td>
            <td><?php echo "chartlink";  ?></td>
        </tr>
<?php } ?>
</table>







<!-- BTST SELL Unonfirmed Calls -->
<table class="table table-bordered table-hover table-responsive table-striped">
<caption class="bg-info text-center">BTST SELL <strong> Unonfirmed  </strong> Calls</caption>
<tr >
<th>Exchange</th>
<th>Symbol</th>
<th>token</th>
<th>Chart</th>
</tr>
<?php   
$nse_conf_buy = $arr['NSE']['unconfirmed']['SELL'];
foreach($nse_conf_buy as $data){
    $symbol= $data['symbol'];
    $token = $data['token'];      ?>
        <tr>
            <td><?php echo "NSE";?></td>
            <td class="bg-danger"><?php echo $symbol;?></td>
            <td><?php echo $token;  ?></td>
            <td><?php echo "chartlink";  ?></td>
        </tr>
<?php } ?>
</table>


<script src='./calls.js'></script>

<!-- space setup -->
<div style="margin-bottom:50px; padding-bottom:10px;"></div>
<link rel="stylesheet" href="https://kite.zerodha.com/static/build/css/publisher.min.css">
<script src="https://kite.trade/publisher.js?v=3"></script>
</body>
</html>