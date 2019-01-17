<?php

$string = file_get_contents('../data/signals/15min.json');

$arr = json_decode($string,true);?>




<table class="table table-bordered table-hover table-responsive table-striped">
<caption class="bg-info text-center">15 Min Signals</caption>
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
            $sma50 =$arr[$exchange][$stockkey]['SMA']['sma50'];
            $sma100 = $arr[$exchange][$stockkey]['SMA']['sma100'];
            $sma200 = $arr[$exchange][$stockkey]['SMA']['sma200'];
            $sma_signal = $arr[$exchange][$stockkey]['SMA']['sma_signal'];
            ?> <tr>
            <td><?php echo $exchange;?>
            <td><?php echo $stockkey;?>
            <td class="<?php if($sma50 =='BUY_SIGNAL'){echo "bg-success";} elseif ($sma50=="SELL_SIGNAL"){echo "bg-danger";} {
                # code...
            } ?>"><?php echo $sma50;?>
            <td  class="<?php if($sma100 =='BUY_SIGNAL'){echo "bg-success";} elseif ($sma100=="SELL_SIGNAL"){echo "bg-danger";} {
                # code...
            } ?>"><?php echo $sma100;?>
            <td  class="<?php if($sma200 =='BUY_SIGNAL'){echo "bg-success";} elseif ($sma200=="SELL_SIGNAL"){echo "bg-danger";} {
                # code...
            } ?>"><?php echo $sma200;?>
            <td  class="<?php if($sma_signal =='BUY_SIGNAL'){echo "bg-success";} elseif ($sma_signal=="SELL_SIGNAL"){echo "bg-danger";} {
                # code...
            } ?>"><?php echo $sma_signal;?>
            <td><?php echo $arr[$exchange][$stockkey]['token'];?>
            <td><?php echo substr($arr[$exchange][$stockkey]['timestamp'],0,19);?>
            <td><?php echo "chartlink";?>
            </tr>
       <?php }
    }
}

?>


</table>
