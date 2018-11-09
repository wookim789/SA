$(document).ready(function(){
    makePlanBoard();  
})

function makePlanBoard(){
    $(".team-list-li").on("click", function(){
        console.log($(this).text());
        $.ajax({
            url: '/onePage/planListClick/',
            type: 'POST',
            dataType: "json",
            contentType: 'application/x-www-form-urlencoded; charest=utf-8',
            data: {"teamName":$(this).text()},
            sucess:function(str){
                var html="";
                if(str.result !="NoResultData")
                $.each(str, function (index, item) {
                    html = '<tr><td id = plan-board-no-'+item.planNo+'>'+item.planNo +'</td>';
                    html += '<td id = plan-board-name-content'+item.planNo+'>'+item.planName+'</td>';
                    html += '<td><button id = plan-board-del-btn-'+item.planNo+'>Delete Plan</button></td></tr>';
                });
                console.log("sssss");
                console.log($(this).text());
                $("#plan-name-head").append("<h3>"+$(this).text()+"</h3>");
                $("#plan-list-board").append(html);
  
            },
            error:function(str){
                console.log(str);
                alert("통신 실패");
            }
        })
    })
}