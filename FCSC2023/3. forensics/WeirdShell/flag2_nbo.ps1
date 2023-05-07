
$s = "FCSC{$(([System.BitConverter]::ToString(([System.Security.Cryptography.SHA256]::Create()).ComputeHash(([System.Text.Encoding]::UTF8.GetBytes(((Get-Process -Id $PID).Id.ToString()+[System.Security.Principal.WindowsIdentity]::GetCurrent().Name).ToString()))))).Replace('-', '').ToLower())}`n"

echo $s

echo "avec mes valeurs"

$s = "FCSC{$(([System.BitConverter]::ToString(([System.Security.Cryptography.SHA256]::Create()).ComputeHash(([System.Text.Encoding]::UTF8.GetBytes(("14856ITESOFT\nbo")))))).Replace('-', '').ToLower())}`n"

echo $s

echo "Leur valeurs depuis le log alerte"

$s = "FCSC{$(([System.BitConverter]::ToString(([System.Security.Cryptography.SHA256]::Create()).ComputeHash(([System.Text.Encoding]::UTF8.GetBytes(("3788FCSC\cmaltese")))))).Replace('-', '').ToLower())}`n"

$s = "FCSC{$(([System.BitConverter]::ToString(([System.Security.Cryptography.SHA256]::Create()).ComputeHash(([System.Text.Encoding]::UTF8.GetBytes(("3788FCSC\cmaltese")))))).Replace('-', '').ToLower())}`n"


echo $s
