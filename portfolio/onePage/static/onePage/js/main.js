var userId;
var userPw;
$(document).ready(function( ) {
 

	// Menu settings
  //var initgnMenu = new gnMenu(document.getElementById('gn-menu'));

  // Carousel
  $('.carousel').carousel({
    interval: 5500
  })

  var slideIndex = 1;
  showDivs(slideIndex);
  
  $("#logout-link").click(function(){
    alert("logout");
    $(location).attr('href',"/../");
  })

   $(".tablinks").click(function(){
      //console.log($(this).attr('value'))
      jamTab(event, $(this).attr("value"))
    })
  document.getElementById("make-team-tab-btn").click();
// When the user clicks anywhere outside of the modal, close it

});

var slideIndex = 1;
function showDivs(n) {
  
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";  
  }
  x[slideIndex-1].style.display = "block";  
}
function plusDivs(n) {
  showDivs(slideIndex += n);
}

function jamTab(evt, tabId) {
  // Declare all variables
  var i, tabcontent, tabcontentID, tablinks, tabID;
 
  tabID = tabId

 // console.log(tabID)
  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
      //console.log("tab = " + tabcontent[i].id)
     // console.log(tabcontent[i].getAttribute("value"))
      if(tabcontent[i].getAttribute("value")==tabID){
        tabcontentID = tabcontent[i].id;
        //console.log("tab 33= "+ tabcontentID);
      }
      tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");

  for (i = 0; i < tablinks.length; i++) {
      //console.log(tablinks[i])
      tablinks[i].className = tablinks[i].className.replace("active", "");
  }
  //
  // Show the current tab, and add an "active" class to the button that opened the tab
  
  document.getElementById("make-team-tab-btn").disabled= false;
  document.getElementById("search-team-tab-btn").disabled= false;
  document.getElementById("manage-team-tab-btn").disabled=false;
  document.getElementById("message-team-tab-btn").disabled=false;

  document.getElementById(tabcontentID).style.display = "block";
  evt.currentTarget.className += "active";

}