$(document).ready(function(){
    printPlanBoard();  
    addPlan();
    $("#plan-board-div").hide();
})
// add plan 버튼을 클릭 시 placeholder에 팀 이름 넣기
function addPlan(){
    $("#add-plan-btn").click(function(){
        var teamName = $("#plan-name-head").text();  
        $("#team-name-plan").attr('placeholder',teamName);
        $("#team-name-plan").attr('value',teamName);
    });
}
function printPlanBoard(){
    $(".team-list-li").on("click", function(){
        $("#plan-name-head").empty();
        $("#plan-name-head").append($(this).text());
        $("#plan-board-div").show();
        console.log($(this).text());
        $.ajax({
            url: '/onePage/planListClick/',
            type: 'POST',
            dataType: "json",
            contentType: 'application/x-www-form-urlencoded; charest=utf-8',
            data: {"teamName":$(this).text()},
            sucess:function(str){
                console.log("플랜 데이터 가져오기 성공");
                var html="";
                $.each(str, function (index, item) {
                    html = '<tr><td id = plan-board-no-'+item.planNo+'>'+item.planNo +'</td>';
                    html += '<td id = plan-board-name-content'+item.planNo+'>'+item.planName+'</td>';
                    html += '<td><button id = plan-board-del-btn-'+item.planNo+'>Delete Plan</button></td></tr>';
                });
                $("#plan-name-head").append("<h3>"+$(this).text()+"</h3>");
                $("#plan-list-board").append(html);
            },
            error:function(str){
                alert("플랜이 없습니다.");
            }
        });
    });
}