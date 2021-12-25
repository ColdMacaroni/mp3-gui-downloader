'https://superuser.com/a/140077
'Used to run it without a command window
Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c start_python_with_venv.bat"
oShell.Run strArgs, 0, false