var items=[];
$(function($){
	$('#form').on('submit',function(e){
		e.preventDefault();
 		$('input:radio[name=user]:checked').each(function() 
   			 {
       				items.push( $(this).val());
       				// alert($(this).val());
       				$.ajax({
			url: '/delete',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$("input").prop('disabled', true);
				location.reload();
				alert('Deleted');
				console.log(response);
			},
			error: function(error){
				alert('not deleted');
				console.log(error);
			}
		});

   			 });
		
	});
});