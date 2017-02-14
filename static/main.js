function getAjaxData(w) {
    $.ajax({type: 'POST',
            url: '/ajax/' + w.toString(),
            success: function(response) {
                $('#main-container').replaceWith(response);
            }
        });
    var btn = $("#gotohome");
    if (w != 0){
        btn.slideDown();
    } else {
        btn.slideUp();
    }
}

$(document).ready(function(){
    getAjaxData(0)
});
