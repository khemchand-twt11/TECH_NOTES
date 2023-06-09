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
  return <h1>Learning React!</h1>;
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
