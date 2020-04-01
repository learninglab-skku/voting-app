// javascript to query via ajax

setInterval(function () {
    $.ajax({
        url: "/ajax/check_vote",
        type: 'POST',
        data: {'check': true},
 
        success: function (data) {
            if (data.status) {
                $('[name="second_vote_status"]').innerText = str(data.status);
                alert("sth is going on");

                // var doc = $.parseHTML(json.notifications_list);
                // $('#notifications-list').html(doc);
            }
            alert("nothing going on");
        }
    });
    
    alert("nothing going on at all");
}, 5000);
