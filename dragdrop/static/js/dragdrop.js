var obj = $("#dragandrophandler");
obj.on('dragenter', function (e) 
{
    e.stopPropagation();
    e.preventDefault();
    $(this).css('border', '2px solid #0B85A1');

});
obj.on('dragover', function (e) 
{
     e.stopPropagation();
     e.preventDefault();
     $("#dragandrophandler").css('background-color', '#ffffe0');
});
obj.on('drop', function (e) 
{
     $(this).css('border', '2px dotted #0B85A1');
     e.preventDefault();
     var files = e.originalEvent.dataTransfer.files;

     //We need to send dropped files to Server
     $("#dropedfile").val(files[0].name);
     $("#dragandrophandler").css('background-color', '#ffffff');

});
$(document).on('dragenter', function (e) 
{
    e.stopPropagation();
    e.preventDefault();
    $("#dragandrophandler").css('background-color', '#ffffff');

});
$(document).on('dragover', function (e) 
{
  e.stopPropagation();
  e.preventDefault();
  obj.css('border', '2px dotted #0B85A1');
});
$(document).on('drop', function (e) 
{
    e.stopPropagation();
    e.preventDefault();
});