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
                <h3 class="text-center"> SignUp to Algo</h3>
                <form class="form-horizontal">


                <div class="form-group">
                        <label for="inputfname" class="control-label col-xs-4">First Name</label>
                        <div class="col-xs-8">
                            <input type="text" class="form-control" id="input" placeholder="First Name">
                        </div>
                </div>

                <div class="form-group">
                        <label for="inputlname" class="control-label col-xs-4">Last Name</label>
                        <div class="col-xs-8">
                            <input type="text" class="form-control" id="inputlname" placeholder="Last Name">
                        </div>
                </div>

                <div class="form-group">
                        <label for="inputgender" class="control-label col-xs-4">Gender</label>
                        <div class="col-xs-8">
                            
                        
<span>
  <input type="radio" id="male" name="gender" value="male">
  <label for="male">Male</label>
</span>

<span>
  <input type="radio" id="female" name="gender" value="female">
  <label for="female">Female</label>
</span>


                            <!--<input type="text" class="form-control" id="inputgender" placeholder="Last Name">-->
                        </div>
                </div>

                <div class="form-group">
                        <label for="inputEmail" class="control-label col-xs-4">Email ID</label>
                        <div class="col-xs-8">
                            <input type="email" class="form-control" id="inputEmail" placeholder="User id or Email">
                        </div>
                    </div>




                    <div class="form-group">
                        <label for="inputEmail" class="control-label col-xs-4">User ID</label>
                        <div class="col-xs-8">
                            <input type="email" class="form-control" id="inputEmail" placeholder="User id or Email">
                        </div>
                    </div>
                    <div id="responsedata"></div>
                    <div class="form-group">
                        <label for="inputPassword" class="control-label col-xs-4">Password</label>
                        <div class="col-xs-8">
                            <input type="password" class="form-control" id="inputPassword" placeholder="Password">
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <div class=" col-xs-8 col-xs-offset-4">
                            <button type="submit" class="btn btn-primary col-xs-8">Sign Up</button>
                            <button type="reset" class="btn btn-danger col-xs-4">Reset</button>
                           
                        </div>
                    </div>

                    
                </form>

            </div>
        </div>
    </div>
<?php require("foot.php"); ?>