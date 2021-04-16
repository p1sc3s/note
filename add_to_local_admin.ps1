$e = (Get-LocalGroup | where name -Like "*adm*" | where name -NotLike "hyper-v*").name;Add-LocalGroupMember -Group $e -Member "lab\owner"
