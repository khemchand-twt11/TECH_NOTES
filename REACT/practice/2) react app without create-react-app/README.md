## Dependencies vs Dev Dependencies

1. **Dependencies**

   - Essential for the functionality of our application at runtime.
   - commands to install packages as dependencies
     - `npm i <package-name>`

2. **Dev Dependencies**
   - Contains packages that are needed during development. such as testing tools, build tools(ex bundlers),
   - commands to install packages as dev dependencies
     - `npm i <package-name> --save-dev`
     - `npm i <package-name> -D`

## package.json vs package.lock.json

1. **package.json**

   - configuration file for node.js projects
   - Metadata name,version,scripts(used to define custom scripts or commands that can be executed using npm)
   - Manually maintained
   - List dependencies(dependencies and devDependencies)

2. **pacakge.lock.json**
   - Auto-generated
   - Lock dependencies versions(ensure consistent and specific versions)
   - ensures consistent installs ( same dependencies for all)
   - reduce conflicts(minimise version conflicts)
   - works with `npm install`

## HMR(Hot Module Reloading)

- Allow web component to be updated as you develop without the need or manually refershing the browser.
