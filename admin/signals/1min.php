<?php

$string = file_get_contents('../data/signals/1min.json');

$arr = json_decode($string,true);?>




<table class="table table-bordered table-hover table-responsive table-striped">
<tr>
<th>Exchange</th>
<th>Symbol</th>
<th>sma50</th>
<th>sma100</th>
<th>sma200</th>
<th>SMA SIGNAL</th>
<th>token</th>
<th>timestamp</th>
<th>Chart</th>
</tr>

<?php
foreach($arr as $exchange=>$stockarr){
    if (is_array($stockarr)){
        foreach($stockarr as $stockkey=>$stockval){
            
            ?> <tr>
            <td><?php echo $exchange;?>
            <td><?php echo $stockkey;?>
            <td><?php echo $arr[$exchange][$stockkey]['SMA']['sma50'];?>
            <td><?php echo $arr[$exchange][$stockkey]['SMA']['sma100'];?>
            <td><?php echo $arr[$exchange][$stockkey]['SMA']['sma200'];?>
            <td><?php echo $arr[$exchange][$stockkey]['SMA']['sma_signal'];?>
            <td><?php echo $arr[$exchange][$stockkey]['token'];?>
            <td><?php echo substr($arr[$exchange][$stockkey]['timestamp'],0,19);?>
            <td><?php echo "chartlink";?>
            </tr>
       <?php }
    }
}

?>


</table>

