<?php
// Check if file is uploaded
if(isset($_FILES['file'])) {
    $file = $_FILES['file'];
    $file_name = $file['name'];
    $file_tmp = $file['tmp_name'];

    // Validate file extension
    $file_ext = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));
    if($file_ext == "jpg") {
        // Check if the specified bytes have the correct values
        $content = file_get_contents($file_tmp);
        if(ord($content[0]) == 10 && ord($content[1]) == 8) {
            echo "lbctf{i_luv_f0rtn1te}";
        } else {
            echo "The witch's HEX is still on the file maybe u need to verify the file, how many seasons were in chapter 1 and 2?";
        }
    } else {
        echo "The witch must have changed the file type. my favortie skins are (J)onesy, (P)eter griffin, and no(G) ops.";
    }
} else {
    echo "gimme back my skin pls";
}
?>

