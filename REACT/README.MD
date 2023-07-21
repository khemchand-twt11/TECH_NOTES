# **React Notes**

## Summary

This file contains my collection of notes on React. It covers various topics related to React development, including:

- [**React Notes**](#react-notes)
  - [Summary](#summary)
  - [Introduction](#introduction)
    - [Index.js Code Breakdown](#indexjs-code-breakdown)
  - [React Components](#react-components)
  - [importing and exporting components](#importing-and-exporting-components)
  - [props](#props)
  - [Chilren prop](#chilren-prop)
  - [React Hooks](#react-hooks)
    - [State Hooks](#state-hooks)
      - [useState](#usestate)
      - [useReducer](#usereducer)
    - [Context Hooks](#context-hooks)
      - [useContext](#usecontext)
    - [Ref Hooks](#ref-hooks)
      - [useRef](#useref)
      - [useImperativeHandle](#useimperativehandle)
    - [Effect Hooks](#effect-hooks)
      - [useEffect](#useeffect)
      - [useLayoutEffect](#uselayouteffect)
      - [useInsertionEffect](#useinsertioneffect)
    - [Performance Hooks](#performance-hooks)
      - [useMemo](#usememo)
      - [useCallback](#usecallback)
      - [useTransition](#usetransition)
      - [useDeferredValue](#usedeferredvalue)
    - [Other Hooks](#other-hooks)
      - [useDebugValue](#usedebugvalue)
      - [userId](#userid)
      - [useSyncExternalStore](#usesyncexternalstore)
  - [React Router](#react-router)
  - [React under the hood](#react-under-the-hood)
    - [React building blocks](#react-building-blocks)
      - [What is DOM ?](#what-is-dom-)
      - [What is Virtual DOM ?](#what-is-virtual-dom-)

## Introduction

- Open source JavaScript Library used for creating user interface
- Follows components based approach where each UI element is devided into reusable and
  independent components.
- Uses a virtual DOM (Document Object Model) to efficiently update and render components
  in response to changes.

### Index.js Code Breakdown

```js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
  console.log(a)
);
```

- Importing `React` module which is responsible for creating components and using JSX Syntax.
- Importing `ReactDOM` package which provides methods for rendering React Component into DOM.
- importig normal css file
- Importing `App` component from `./App` file. It is the main component of the application that will be rendered.
- Creating `root` instance using `ReactDOM.createRoot`, this root is responsible for rendering and updating the React application.
- `document.getElementById('root')` retrive the DOM element with id `root` where the React application will be mounted.
- `root.render()` method is called to render the application.
- `<React.StrictMode>` enable additional runtime checks and warnings.
- `<App/>` represents the `App` Component which is the main entry point of the application. It will be renderd as the root element of the application

## React Components

Component Syntax

```js
function Greeting() {
  return <h1>Learning React!</h1>
}
```

The syntax inside the function is not HTML it's JSX(JavaScript XML)

## importing and exporting components

There are two ways to export a component

- **using default keyword**

  while importing a component we can name the component anything that is exported using default keyword

- **without default keyword**

  while importing a component without using default we have to use the exact name as of the component, and also we have to use curly braces while importing

  example: `import {ExactName} from './ExactName.js'`

## props

Prop is a way to pass information from one component to another

```js
const author ='martin luthor';

const BookList()=>{
  return (
    <Book authorName = {author}/>
  )
}

function Book(props){
 return <h1>{props.authorName}</h1>
}

```

## Chilren prop

```js
const author = 'harry broose'
const BookList()=>{
  return (
    <Book authorName = {author}/><p>this is going to be a children prop</p></Book>
  )
}

function Book(props){
 return
   <>
  <h1>{props.authorName}</h1>
  {props.children}
  </props.children> // will show the paragraph
}
```

Note:

- Name can't be changed for children prop it will be same
- if we will pass multiple elements as children prop they will be passed in form of array

## React Hooks

Hooks let us use different react features from our components
There are total 15 hooks avilable at present

### State Hooks

state lets a component remember information/data
like user input

#### useState

it returns an array with two values

- First value represnets the variable or state data itself.
- Second value represents a setter function that allows us to update the state variable(first value).

```react

function App(){
  const [count,setCount] = useState(0);
}
```

#### useReducer

### Context Hooks

#### useContext

### Ref Hooks

#### useRef

#### useImperativeHandle

### Effect Hooks

#### useEffect

#### useLayoutEffect

#### useInsertionEffect

### Performance Hooks

#### useMemo

#### useCallback

To prioritize rendering, use one of these hooks.

#### useTransition

#### useDeferredValue

### Other Hooks

#### useDebugValue

#### userId

#### useSyncExternalStore

## React Router

- It is a popular library for handling routing in React application
- It is not a part of official react library
- Provide a way to manage navigation between different views.
- Content loaded without full page reload which happens in html based websites.

## React under the hood

### React building blocks

let's first go through some key points that will be important going forward.

#### What is DOM ?

- it's an abbreviation of document object model.
- It represent html pages as a tree of elements called nodes
- document is the root node
- DOM interface lets us do operations such as the addition, modification,or removal of items from the document.
- whenever any change happens to the DOM, the browser re-renders the UI.

let's look at the DOM representation of following html document.

```html
<html>
  <body>
    <nav>
      <h1>Hi</h1>
    </nav>
    <main>
      <p>React is awesome</p>
    </main>
  </body>
</html>
```

document-> html->body->(nav->h1,main->p)

#### What is Virtual DOM ?

- it's a replica of the actual DOM.
- it's an object create to resemble the actual DOM.
- it's less expensive than actual DOM as it doesn't write to the screen

  let's look at the virtual DOM representation of the following HTML document.

  ```html
  <div>
    <h1>Hi</h1>
    <p>React is awesome</p>
  </div>
  ```

  ```JavaScript
    {
      type: 'div',
      childrens: [
        {
          type: 'h1',
          text: 'Hi'
        },
        {
          type: 'p',
          text: 'React is awesome'
        }
      ]
    }
  ```

### What is JSX ?

- it's a syntax extension to js.
- with the help of it react combines HTML and JavaScript easily.
- usually refer it as syntatic sugar
- it is then converted to js using code transpiler called babel

### React core

- it contains all of the api required to define react components
- it is where we will find methods such as createElement.
- it also manages state management,communicate between various components, and so forth.

### React Render

- it takes charge or rendering react components on various platforms such as the web,mobile, and so on.

- different platforms utilize numerous rendering methods. for example in web apps , the DOM is utilized to render the content. to alter the dom and re-render the UI, we may use methods like appendChild() and remove() on the DOM nodes.
- for mobile apps , we require UI support straight from the operating system. however, the react library doesn't manage this, it is the rendere that performs all of the rendering taks for multiple platforms.

### React Reconciler

- It's the process through which react changes the browser DOM.
- It contains the diffing mechanism, which decides which part of tree the renderer should update.

## Context

context let's a component recieve information from it's distant parent without passing it as a props

Steps involved while using context

1. Create a context : firs step is to create a context using `createContext()` function provided by react. This creates an object that holds the shared data or state. The inital value can be passed as an argument to `createContext()`
2. Define a provider component: Next step is to define a provider component that will wrap all the components that need access to context value. It is responsibe for providing the context value to it's child components. It accepts a `value` prop that defines the data or state to be shared.
3. wrap the components: Wrap all the components in provider component that need access to context values
4. consume context value: To access the context value within a component we use `useContext()` that allow us to use context values directly by passing the context object(created in first step) as argument to the hook.

## Redux

It's a container state container for javascript applications

**Redux principles**

1. first principle: Entire state of an application is stored in a single javascript object called `state tree` or `store`.
2. second principle: State tree is immutable, it is readonly. Instead anytime we want to change state we dispatch an action(represent the change or update in the state). Action is a javascript object and it's structure is upto us but it has a `type` property that indicates the type of action being performed.

**Difference between pure and impure function**

**pure functions**:

1. Pure function soley depend on the input parameters being passed

   example:

   ```javascript
   function square(n) {
     return n * n
   }
   ```

2. Pure function doesn't cause any side effect(anything beyone computing and returning a value).

   example:

   ```javascript
   /* side effect being performed */

   function change(obj) {
     obj.price = 300
     return obj
   }
   ```

**Impure functions**

1. function that performs side effects.

   example:

   ```javascript
   function squareArray(items) {
     for (let i = 0; i < items.length; i++) {
       items[i] = items[i] ** 2
     }
   }
   ```
