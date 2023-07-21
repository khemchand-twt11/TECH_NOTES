# **MONGODB**

**Terminologies:**

- collection: can be thought of as a table, it is a collection of mondDB documents.
- documents: It's a basic unit of storage in mongoDB, can be thought of as rows in relational database.

## **Basic Commands**:

- `mongosh` command to open mongodb in the terminal
- `show dbs` to show all the database avilable
- `use <database-name>` to switch to a database, if not there it will create a new one
  Note: if we use `show dbs` after creating database, database will not be visible as there it is empty

### **collection queries**

**show collection**

- `show collection`: it shows all the collections inside a database, like different tables in mysql

**create collection**

- `db.createCollection('<collection-name>')`
- `db.posts.insertOne({name:"xyz",age:23})` it is used to insert a document inside the collection but even if the collection is not present this query will create a new one.

# **Crud Operations on a collection**

**insert data in collections**

- `db.<collection-name>.insertOne(object)` : insert a single document inside the database.
- `db.<collection-name>.insertMany(object)` : insert as many document as we want inside the database.
  Note: here object refers to documents that contains the data in key-value pairs, for Example
  {name:"khemchand",age:21,city:"Delhi"}

**find and findOne**
used to select data from the database. both accpets a query object as a parameter if not passed it will return all the documents.

find will return all the documents but findOne will return only one document in the collection if query object is not being passed.
