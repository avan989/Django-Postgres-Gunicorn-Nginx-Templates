$.ajax({
    url: 'api/developer_endpoint/',
    type: 'GET',
    dataType: 'json',
    success: function(json){

        $.each(json, function(index, obj){

            console.log(obj.title)

        });

    },
    error: function(xhr, ajax_options, error){
        console.log("error request");
        console.log(xhr.status);
        console.log(error);
    }
})