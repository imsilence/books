<?php
echo sprintf('<div>%s</div>', $_GET['o']);

/**
* http://localhost:9999/03_xss/01.php?o=<script>alert(1)</script>
*/
