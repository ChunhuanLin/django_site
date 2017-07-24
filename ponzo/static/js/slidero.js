/**
 * Created by gaoshuai on 2017/4/5.
 */
$( function() {
    var handle = $( "#ratio-handle" );
    $( "#slider" ).slider({
        orientation:"horizonal", min: 50, max: 150,
        create: function() {
			var val = parseFloat($(this).slider("value"))/100.0;
            handle.text( val.toString() );
        },
        slide: function( event, ui ) {
			var val = parseFloat(ui.value)/100.0;
            handle.text( val.toString() );
        }
    });
} );
