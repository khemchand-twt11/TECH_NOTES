# **HTML (HYPER TEXT MARKUP LANGUAGE)**

- Language that is used to create webpage on the internet.
- Hyper refers to Hyper links that is digital reference to data on the internet.
- Markup part means that we use instructions or special tags to give structure to the webpage.

### **Boilerprate code (basic structure for a webpage)**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body></body>
</html>
```

- `<!DOCTYPE html>` Refers that we are using html 5 which is the latest version of html.

- `<html lang="en">` It's the root or the top-level element of the webpage and everything is wrapped inside it and `lang="en"` specifies that the webpage is using english as it's language.

- `<head>` Contains meta-information(additional information about the webpage that provide context and instructions to the browser) about the webpage. content within head tag it's not directly visible inside the webpage.

  Head tag contains server important tags inside it

  - `<meta charset="UTF-8" />` This tag defines the character encoding of the webpage, It ensures that the browser display the text correctly by supporting a wide range of characters.

  - `<meta http-equiv="X-UA-Compatible" content="IE=edge" />` This tag makes sure your webpage works well with internet explorer. Here, first attribute give instructions to Internet Explrorer to work smoothly and compatible with certain instructions and standards for displaying webpages. Second attribute tells IE to use it's latest and best rendering engine
    here rendering engine can be thought of like brain of the browser that read and interepret code and display it accordingly on our screen.

  - `<meta name="viewport" content="width=device-width, initial-scale=1.0" />` This tag tells the browser how to handle and display webpage on different screen sizes. here `name=viewport` tells that it's defining the viewport, which is the visible part of the webpage on the scree. `content="width=device-width` It tells the browser that the width is equal to device width.`initial-scale=1.0"` It tells about the zoom level of the webpage when it loads first, 1.0 means the original size without zooming in or out.
