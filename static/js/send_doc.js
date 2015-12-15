$(function($){
	$('#form').on('submit',function(e){
		e.preventDefault();
		var db = $('#name').val();
		var type = $('#gen').val();
		$.ajax({
			url: '/regDoc',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$('#name,#gen').val('');
				alert('inserted');
				console.log(response);
			},
			error: function(error){
				alert('not inserted');
				console.log(error);
			}
		});
	});
});