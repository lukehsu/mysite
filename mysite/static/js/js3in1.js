$(function(){

    var $container = $('#container');

    $container.imagesLoaded(function(){
      $container.masonry({
        itemSelector: '.item',
        columnWidth: 20,
        isAnimated: true,
        isFitWidth: true
      });
    });

    $container.infinitescroll({
      navSelector  : 'div.nav',    // selector for the paged navigation
      nextSelector : 'div.nav a',  // selector for the NEXT link (to page 2)
      itemSelector : '.item',     // selector for all items you'll retrieve
      loading: {
      	  img: '../static/pic/6RMhx.gif',
		  msgText: 'loading....',
		  finishedMsg: 'no more...'
	    }

      },
      // trigger Masonry as a callback
      function( newElements ) {
        // hide new items while they are loading
        var $newElems = $( newElements ).css({ opacity: 0 });
        // ensure that images load before adding to masonry layout
        $newElems.imagesLoaded(function(){
          // show elems now they're ready
          $newElems.animate({ opacity: 1 });
          $container.masonry( 'appended', $newElems, true );
        });
      }
	);

});

