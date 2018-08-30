/**
 * dropdownコントロール
 */
(function($){
	/* humburger menu */
	function removeMenu($shade){
		$shade
		.remove();
		$('#js-slidemenu').slideUp('fast');
	}
	$('#slidemenu-btn').on('click', function(e){
		e.preventDefault();
		var $shade = $('.js-slidemenu-effect')[0];
		if($shade === undefined) {
			$('<div>')
			.addClass('js-slidemenu-effect')
			.on('click', function(){
				removeMenu(this);
			})
			.appendTo($('body'));
			$('#js-slidemenu').slideDown('fast');
		} else {
			removeMenu($shade);
		}
	});
})(jQuery);

$(function(){
    //.accordionの中のli要素がクリックされたら
	$('.accordion li').click(function(){
		//クリックされた.accordionの中のp要素に隣接するul要素が開いたり閉じたりする。
		$(this).next('ul').slideToggle('fast');
 
	});
});