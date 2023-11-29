function add()
{
    let a=parseInt(document.getElementById("ft").value);
    let b=parseInt(document.getElementById("sd").value);
    document.getElementById("rt").innerHTML=`sum : ${a+b}`
}
function sub()
{
    let a=parseInt(document.getElementById("ft").value);
    let b=parseInt(document.getElementById("sd").value);
    document.getElementById("rt").innerHTML=`sub : ${a-b}`
}
function mul()
{
    let a=parseInt(document.getElementById("ft").value);
    let b=parseInt(document.getElementById("sd").value);
    document.getElementById("rt").innerHTML=`mul : ${a*b}`
}
function div()
{
    let a=parseInt(document.getElementById("first").value);
    let b=parseInt(document.getElementById("second").value);
    document.getElementById("rt").innerHTML=`div : ${a/b}`
}
