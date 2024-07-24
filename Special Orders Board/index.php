<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    echo "lbctf{GIMME_LEWIS_UNDERWEAR}";
    exit; 
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stardew Valley</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            text-align: center;
        }
        .fullscreen-img {
            width: 100vw;
            height: 100vh;
            object-fit: cover;
        }
        .content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: #5e7e47;
        }
        .content h1 {
            font-size: 36px;
            margin-bottom: 20px;
        }
        .content p {
            font-size: 18px;
            line-height: 1.5;
            max-width: 600px;
            margin: 0 auto;
            padding: 0 20px;
        }
    </style>
</head>
<body>

    <img class="fullscreen-img" src="Special_Orders_Final.png" alt="Stardew Valley Background">

    <div class="content">
        <p>
            Welcome to Pelican Town, we just finished setting up our Special Orders Board, feel free to help out others in need of requests, or POST your own. Maybe you will get a special reward.
        </p>

</body>
</html>
