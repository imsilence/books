<?php
file_put_contents('store.txt', $_GET['o']);

header('location:/03_xss/03.php');
/**
* http://localhost:9999/03_xss/02.php?o=<script>alert(1)</script>
*/
