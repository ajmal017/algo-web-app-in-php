<!DOCTYPE html>
<html>
<head>

    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title><?php echo " " ?></title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- <link rel="stylesheet" type="text/css" media="screen" href="main.css" /> -->
    <script src="main.js"></script>
    <link rel="stylesheet" href="bootstrap.min.css">
    <link rel="stylesheet" href="bootstrap-theme.min.css">
    <script src="jquery-3.3.1.js"></script> 
    
 
</head>

<body>
<div class="container">
  <div class="row">
<div class="col-sm-12">
  <ul class="list-inline">
   <li id="a"><a href="" class="btn btn-info">Long Day</a></li>
   <li id="b"><a href="" class="btn btn-info">Long Week</a></li>
   <li id="c"><a href="" class="btn btn-info">Short 60min</a></li>
   <li id="d"><a href="" class="btn btn-info">Short Day</a></li>
   <li id="e"><a href="" class="btn btn-info">Swing 15mi</a></li>
   <li id="f"><a href="" class="btn btn-info">Swing 60mi</a></li>
   <li id="g"><a href="./btst_15min.php" class="btn btn-danger">BTST 5min</a></li>
   <li id="h"><a href="./btst_15min.php" class="btn btn-info">BTST 15min</a></li>
   <li id="i"><a href="./intraday_1min.php" class="btn btn-info">Intra 1min</a></li>
   <li id="j"><a href="./intraday_5min.php" class="btn btn-info">Intra 5min</a></li>
  

  </ul>
</div>
</div>
</div>


<!--ohlc data -->

<?php

$string = file_get_contents('../data/calls/btst_5min.json');
$arr = json_decode($string,true);?>



<!-- BTST BUY  Confirmed Calls -->
<div class="container">
    <div class="col-sm-8 col-sm-offset-2">
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
            <td class="btn"> <kite-button href="#" data-kite="z8lgeb6fk65uargj"
            data-exchange="NSE"
            data-product="MIS"
            data-tradingsymbol="<?php echo $symbol;  ?>"
            data-transaction_type="BUY"
            data-quantity="10"
            class="kite-buy"
            title="BUY <?php echo $symbol; ?>"
            data-order_type="MARKET">Buy <strong> <?php echo $symbol; ?></strong> stock</kite-button></td>
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
<th>Zerodha</th>
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
            <!-- zerodha button -->
            <td class="btn"> <kite-button href="#" data-kite="z8lgeb6fk65uargj"
            data-exchange="NSE"
            data-product="MIS"
            data-tradingsymbol="<?php echo $symbol;  ?>"
            data-transaction_type="SELL"
            data-quantity="10"
            class="kite-sell"
            title="SELL <?php echo $symbol; ?>"
            data-order_type="MARKET">Sell <strong> <?php echo $symbol; ?></strong> stock</kite-button></td>
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
<th>Zerodha</th>
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
            <!-- zerodha button -->
            <td class="btn"> <kite-button href="#" data-kite="z8lgeb6fk65uargj"
            data-exchange="NSE"
            data-product="MIS"
            data-tradingsymbol="<?php echo $symbol;  ?>"
            data-transaction_type="BUY"
            data-quantity="10"
            class="kite-buy"
            title="BUY <?php echo $symbol; ?>"
            data-order_type="MARKET">Buy <strong> <?php echo $symbol; ?></strong> stock</kite-button></td>
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
<th>Zerodha</th>
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
            <!-- zerodha button -->
            <td class="btn"> <kite-button href="#" data-kite="z8lgeb6fk65uargj"
            data-exchange="NSE"
            data-product="MIS"
            data-tradingsymbol="<?php echo $symbol;  ?>"
            data-transaction_type="SELL"
            data-quantity="10"
            class="kite-sell"
            title="SELL <?php echo $symbol; ?>"
            data-order_type="MARKET">SELL <strong> <?php echo $symbol; ?></strong> stock</kite-button></td>
            <td><?php echo "chartlink";  ?></td>
        </tr>
<?php } ?>
</table>
</div>
</div>


<link rel="stylesheet" href="https://kite.zerodha.com/static/build/css/publisher.min.css">
<script src="https://kite.trade/publisher.js?v=3"></script>
</body>
</html>