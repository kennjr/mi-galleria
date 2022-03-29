function copyUrl(url){
    /* Copy the text inside the text field */
    navigator.clipboard.writeText(format_url(url));
    console.log("The text was copied " + url);
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

function open_modal(url, description, category, caption, location, timestamp){
    var modal = document.querySelector('.modal');
    var img_cont = document.getElementById('img_container')
    var details_cont = document.getElementById('details_container')
    img_cont.innerHTML="<img class=\"selected_img\" src=\"/files/"+url+"\">";
    details_cont.innerHTML="<p class=\"details_caption_txt\">"+caption+"</p> <p class=\"details_description_txt\">"+description+"</p> <p class=\"details_category_txt\">"+category+"</p> <p class=\"details_location_txt\">"+location +",  "+ timestamp+"</p>";
    modal.style.display = "block";
}

function close_modal(url){
    var modal = document.querySelector('.modal');
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    var modal = document.querySelector('.modal');
      if (event.target == modal) {
        modal.style.display = "none";
      }
}



function format_url(url){
    return "http://127.0.0.1:8000/files/" + url
}