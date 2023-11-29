function add()
{
    let a=parseInt(document.getElementById("first").value);
    let b=parseInt(document.getElementById("second").value);
    document.getElementById("sum").innerHTML=`sum : ${a+b}`
}