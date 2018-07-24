window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function(){
        $(this).alert('close');
    });
    console.log("Hidden in 4 seconds");
}, 4000);

