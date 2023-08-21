


$('.reply-btn').click(function() {
  $(this).parent().next('.replied-comments').fadeToggle()
});

$(document).ready(function(event){
  
    $(document).on('click', '#like', function(event) {
            event.preventDefault();
            var pk = $(this).attr('value');
            $.ajax({
                type: 'POST',
                url: '/like/', //{% url "like_post" %}',
                data: {"id":pk, "csrfmiddlewaretoken":  $("input[name='csrfmiddlewaretoken']").val(),},
                dataType: 'json', 
                success: function(response){
                  $('#like-section').html(response['form'])
                },
                error: function(rs, e){
                    console.log(rs.responseText)
                  
                },   
            });
      }); 
  

    $(document).on('submit', '.comment-form', function(event){
      event.preventDefault();
      console.log($(this).serialize());
      $.ajax({
        type: 'POST',
        url: $(this).attr('action'),
        data: $(this).serialize(),
        dataType: 'json',
        success: function(response) {
          $('.main-comment-section').html(response['form']);
          $('textarea').val('');
          
        },
        error: function(rs, e) {
          console.log(rs.responseText);
        },
      });
    });

    $(document).on('submit', '.opinion-form', function(event){
      event.preventDefault();
      console.log($(this).serialize());
      $.ajax({
        type: 'POST',
        url: $(this).attr('action'),
        data: $(this).serialize(),
        dataType: 'json',
        success: function(response) {
          $('.main-opinion-section').html(response['form']);
          $('textarea').val('');
          $('.reply-btn').click(function() {
            $(this).parent().next('.replied-comments').fadeToggle();
            $('textarea').val('');
          });
        },
        error: function(rs, e) {
          console.log(rs.responseText);
        },
      });
    });


    $(document).on('submit', '.reply-form', function(event){
      event.preventDefault();
      console.log($(this).serialize());
      $.ajax({
        type: 'POST',
        url: $(this).attr('action'),
        data: $(this).serialize(),
        dataType: 'json',
        success: function(response) {
          $('.main-opinion-section').html(response['form']);
          $('textarea').val('');
          $('.reply-btn').click(function() {
            $(this).parent().next('.replied-comments').fadeToggle();
            $('textarea').val('');
          });
        },
        error: function(rs, e) {
          console.log(rs.responseText);
        },
      });
    });
  

  });


/* Profile Page */
$('.myNav ul li').click(function(){
  $(this).addClass("active").siblings().removeClass('active');

});


const tabBtn = document.querySelectorAll('.myNav ul li');
const tab = document.querySelectorAll('.tab');

function tabs(panelIndex) {
  tab.forEach(function(node) {
      node.style.display = 'none';
    
  });
  tab[panelIndex].style.display = 'block';
}
tabs(0);

