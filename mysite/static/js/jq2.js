$(function(){
var $container = $('#container');
$container.imagesLoaded(function(){
$container.masonry({
itemSelector : '.item',
 isAnimated: true,
columnWidth : 240
});
});
});