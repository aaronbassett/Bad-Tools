<?php
$opts = array(
  'http'=>array(
    'method'=>"GET",
    'header'=>"Accept: text/plain"
  )
);

$context = stream_context_create($opts);
$handle = fopen("http://www.codingexcuses.com", "r", false, $context);
$contents = stream_get_contents($handle);

print $contents;
