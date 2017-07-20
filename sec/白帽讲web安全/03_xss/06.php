<?php
$charset='gbk';
header(sprintf('Content-Type: text/html; charset=%s', $charset));
function escape($str) {
    return str_replace('"', '\"', $str);
}

$str = isset($_GET['o']) ? $_GET['o'] : 'test';

/*
* http://localhost:9999/06.php?o=%c1%22;alert(2);//
*/
?>
<html>
    <head>
        <meta charset="<?=$charset?>" />
        <title>xss charset</title>
    </head>
    <body>
        <button onclick="btn_click();">xss</button>
        <script type="text/javascript">
        var btn_click = function() {
            var text = "<?=escape($str)?>";
            alert(text);
        }
        </script>
    </body>
</html>
