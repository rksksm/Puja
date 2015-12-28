
$(function($){
	$('#pri').hide();
	$('#form1').on('submit',function(e){
		e.preventDefault();
		$('#pri').hide();
		var db = $('#ask').val();
		var user = $('#enroll').val();
		var type = $('#dis').val();
		var kpi = $('#dep').val();
		$.ajax({
			url: '/show',
			data: $('#form1').serialize(),
			type: 'POST',
			success: function(response){
				$("#name").text(response.name);
				$("#dob").text(response.dob);
				$("#gen").text(response.gen);
				$('#container1').hide();
				$('#enroll').val(db);
				$('#enrollCopy').val(db);
				$("h3").text("Patient Details of  "+db);
				$("#name,#age,#dob,#enrollCopy,#gen").prop('disabled', true);
				$('#pri').show();
				console.log(response);

			},
			error: function(error){
				alert('Not found, register this Patient');
				location.href='insStud';
		$.ajax({
			url: '/show',
			data: $('#form2').serialize(),
			type: 'POST',
			success: function(response){
				alert('found');
				$('#container1').hide();
				 $('#pri').show();
				console.log(response);
			},
			error: function(error){
				alert('not found');
				console.log(error);
			}
		});
	});
});