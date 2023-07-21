# **JavaScript**

- [**JavaScript**](#javascript)
- [Interview Questions](#interview-questions)
- [Destructuring](#destructuring)
  - [Destructuring Arrays](#destructuring-arrays)
  - [Destructuring Objects](#destructuring-objects)
- [polyfills](#polyfills) - [polyfill of Filter method](#polyfill-of-filter-method)

# Interview Questions

hi why are you

# Destructuring

### Destructuring Arrays

### Destructuring Objects

```js
const destructor = ({
  name,
  age,
  hobbies: [e, t, m],
  meta: { height, isMarried },
}) => {
  console.log(name, age, e, t, m, height, isMarried);
};

const obj = {
  name: "gaurav",
  age: "21",
  hobbies: ["eating", "travel", "music"],
  meta: {
    height: "5ft",
    isMarried: "false",
  },
};
destructor(obj);
```

# polyfills

pollyfill is a piece of code that is used to provide modern functionallity on older browsers that do not natively support it.

#### polyfill of Filter method

```js
Array.prototype.myFilter = function (callback) {
  let tempArr = [];
  for (let i = 0; i < this.length; i++) {
    if (callback(this[i], i, index)) {
      tempArr.push(this[i]);
    }
  }
  return tempArr;
};

const arr = [1, 2, 3, 4, 5, 6, 7];
const evenArray = arr.myFilter((val, i, arr) => val % 2 === 0);
console.log(evenArray);
```
