# **JavaScript**

- [**JavaScript**](#javascript)
- [Interview Questions](#interview-questions)
- [Destructuring](#destructuring)
  - [Destructuring Arrays](#destructuring-arrays)
  - [Destructuring Objects](#destructuring-objects)

# Interview Questions

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
