$(function($){
	$('#form').on('submit',function(e){
		e.preventDefault();
		var db = $('#name').val();
		var user = $('#enroll').val();
		var type = $('#gen').val();
		var kpi = $('#dob').val();
		$.ajax({
			url: '/save',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$('#name,#enroll,#gen,#dob').val('');
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