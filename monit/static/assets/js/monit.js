$('#post_text').on('click',function(){
    var data = $('#input_text').val();
    ajax_post(data,0,0);
});
                  
// button_off post function.........
$('#button_off').on('click',function(){
    ajax_post(null,1,0);
});
                                        
// button_onn post function.........
$('#button_oon').on('click',function(){
    ajax_post(null,0,1);
});
                                                            
function ajax_post(data=null,button_off=0,button_oon=0){
    var url = ''; //type your url here..........
    var type = 'POST';
    var data = {
        text : data,
        button_off : button_off,
        button_oon : button_oon
    };
                                                                                                                                            
    $.ajax({
        url: url,
        type: type,
        data: data,
        success: function(response) {
            console.log(response);
        },
        error: function(jqXHR, exception, response) {
            console.log('Error');
            console.log(exception+response);
        }
    });
}
