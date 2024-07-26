function setPage(){
    var cameraPage = document.getElementById("camera").value;
    window.location.replace(""+cameraPage+".html")
    console.log(cameraPage);
}