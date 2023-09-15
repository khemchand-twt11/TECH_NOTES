# Latency, Bandwith and Throughtput

## Latency

The amount of time it takes for data to transfer from one location to another. It is measurment of time, not how much data being downloaded over that time. lowering latecny is the important part of good user experience.

### How to reduce latency

- By using CDN(Content Delivery Netowrk). A CDN cache static content and server it to the end user. CDN servers are located at different locations so that content is stored close to end user.
- Optimising images for faster loading, and reduce file size wherever possible.
- Code minification is a way of reducing the size of js and css files.

## Improving user experience without actually reducing the network latency

- Improved percieved page performance by strategically loading certain assets first. a webpage can be configured to load above-the-fold(what appears in the browsers window before the user scrolls) area of the page first so that user can begin interacting with the page even before it finishes loading
- Webpage can also load assets only when they are needed using technique known as `lazy loading`

above approaches doesn't improve latency but they improve user perception of improved speed.

## Bandwidth

Maximum amount of data that can be pass through a network at a given time.

## Throughtput

Average amount of data that actually passed through in a given period of time. it doesn't necessarily equivalent to bandwith because it is affected by latency, network congestion and other factors.
