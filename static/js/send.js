$(function($){
	$('#form').on('submit',function(e){
		e.preventDefault();
		var db = $('#name').val();
		var user = $('#age').val();
		var type = $('#gen').val();
		var kpi = $('#dob').val();
		var unit = $('#dept').val();
		$.ajax({
			url: '/save',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$('#name,#age,#gen,#dob,#dept').val('');
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