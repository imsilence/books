<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <div id="result"></div>
        <input type="text" id="input" value="<a onclick='alert(1)'>click</a>"/>
        <input type="button" value="show" id="show"/>
        <script type="text/javascript">
            var result = document.getElementById('result'),
                input = document.getElementById('input'),
                button = document.getElementById('show');

            button.addEventListener('click', function() {
                result.innerHTML = input.value;
            }, false);
        </script>
    </body>
</html>
