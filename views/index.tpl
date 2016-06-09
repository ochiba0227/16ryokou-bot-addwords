<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>社員旅行Botに喋って欲しいことを書くところ</title>

  <link rel="stylesheet" type="text/css" href="botwords/css/bootstrap.css">
</head>
<body>
<div class="container">
  <!-- Forms
  ================================================== -->
  <div class="bs-docs-section">
    <div class="row">
      <div class="col-lg-12">
        <div class="page-header">
          <h1 id="forms">社員旅行Botに喋って欲しいことを書くところ</h1>
          入力された言葉は自動的にBotに追加されます。
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="well bs-component">
          <form id="inputForm" class="form-horizontal">
            <fieldset>
              <div class="form-group">
                <label for="inputCall" class="col-lg-2 control-label">話しかける人の言葉</label>
                <div class="col-lg-10">
                  <input type="text" class="form-control" id="inputCall" placeholder="|で区切って複数の言葉も可 (例：チョコ|チョコレート)">
                </div>
              </div>
              <div class="form-group">
                <label for="inputResponse" class="col-lg-2 control-label">返信</label>
                <div class="col-lg-10">
                  <input type="text" class="form-control" id="inputResponse" placeholder="|で区切って複数の言葉も可 (例：甘い|苦い) ランダムで出力されます">
                </div>
              </div>
              <div class="form-group">
                <div class="col-lg-10 col-lg-offset-2">
                  <button type="button" id="sendButton" class="btn btn-primary pull-right">送信！</button>
                </div>
              </div>
            </fieldset>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>


<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="botwords/js/bootstrap.min.js"></script>
<script src="botwords/js/index.js"></script>

</body>
</html>
