<?php
session_start();
if(!isset($_SESSION['token'])) {
    mt_srand(time());
    $_SESSION['token'] = mt_rand();
}
echo <<<END
<html>
    <head>
        <meta charset="utf-8"/>
        <title>cookie劫持</title>
    </head>
    <body>
        {$_SESSION['token']}
        <script type="text/javascript" src="http://localhost:19999/03_xss/cookie.js"></script>
    </body>
</html>
END;


/**
* http://localhost:9999/03_xss/05.php
*/
