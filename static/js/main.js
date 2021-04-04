$(window).on("load", function() {
	setTimeout(function () {
	$(".loading").hide();
	$(".msger").fadeIn(800);
}, 3000);
});

    let dark=0;
   


  
  $(".fa-certificate").on("click", function() {
    
    if(dark == 0) {
      dark = 1;
    
    }
    else if(dark == 1) {
      dark = 0;
    }
    $.ajax({
      url: "/t2",
      type: "GET",
      data: {dark},
      success:function(data){
       console.log('success');
       a=dark;
       console.log(a);
       window.location.replace("/t1");
     
       
       
      }
    });
   
  });   
 

 