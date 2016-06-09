var inputCall,inputResponse;
var result;

$(document).ready(function(){
  inputCall=$('#inputCall');
  inputResponse=$('#inputResponse');
  $('#sendButton').on('click touchstart', buttonTouched);
  //クォートに置換する
  resultText=result_text.replace(/&quot;/g,"\"")
  result = JSON.parse(resultText)

  //はじめにレコードがないテーブルが生成されるので削除
  $(".no-records-found").remove();

  //テーブル要素の追加
  resultBody = $('#resultBody');

  $.each(result, function(index, value) {
    tempContent = $("<tr></tr>").append('<td>'+value[0]+'</td><td>'+value[1]+'</td><td>'+value[2]+'</td>');
    resultBody.append(tempContent);
  });

  $('#contentTable').addClass('table-striped');
});

function buttonTouched(){
  var inputCallText = inputCall.val();
  var inputResponseText = inputResponse.val();

  if(!formValueValidation(inputCallText)){
    alert('話しかける人の言葉の入力エラー！！！')
    return false;
  }
  if(!formValueValidation(inputResponseText)){
    alert('返信の入力エラー！！！')
    return false;
  }

  $.post("/botwords",
    { call: inputCallText, response: inputResponseText },
    function(data){
      if(data!==''){
        alert("|のみの入力は禁止です！！！！");
        return false;
      }
      alert("送信しました！"+data);
      inputCall.val('');
      inputResponse.val('');
    }
  );
}

function formValueValidation(value){
  if(value===''){
    return false;
  }
  return true;
}
