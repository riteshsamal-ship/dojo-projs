var testArr = [6,3,5,1,2,4]
var sum=0;
for(var i=0; i<testArr.length;i++)
{
    sum=testArr[i]+sum;
    console.log("Num:"+testArr[i]+", Sum:"+ sum);
}

var testArr = [6,3,5,1,2,4]
var newArr= [];
for(var i=0; i<testArr.length;i++)
{
    newArr[i]= testArr[i]*i;
}

console.log(newArr);