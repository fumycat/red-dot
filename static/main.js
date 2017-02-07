function getAjaxData(w) {
    $.ajax({type: 'POST',
            url: '/ajax/' + w.toString(),
            success: function(response) {
                // var result = JSON.parse(response);
                $('#lvl-name').text(response.h);
                $('#main-text').text(response.text);
                $('#button-box').replaceWith(response.divs);
            }
        });
        e.preventDefault();
}

$(document).ready(function(){
    getAjaxData(0)
});
