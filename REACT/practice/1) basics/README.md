## What is emmet?

Emmit is a powerful toolkit for web developers that enhance speed and efficiency of the workflow.

Emmet allows you to write complex HTML and CSS code using simple and abbreviated syntax.

It's useful for rapidly creating repetitive code structure

## Difference between a Library and Framework?

library is like a toolbox of different tools. we can pick and choose the tool that we want for our application.libraries are flexible, and you have more control over how to use them whereas framework is like a blueprint for building a specific type of structure. It provides a structure to our application and comes with predefined rules and components you must follow

## What is CDN ?

CDN stands for Content Delivery Network. It's a network of distributed servers that work together to deliver various types of web content, such as images, videos, stylesheets, scripts, and other assets, to users based on their geographical location.

## Why react is called react ?

The term "react" in this context refers to the library's ability to efficiently manage and update the user interface by "reacting" to changes in the underlying data

## What is crossorigin in script tag?

The crossorigin attribute in the `<script>` tag is used when loading external JavaScript files (scripts) from a different domain or server. It is used as a security measure to control how the browser should handle requests for these scripts when there might be potential issues related to Cross-Origin Resource Sharing (CORS).

crossorigin has three values:

1. anonymous
2. use-credentials
3. ommited(provide nothing)

## What is diference between React and ReactDOM ?

React is a library for building user interface, primarly focused on creation of reusable ui componenets

- ReactDOM is a special package that provides integration between React and browsers's document object model.
- Allows us to render react components into the actual DOM
- ReactDOM provides render() method, which is used to render react components into a specific DOM container

## What is difference between react.development.js and react.production.js files via CDN?

1. **react.development.js:**

- Meant for development.
- Larger file size.
- Includes warnings, error checks, and comments.
- Helps catch mistakes and debugging during development.

2. **react.production.js:**

- Optimized for production.
- Smaller file size.
- No warnings, error checks, or comments.
- Prioritizes performance for production deployments.

## Difference between normal script tag vs scirpt tag with async vs script tag with defer

1. **Normal script tag**

   - blocks HTML parsing until the external resources are being loaded and executed
   - can affect performance if script size is large or loading slow
   - useful for script that needs to be load before the DOM is ready.

2. **Script tag with async**

   - downloads the script asyncrhonously, allow html parsing to be executed continuously
   - Executes the script as soon as the script is downloaded
   - Suitable for script that dont' rely on other scripts or the DOM being ready.

3. **Script tag with defer**
   - downloads the script asyncrhonously, like `async`
   - Defer execution until HTML parsing is complete
   - Good for the script that needs to be run after the DOM is ready
