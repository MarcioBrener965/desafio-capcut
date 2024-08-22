$exclude = @("venv", "bot_capcut.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_capcut.zip" -Force