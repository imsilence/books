<?php

if($user == 'kk') {
    echo('register_globals is on');
} else {
    echo('register_globals is off');
}

/*
curl -XGET "localhost/test_register_globals.php?user=kk"
*/
