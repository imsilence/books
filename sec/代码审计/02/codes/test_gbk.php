<!DOCTYPE html>
</html>
<head>
    <meta charset="gbk"/>
</head>
<body>
<?php
echo '<pre>';
$conn = mysql_connect('127.0.0.1','root','root');
mysql_select_db('mysql',$conn);
mysql_query("set names gbk");  //不安全的编码设置方式
mysql_query("set character_set_connection=gbk, character_set_results=gbk, character_set_client=gbk");  //不安全的编码设置方式
$res = mysql_query("show variables like 'character%';"); //显示当前数据库设置的各项字符集
while($row = mysql_fetch_array($res)){
var_dump($row);
}
$user = iconv('GBK', 'UTF-8',$user);
$user = addslashes($_GET['sql']); //mysql_real_escape_string() magic_quote_gpc=On addslashes() mysql_escape_string()功能类似
$sql = "SELECT host,user,password FROM user WHERE user='{$user}'";
echo $sql.'</br>';
if($res = mysql_query($sql)){
while($row = mysql_fetch_array($res)){
var_dump($row);
}
}
else{
echo "Error".mysql_error()."<br/>";
}


error_reporting(0);
$conn = mysql_connect('127.0.0.1','root','root');
mysql_select_db('mysql',$conn);
mysql_set_charset("utf8"); //推荐的安全编码
$user = mysql_real_escape_string(($_GET['sql'])); //推荐的过滤函数
$user = iconv('GBK', 'UTF-8',$user);
$sql = "SELECT host,user,password FROM user WHERE user='{$user}'";
echo $sql.'</br>';
$res = mysql_query($sql);
while($row = mysql_fetch_array($res)){
var_dump($row);
}
?>
