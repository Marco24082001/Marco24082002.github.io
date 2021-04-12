// callback filter function
let arr = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];

arr.myfilter = function(compare) {
	let newArr = [];
	for(let i = 0; i < this.length; i++)
  {
  
  	if(compare(this[i])) newArr.push(this[i]);
  }
  return newArr;
}

console.log(arr.length);

let arr1 = arr.myfilter(ele => ele.length > 6);
console.log(arr1);

// callback map function
let arrMap = [2,3,5,6,7];
arr.mymap = function(callback) {
    
}

// callback map function
let arrMap = [1, 4, 9, 16];

arrMap.mymap = function(callback) {
  if(this == null)
  {
    throw new TypeError('this is null or not defined');
  }
  if (typeof callback !== 'function') {
      throw new TypeError(callback + ' is not a function');
  }
    console.log(this.length);
    let newArr = [];
    for(let i = 0; i < this.length; i++)
    {
    	let value = callback(this[i]);
      newArr.push(value);
    }
    return newArr;
} 

let arrMap1 = arrMap.mymap(x => x*2);
console.log(arrMap1);

// callback foreach function
let arrforeach = [1, 4, 9, 16];

arr.myforeach = function(callback)
{
	if(this == null) throw new TypeError('this is null or not defined');
  if (typeof callback !== 'function') throw new TypeError(callback + ' is not a function');
  
  for(let i = 0; i < this.length; i++)
  {
  	callback(this[i]);
  }
}

arrforeach.myforeach((x) => {
	console.log(x);
});

// callback reduce function
