 <img src ="/IMAGES/typescript2.png" width="200%">

# **TYPESCRIPT**

- Typescript is a statically-typed superset of JavaScript(JavaScript with type annotations).
- It helps us write robust and maintanable code.
- It checks for error during development rather than at runtime which JavaScript does.
- Typescript iteself doesn't add any optimization
- Typescript code is transpiled to JavaScript, TypeScript code can't be run in the browser directly.

# **Initialize a typescript project**

- Create a foler

  ```
  mkdir project-name
  ```

- change directory

  ```
  cd project-name
  ```

- Run npm init(or npm init -y if you want things to be handled implicitly like name,version,description etc)

  ```
  npm init -y
  ```

- Install typescript (preferring it to be installed globally on machine using -g flag)

  ```
  npm install -g typescript
  ```

  It will downloaded dependencies for typescript. It will also provide tsc(compiler for typscript) that will [**transpile**](#important-terms) our transcript(.ts) file to JavaScript(.js) file. It will also allow us to create and modify `tsconfig.json` file

- You can check globally installed npm packages using command

  ```
  npm list -g
  ```

- Create a typescript configuration file

  ```
  npx tsc --init
  ```

  It creates a `tsconfig.json` file that is used to customize the transpilation process

- add the below code to tsconfig.json file

  ```
  {
  "compilerOptions": {
    "target": "ES6",
    "module": "commonjs",
    "outDir": "dist",
    "strict": true
  },
  "include": [
    "src/**/*.ts"
  ],
  "exclude": [
    "node_modules"
  ]
  }
  ```

# **Important Terms**

- **transpile** : Short for transforming, refers to the process of converting source code written in one language (such as JavaScript) to another language (such as typescript).

```

```

```

```
