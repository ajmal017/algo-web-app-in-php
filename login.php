<?php require("head.php"); ?>

<link rel="stylesheet" href="/css/login.css">
    <!-- top menu -->
    <nav class="navbar navbar-default navbar-fixed-top  pagesetup">
      <?php require("menu.php"); ?>
    </nav>

    <!-- bottom menu -->
    <nav class="navbar navbar-default  navbar-fixed-bottom pagesetup">
    <?php require("menu.php"); ?>
    </nav>

    <div style="margin-top:50px; padding-top:10px;"></div>
    <!-- main contents   -->

    <div class="container">
        <div class="row">
            <div class="col-sm-4 col-sm-offset-4">
                <h3 class="text-center"> Login to Algo</h3>
                <form class="form-horizontal">
                    <div class="form-group">
                        <label for="inputEmail" class="control-label col-xs-2">User</label>
                        <div class="col-xs-10">
                            <input type="email" class="form-control" id="inputEmail" placeholder="User id or Email">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="inputPassword" class="control-label col-xs-2">Password</label>
                        <div class="col-xs-10">
                            <input type="password" class="form-control" id="inputPassword" placeholder="Password">
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="col-xs-offset-2 col-xs-10">
                            <div class="checkbox">
                                <label><input type="checkbox"> Remember me</label>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="col-xs-offset-2 col-xs-10">
                            <button type="submit" class="btn btn-primary">Login</button>
                            <a href="/reset_password.php"> <span class="btn btn-danger">Forget Password</span> </a>
                            <a href="/sign_up.php"> <span class="btn btn-info pull-right">Sign Up </span> </a>
                        </div>
                    </div>
                </form>

            </div>
        </div>
    </div>
<?php require("foot.php"); ?>