<?php require("head.php"); ?>

<script type="text/javascript">
  $(document).ready(function(){
    $('.marketwatch').css({"background-color": "lightblue", "font-size": "120%"});
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
   <li><button class="btn btn-success">Nifty 50</button></li>
   <li><button class="btn btn-success">NSE FO</button></li>
   <li><button class="btn btn-success">NSE NEXT 50</button></li>
   <li><button class="btn btn-success">MCX COMMODITY</button></li>
   <li><button class="btn btn-success">NCDEX COMMODITY</button></li>
   <li><button class="btn btn-success">NSE 500</button></li>
  
  </ul>
</div>
</div>
</div>



<!--ohlc data -->

<div class="container">
<table class="table table-bordered table-hover table-responsive table-striped">
<tr>
<th>ID(TimeStamp)</th>
<th>Exchange</th>
<th>Symbol</th>
<th>token_by_zerodha</th>
<th>industry</th>
<th>nifty_50</th>
<th>nifty_fo</th>
<th>nifty_next_50</th>
<th>nifty_500</th>
<th>daily_volatility</th>
</tr>

<?php 
$servername = "localhost:3308";
$username = "root";
$password = "";
$dbname = "test";

$con = mysqli_connect($servername,$username,$password,$dbname);
// Check connection
if (mysqli_connect_errno())
{
 echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
else{
  echo "connected ";
}?>

<?php
$query=mysqli_query($con,"select * from stock_details");
$cnt=1;
while($row=mysqli_fetch_array($query))
{
?>
<tr>
<td><?php echo "ID"?> </td>
<td><?php echo $row['exchange'];?></td>
<td><?php echo $row['symbol'];?></td>
<td><?php echo $row['token_by_zerodha'];?></td>
<!-- <td><?php echo $row['industry'];?></td>
<td><?php echo $row['nifty_50'];?></td>
<td><?php echo $row['nifty_fo'];?></td>
<td><?php echo $row['nifty_next_50'];?></td>
<td><?php echo $row['nifty_500'];?></td>
<td><?php echo $row['daily_volatility'];?></td> -->
 </tr>
 <?php
$cnt=$cnt+1;
 } ?>
</table>
</div>
<!-- space setup -->
<div style="margin-bottom:50px; padding-bottom:10px;"></div>


</body>

</html>