/***
 * HMR(hot module reloading)
 * file watcher algorithm (c++)
 * Building
 * minify
 * cleaing code
 * superfast build algorithm
 * Image optimization
 * Caching while development
 * compression
 * compatible witholder versions of browsers
 * https on development
 * manages port number
 * consistent hashing algorithm
 * zero config
 * Tree shaking (remove unwated code)
 *
 *
 * Transitive Dependencies
 */
import React from 'react'
import ReactDOM from 'react-dom/client'
const heading = React.createElement('h1', {}, 'hello world!')
const div = React.createElement('div', {}, heading)

const root = ReactDOM.createRoot(document.getElementById('root'))

root.render(div)

// to run app `npx parcel index.html `
