<?php require("head.php"); ?>

<script type="text/javascript">
  $(document).ready(function(){
    $('.watchlist').css({"background-color": "lightblue", "font-size": "120%"});
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
    <!-- main contents   -->

    <div class="container">
  <div class="row">
<div class="col-sm-12">
  <ul class="list-inline">
   <li><button class="btn btn-success">NSE NIFTY</button></li>
   <li><button class="btn btn-success">NSE 500</button></li>
   <li><button class="btn btn-success">NSE FO STOCK</button></li>
   <li><button class="btn btn-success">MCX COMMODITY</button></li>
   <li><button class="btn btn-success">NSE CDS</button></li>
   <li><button class="btn btn-success">NSE FO</button></li>
   <li><button class="btn btn-success">NSE FUTURE</button></li>
   <li><button class="btn btn-success">NSE OPTION</button></li>
   <li><button class="btn btn-success">NSE ANY</button></li>

  </ul>
</div>
</div>
</div>


<div class="container-fluid">
<table class="table table-bordered table-hover table-responsive table-striped">
<tr>
<th>ID</th>
<th>Exchange</th>
<th>Symbol</th>
<th>category</th>
<th>exchange_symbol</th>
<th>trend_monthly</th>
<th>trend_weekly</th>
<th>trend_daily</th>
<th>trend_60min</th>
<th>group_name</th>
<th>price</th>
<th>sector</th>
<th>industry</th>
<th>mcap</th>
<th>volume</th>
</tr>
<!-- show_watchlist.php -->
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
$query=mysqli_query($con,"select * from watchlist");
$cnt=1;
while($row=mysqli_fetch_array($query))
{
?>
<tr>
<td><?php echo "ID"?> </td>
<td><?php echo $row['exchange'];?></td>
<td><?php echo $row['symbol'];?></td>
<td><?php echo $row['category'];?></td>
<td><?php echo $row['exchange_symbol'];?></td>
<td><?php echo $row['trend_monthly'];?></td>
<td><?php echo $row['trend_weekly'];?></td>
<td><?php echo $row['trend_daily'];?></td>
<td><?php echo $row['trend_60min'];?></td>
<td><?php echo $row['group_name'];?></td>
<td><?php echo $row['price'];?></td>
<td><?php echo $row['sector'];?></td>
<td><?php echo $row['industry'];?></td>
<td><?php echo $row['mcap'];?></td>
<td><?php echo $row['volume'];?></td>
 </tr>
 <?php
$cnt=$cnt+1;
 } ?>
</table>
</div>

<!-- add_watchlist.php -->
<div class="container-fluid">
<form action="/admin/add_watchlist.php">
<ul class="list-inline">
<li><input type="text" placeholder="ID" style="width:70px"></li>
<li><input type="button" onclick=window.alert("LOAD") value="LOAD" style="width:100px"></li>

<li><input type="text" placeholder="Exchange" style="width:70px"></li>
<li><input type="text" placeholder="symbol" style="width:100px"></li>
<li> <select name="" id="">
<option value="Select Category" style="width:70px">Select Category</option>
<option value="Blacklist">Blacklist</option>
<option value="Whitelist">Whitelist</option>

</select>
</li>
<li><input type="text" placeholder="sector" style="width:100px"></li>
<li><input type="text" placeholder="industry" style="width:100px"></li>
<li><input type="button" onclick=window.alert("ADD") value="ADD" style="width:100px"></li>
<li><input type="button" onclick=window.alert("UPDATE") value="UPDATE" style="width:100px"></li>
<li><input type="button" onclick=window.alert("DELETE") value="DELETE" style="width:100px"></li>
<li><input type="reset" value="Reset" style="width:100px"></li>
</ul>
</form>
</div>
<?php ?>

<div style="margin-top:50px; padding-top:10px;"></div>


</body>
</html>