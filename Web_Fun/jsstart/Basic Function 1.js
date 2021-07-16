function a(){
    return 35;  /*35*/
}
console.log(a())

function a(){
    return 4;   /*8*/ 
}
console.log(a()+a())

function a(b){
    return b;   /*6*/ 
}
console.log(a(2)+a(4));

function a(b){
    console.log(b);
    return b*3;     /*3 9*/
}
console.log(a(3));

function a(b){
    return b*4;     /*40*/ 
    console.log(b);
 }
 console.log(a(10));

 function a(b){
    if(b<10) {
        return 2;
    }
    else     {
        return 4;       /*4*/
    }
    console.log(b);
}
console.log(a(15));

function a(b,c){
    return b*c;         /*10 3 30*/
}
console.log(10,3);
console.log( a(3,10) );

function a(b){
    for(var i=0; i<10; i++){
        console.log(i);    /*3 4*/
    }
    return i;
}
console.log(3);
console.log(4);

function a(){
    for(var i=0; i<10; i++){
        i = i +2;
        console.log(i); /*2 5 8 11*/
    }
}
a();

function a(b,c){
    for(var i=b; i<c; i++) {
       console.log(i);          /*0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0*/
   }
   return b*c;
}
a(0,10);
console.log(a(0,10));

function a(){
    for(var i=0; i<10; i++){
       for(var j=0; j<10; j++){
           console.log(j);
       }
       console.log(i);          /*There is no call for the function so nothing happens*/
    }
}

function a(){
    for(var i=0; i<10; i++){
        for(var j=0; j<10; j++){
            console.log(i,j);
        }                       /*There is no call for the function so nothing happens*/
        console.log(j,i);
    }
}

var z = 10;
function a(){
    var z = 15;
    console.log(z);     /*10*/
}
console.log(z);

var z = 10;
function a(){
    var z = 15;
    console.log(z);     /*15 10*/
}
a();
console.log(z);

var z = 10;
function a(){
    var z = 15;
    console.log(z);     /*15 15*/
    return z;
}
z = a();
console.log(z);