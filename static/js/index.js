var inputCall,inputResponse;

$(document).ready(function(){
  inputCall=$('#inputCall');
  inputResponse=$('#inputResponse');
  $('#sendButton').on('click touchstart', buttonTouched);
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
