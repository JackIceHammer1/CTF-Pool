function refreshPage(){
    window.location.reload();
} 

function setCookie(){
    document.cookie = "sorcerer = false";
}

function resetCookies(){
    document.cookie = "sorcerer = false";
}

function getCookie(){
    return document.cookie;
}

function authenticate(){
    var authorised;
    

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    

    if(username == "KokichiMuta" && password == "PlsIdleTransfigureMeDaddyMahito" && checkSorcererCookie()){
      authorised = true;
    }else{ 
      authorised = false;

      alert("MECHAMARU SAYS NO");
    }
 
    return authorised;
  }

  function checkSorcererCookie() {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.indexOf('sorcerer=') === 0) {
            var sorcererValue = cookie.substring('sorcerer='.length);
            if (sorcererValue.toLowerCase() === 'true') {
                return true;
            }  
            else {
              return false;
            }
            break;
        }
    }
}
