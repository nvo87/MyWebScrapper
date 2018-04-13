// jQuery(document).ready(function($) {
//     $('.js-scrapper-delete').on('click', function(event) {
//         event.preventDefault();
//
//         var $this = $(this);
//         var $scrapperForm = $this.closest('.scrapper-form-wrapper');
//         var $scrapper = $scrapperForm.closest('.scrapper');
//         var scrapper_id = $scrapperForm.find('.scrapper_id').val();
//
//         $.ajax({
//             url: '/delete-scrapper/'+scrapper_id,
//             type: 'POST',
//             data: {
//                 scrapper_id: scrapper_id
//             }
//         })
//         .done(function() {
//             console.log("success");
//             $scrapper.remove();
//         })
//         .fail(function() {
//             console.log("error");
//         })
//         .always(function() {
//             console.log("complete");
//         });
//
//     });
// });