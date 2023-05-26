<?php
function xor_encrypt($in) {
    $key = 'KNHL'; // Use unencrypted string as key
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

// 1. base64 decode encrypted string
$base64decoded = '{"showpassword":"yes","bgcolor":"#ffffff"}';
//$base64decoded = base64_decode("KNHLKNHLKNHLKNHLKYBEIOBKOVPTJHLKNJ");


// 2. Execute XOR function
$secretKey = xor_encrypt($base64decoded);

// 3. Print secret key
print(base64_encode($secretKey));
?>