 $("#id_brand").change(function () {
      var str = $("#CarForm").attr("data-versions-url");
      var url = str.replace(' ','');
      var brandId = unescape($(this).val());
      $.ajax({
        url: url,
        data:{
          'brand':brandId          
        },
        success: function (data) {
          unescape($("#id_version").html(data));
        }
      });
    });


$(document).ready(function(){  
$("#step-1").css('display', 'block');
$("#step-2").css('display', 'none');
$("#step-3").css('display', 'none');
//$("#searchresult").css('display', 'none');

   $("#image2").css('display', 'none');
   $("#image3").css('display', 'none');
   $("#image4").css('display', 'none');
   $("#image5").css('display', 'none');
   $("#image6").css('display', 'none');
   $("#image7").css('display', 'none');

$("#image1").change(function(){
   $("#image2").css('display', 'block');});

$("#image2").change(function(){
   $("#image3").css('display', 'block');});

$("#image3").change(function(){
   $("#image4").css('display', 'block');});

$("#image4").change(function(){
   $("#image5").css('display', 'block');});

$("#image5").change(function(){
   $("#image6").css('display', 'block');});

$("#image6").change(function(){
   $("#image7").css('display', 'block');});



      
    

});

// Function that executes on click of first next button.
function next_step1() {
document.getElementById("step-1").style.display = "none";
document.getElementById("step-2").style.display = "block";
document.getElementById("two").addclass="active";
document.getElementById("one").classList.remove("active");
document.getElementById("one").classList.add("passed");
}
// Function that executes on click of first previous button.
function prev_step1() {
document.getElementById("step-1").style.display = "block";
document.getElementById("step-2").style.display = "none";
document.getElementById("two").classList.remove("active");
document.getElementById("one").classList.add("active");
document.getElementById("one").classList.remove("passed");
}
// Function that executes on click of second next button.
function next_step2() {
document.getElementById("step-2").style.display = "none";
document.getElementById("step-3").style.display = "block";
document.getElementById("three").classList.add("active");
document.getElementById("two").classList.add("passed");
document.getElementById("two").classList.remove("active");

}
// Function that executes on click of second previous button.
function prev_step2() {
document.getElementById("step-3").style.display = "none";
document.getElementById("step-2").style.display = "block";
document.getElementById("three").classList.remove("active");
document.getElementById("two").classList.add("active");
document.getElementById("two").classList.remove("passed");

}

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle("active");

        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}

//$("#search").on('click',function(){
 // $("#searchresult").css('display', 'block');
//});

//function show_search_result() {

//document.getElementById("searchresult").style.display = "block";}

