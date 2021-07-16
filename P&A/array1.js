function pushFront(arr, value) {
	// move all values in array over
	for(let i = arr.length; i > 0; i--)
    {
        arr[i] = arr[i-1]
    }
	
	arr[0] = value;
}

function popFront(arr) {
	var val = arr[0];
	for(let i = 0; i < arr.length; i++)
    {
		arr[i] = arr[i + 1];
    }
	arr.length = arr.length - 1;
	return val;
}

function insertAt(arr, idx, val) {
	for(let i = arr.length; i > idx; i--)
		arr[i] = arr[i-1]
	
	arr[idx] = val;
}