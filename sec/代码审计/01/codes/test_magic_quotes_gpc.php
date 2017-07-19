<?php
if($_GET['name'] == 'kk\\\'') {
    echo('magic_quotes_gbc is on');
} else {
    echo('magic_quotes_gbc is off');
}
