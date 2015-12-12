
$(function($){
	// $('#pri').hide();
	$('#form1').on('submit',function(e){
		e.preventDefault();
		$('#pri').hide();
		var db = $('#ask').val();
		$.ajax({
			url: '/show',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				alert('found');
				// $('#container1').hide();
				 // $('#pri').show();
				console.log(response);
			},
			error: function(error){
				alert('not found');
				console.log(error);
			}
		});
	});
});