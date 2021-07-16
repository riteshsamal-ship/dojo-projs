function reverse(arr) {
    // loop through half of the array
    for(var i=0; i<arr.length/2; i++) {
        // swap values across midpoint
        var temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
}

function rotate(arr, shiftBy) {
	let t = Math.abs(shiftBy);
	while(t > 0) {

		if(shiftBy > 0) {
			let temp = arr[arr.length-1]
			
			for(let i = arr.length - 1; i > 0; i--)
				arr[i] = arr[i-1];
			arr[0] = temp;

		} else {
			let temp = arr[0];
			for(let i = 0; i < arr.length - 1; i++) {
				arr[i] = arr[i + 1];
			}
			arr[arr.length-1] = temp;
		}
		t--;
	}
}

function filterRange(arr, min, max) {
	for(let i = 0; i < arr.length; i++) {
		if(arr[i] > min && arr[i] < max) {
			for(let j = i; j < arr.length - 1; j++) {
                arr[j] = arr[j + 1];
            }
            arr.length = arr.length - 1;
			i--;
		}
	}
}

function concat(arr1,arr2){
    var newarr = [];
    for(let i=0;i< arr1.length;i++)
    {
        newarr.push(arr1[i]);
    }
    for(let i=0;i<arr2.length;i++)
    {
        newarr.push(arr2[i])
    }
    return newarr;
}