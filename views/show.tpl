<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>社員旅行Botが喋ること</title>

  <link rel="stylesheet" type="text/css" href="css/bootstrap.css">
  <!-- Latest compiled and minified CSS -->
  <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.10.1/bootstrap-table.min.css">
</head>
<body>
<div class="container">
  <!-- Forms
  ================================================== -->
  <div class="bs-docs-section">
    <div class="row">
      <div class="col-lg-12">
        <div class="page-header">
          <h1 id="forms">社員旅行Botが喋ることリスト</h1>
          正規表現をあまり上手に書いていないので、喋らない可能性もあります。
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-12 table-responsive">
        <table data-toggle="table" id='contentTable'>
          <thead class='btn-primary'>
              <tr>
                  <th>ID</th>
                  <th>話しかける人の言葉</th>
                  <th>返信</th>
              </tr>
          </thead>
          <tbody id='resultBody'>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>


<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<!-- Latest compiled and minified JavaScript -->
<script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.10.1/bootstrap-table.min.js"></script>
<!-- Latest compiled and minified Locales -->
<script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.10.1/locale/bootstrap-table-ja-JP.min.js"></script>
<script>var result_text = '{{result}}';</script>
<script src="js/show.js"></script>

</body>
</html>
