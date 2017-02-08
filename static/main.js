function getAjaxData(w) {
    $.ajax({type: 'POST',
            url: '/ajax/' + w.toString(),
            success: function(response) {
                $('#main-container').replaceWith(response);
            }
        });
}

$(document).ready(function(){
    getAjaxData(0)
});
