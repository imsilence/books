<?php
$v1 = isset($_GET['v1']) ? $_GET['v1'] : 'v1';
$v2 = isset($_GET['v2']) ? $_GET['v2'] : 'v2';
?>

<html>
    <head>
        <meta charset="utf-8" />
        <title>xss charset</title>
    </head>
    <body>
        <form action="" method="get">
            <label>v1:</label><input type="text" name="v1" value="<?=$v1?>" maxlength="20"/>
            <label>v2:</label><input type="text" name="v2" value="<?=$v2?>" maxlength="50"/>
            <input type="submit" value="提交" />
            <div>
                <pre>
提示: 1. v1输入:<?=htmlspecialchars('"><script>alert(1)</script>')?>或<?=htmlspecialchars('"onclick="alert(2)')?> \n
     2. v2输入:<?=htmlspecialchars('"onclick="eval(location.href.substr(1))')?>
     3. v1输入:<?=htmlspecialchars('"><!--')?> v2输入:<?=htmlspecialchars('--><script>alert(1)</script>')?>
                </pre>
            </div>
        </form>
    </body>
</html>
