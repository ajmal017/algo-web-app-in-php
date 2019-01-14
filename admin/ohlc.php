<?php require("head.php"); ?>

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
   <li><button class="btn btn-success">Monthly</button></li>
   <li><button class="btn btn-success">Weekly</button></li>
   <li><button class="btn btn-success">Daily</button></li>
   <li><button class="btn btn-success">60 Min</button></li>
   <li><button class="btn btn-success">15 Min</button></li>
   <li><button class="btn btn-success">5 Min</button></li>
   <li><button class="btn btn-success">1 Min</button></li>
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
<th>date_and_time</th>
<th>open_price</th>
<th>high_price</th>
<th>low_price</th>
<th>close_price</th>
<th>volume</th>
<th>cp</th>
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
$query=mysqli_query($con,"select * from ohlc_monthly");
$cnt=1;
while($row=mysqli_fetch_array($query))
{
?>
<tr>
<td><?php echo "ID"?> </td>
<td><?php echo $row['exchange'];?></td>
<td><?php echo $row['symbol'];?></td>
<td><?php echo $row['date_and_time'];?></td>
<td><?php echo $row['open_price'];?></td>
<td><?php echo $row['high_price'];?></td>
<td><?php echo $row['low_price'];?></td>
<td><?php echo $row['close_price'];?></td>
<td><?php echo $row['volume'];?></td>
<td><?php echo $row['cp'];?></td>
 </tr>
 <?php
$cnt=$cnt+1;
 } ?>
</table>
</div>
<!-- space setup -->
<div style="margin-bottom:50px; padding-bottom:10px;"></div>
<?php require("foot.php"); ?>