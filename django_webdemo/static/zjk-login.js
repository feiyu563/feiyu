(function(arg){
	arg.extend({
	'check':function(form){
		$(form).find(':submit').click(function(){
			var flag=true;
			$(form).find(':text,:password').each(function(){
				var name=$(this).attr('name');
				var value=$(this).val();
				if(!value || value.trim()==''){
					flag=false;
					font='× ** '+name+' 不能为空!';
					html="<span style='color:red;'>"+font+"</span>";
					$(this).next().remove();
					$(this).after(html);
				}else{
					html="<span style='color:green;'>√</span>";
					$(this).next().remove();
					$(this).after(html);
				}
			})
			return flag;
		})
	}
	})
})(jQuery)