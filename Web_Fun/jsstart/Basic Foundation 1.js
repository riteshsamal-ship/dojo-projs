function get255()
{
    var newArr=[];
    for (var i=1;i<=255;i++)
    {
        newArr.push(i);
    }
    return(newArr);
}

function geteven1000()
{
    var sum=0;
    for(var i=0;i<=1000;i++)
    {
        if(i%2==0)
        {
            sum=i+sum;
        }
    }
    return(sum)
}

function sumodd5000()
{
    var sum=0;
    for(var i=0;i<5000;i++)
    {
        if(i%2!=0)
        {
            sum=i+sum;
        }
    }
    return sum;
}

function iteratearray(newArr)
{
    var sum=0;
    for(var i=0;i<newArr.length;i++)
    {
        sum=sum+newArr[i];
    }
    return sum;
}

function findmax(newArr)
{
    var max=0;
    for(var i=0;i<newArr.length;i++)
    {
        if(max<newArr[i])
        {
            max=newArr[i];
        }
    }
    return max;
}

function findaverage(newArr)
{
    sum=0;
    for(var i=0;i<newArr.length;i++)
    {
        sum=sum+newArr[i];
    }
    sum=sum/newArr.length;
    return sum;
}

function Arrayodd()
{
    var newArr=[];
    for(var i=0;i<=50;i++)
    {
       if(i%2!=0)
       {
           newArr.push(i);
       } 
    }
    return newArr;
}

function greaterthan(newArr,y)
{
    sum=0;
    for(var i=0;i<newArr.length;i++)
    {
        if(y<newArr[i])
        {
            sum++;
        }
    }
    return sum;
}

function squares(newArr)
{
    for(var i=0;i<newArr.length;i++)
    {
        newArr[i]=(newArr[i]*newArr[i]);
    }
    return newArr;
}

function Negatives(newArr)
{
    for(var i=0;i<newArr.length;i++)
    {
        if(0>newArr[i])
        {
            newArr[i]=0;
        }
    }
    return newArr;
}

function maxminavg(newArr)
{
    sum=0;
    max=0;
    min=1000000000000;
    var rArr=[];
    for(var i=0;i<newArr.length;i++)
    {
        if(newArr[i]>max)
        {
            max=newArr[i];
        }

        if(newArr[i]<min)
        {
            min=newArr[i];
        }
        sum=sum+newArr[i];
    }
    sum=sum/newArr.length;
    rArr.push(max);
    rArr.push(min);
    rArr.push(sum);
    return rArr;
}

function swapvalues(newArr)
{
    var first=newArr[0];
    var last=newArr[newArr.length-1];
    newArr[newArr.length-1]=first;
    newArr[0]=last;
    return newArr;
}

function negtostring(newArr)
{
    for(var i=0;i<newArr.length;i++)
    {
        if(0>newArr[i])
        {
            newArr[i]="Dojo";
        }
    }
    return newArr;
}

console.log(get255());
console.log(geteven1000());
console.log(sumodd5000());
var newArr=[1,2,5,10];
console.log(iteratearray(newArr));
console.log(findmax(newArr));
console.log(findaverage(newArr));
console.log(Arrayodd());
console.log(greaterthan(newArr,1));
console.log(squares(newArr));
var testArr=[1,2,5,10,-33];
console.log(Negatives(testArr));
console.log(maxminavg(testArr));
console.log(swapvalues(testArr));
var negArr=[47,-12,67,-9,9];
console.log(negtostring(negArr));

