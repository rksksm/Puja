$(function($){
	$('#prt').hide();
	$('#new').hide();
	$('#print').hide();

	$('#form2').on('submit',function(e){
		e.preventDefault();
		var user = $('#enroll').val();
		var type = $('#dis').val();
		var kpi = $('#dep').val();
		$.ajax({
			url: '/conferm',
			data: $('#form2').serialize(),
			type: 'POST',
			success: function(response){
				alert(response)
				$('#cre').text(new Date());
				$('#dep1').text(response);
				console.log(response);
			},
			error: function(error){
				alert('SERVER ERROR CONTACT ADMIN');
				console.log(error);
			}
		});
	});
});