 <img src ="/IMAGES/typescript2.png" width="200%">

# **TYPESCRIPT**

- Typescript is a statically-typed superset of JavaScript(JavaScript with type annotations).
- It helps us write robust and maintanable code.
- It checks for error during development rather than at runtime which JavaScript does.
- Typescript iteself doesn't add any optimization
- Typescript code is transpiled to JavaScript, TypeScript code can't be run in the browser directly.

# **Initialize a typescript project**

- Create a foler

  `mkdir project-name`

- change directory

  `cd project-name`

- run npm init(or npm init -y if you want things to be handled implicitly like name,version,description etc)

  `npm init -y`

- install typescript (preferring it to be installed globally on machine using -g flag)

  `npm install -g typescript`

  It will downloaded dependencies for typescript. It will also provide tsc(compiler for typscript) that will [**transpile**](#transpile) our transcript(.ts) file to JavaScript(.js) file. It will also allow us to create and modify [**tsconfig.json**](#tsconfig.json) file

# **Jargons**

- #transpile : Short for transforming, refers to the process of converting source code written in one language (such as typescript) to another language (such as typescript).
