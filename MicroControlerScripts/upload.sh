host=$1
password=$2
code=$3
sshpass -p "$password" ssh $host "echo $code > output.py"
