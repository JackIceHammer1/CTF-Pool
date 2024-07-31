<?php

# If ur reading this, good luck reading my crappy code :)

$code = $_POST['code'];
$code = explode("<body>", $code);
$code = explode("</h1>", $code[1]);

if(strpos(htmlspecialchars($code[0]), "&lt;h1&gt;Dunder Mifflin Infinity") !== false)
{

  $code = explode("</a>", $code[1]);

  if(strpos(htmlspecialchars($code[0]), "&lt;a href='/home.html'&gt;Home") !== false)
  {
    if(strpos(htmlspecialchars($code[1]), "&lt;a href=&quot;/shop.html&quot;&gt;Shop") !== false)
    {
      if(strpos(htmlspecialchars($code[2]), "&lt;a href=&quot;/cart.html&quot;&gt;Cart") !== false)
      {

        $code = explode("</h2>", $code[3]);

        if(strpos(htmlspecialchars($code[0]), "&lt;h2&gt;Welcome to Dunder Mifflin Infinity!") !== false)
        {

          $code = explode(">", $code[1], 2);

          if(strpos(htmlspecialchars($code[0]), "&lt;img src=&quot;logo.png&quot;") !== false)
          {

            $code = explode("</h3>", $code[1]);

            if(strpos(htmlspecialchars($code[0]), "&lt;h3&gt;Dwights Paper Picks") !== false)
            {

              $code = explode(">", $code[1], 4);

              if(strpos(htmlspecialchars($code[0]), "&lt;img src=&quot;glossystock.jpg&quot;") !== false)
              {
                if(strpos(htmlspecialchars($code[1]), "&lt;img src=&quot;legalpaper.jpg&quot;") !== false)
                {
                  if(strpos(htmlspecialchars($code[2]), "&lt;img src=&quot;collegeruled.png&quot;") !== false)
                  {

                    $code = explode("</h6>", $code[3]);

                    if(strpos(htmlspecialchars($code[0]), "&lt;h6&gt;Ⓒ 2000-2015 &lt;br&gt; Talk to a representative: (443)-797-3842") !== false)
                    {
                      $url = "Location: " . strlen($code[1]) . ".html";
                      header($url);
                      exit();
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}

echo $_POST['code'];
exit();

?>