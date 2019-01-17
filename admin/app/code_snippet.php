
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