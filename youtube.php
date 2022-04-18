<?php
    $command = escapeshellcmd('musica_youtube.py');
    $output = shell_exec($command);
    echo $output;
?>