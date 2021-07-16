function greeting()
{
    return "Hello";
    console.log("World");
}
var word = greeting();
console.log(word);      /*Hello*/

function add(num1, num2)
{
    console.log("Summing Numbers!");
    console.log("num1 is: " + num1);
    console.log("num2 is: " + num2);
    var sum = num1 + num2;
    return sum;
}
var result1 = add(3,5);         /*Summing Numbers! num1 is: 3 num2 is:5 Summing Numbers! num1 is: 4 num2 is:7 8 11*/ 
var result2 = add(4,7);
console.log(result1);
console.log(result2);

function highFive(num)
{
    for(var i=0; i<num; i++)
    {
        if(i == 5)
        {
            console.log("High Five!");
        }
        else
        {
            console.log(i);             /*Considering there is no call for the function there would be no output but just in case if you gave the function any number from 
                                          1-5 then it would just print all numbers leading up to it -1, and if you do anything above 5 then it will print High five once.                                                                                          */
        }
    }
}