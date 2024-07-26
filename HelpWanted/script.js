function refreshPage(){
    window.location.reload();
} 

function setCookie(){
    document.cookie = "friend = false";
}

function resetCookies(){
    document.cookie = "friend = false";
}

function getCookie(){
    return document.cookie;
}

function authenticate(){
    var authorised;
    

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    

    if(username == "MikeSchmidt" && password == "ProtectAbby" && getCookie() == friend == "true"){
      authorised = true;
    }else{ 
      authorised = false;

      alert("Sorry, that login is incorrect.");
    }
 
    return authorised;
  }