# rd-prompt3

**User:**  
in javascript, using the raindrop.io API, can you give me an example of how to print a list of all  
 my public collections, than do a loop through each collection, printing the "Title", "link", "tags" and "date" of each bookmark, and output to a markdown file using the name of the collection as the file name.

***

**ChatGPT:**  
Sure, here is an example of how you might do that using the raindrop.io API in JavaScript:

```javascript
const fetch = require('node-fetch');

async function getCollections() {
  // Get a list of all your public collections
  const res = await fetch('https://raindrop.io/api/collections/public?format=json');
  const collections = await res.json();

  // Loop through each collection
  for (const collection of collections) {
    const fileName = `${collection.title}.md`;

    // Open a new file for this collection
    const file = fs.createWriteStream(fileName);

    // Write the collection's title to the file
    file.write(`# ${collection.title}\n\n`);

    // Get the collection's bookmarks
    const bookmarkRes = await fetch(`https://raindrop.io/api/collections/${collection.id}?format=json`);
    const bookmarks = await bookmarkRes.json();

    // Loop through each bookmark and write its details to the file
    for (const bookmark of bookmarks) {
      file.write(`- Title: ${bookmark.title}\n`);
      file.write(`  Link: ${bookmark.link}\n`);
      file.write(`  Tags: ${bookmark.tags.join(', ')}\n`);
      file.write(`  Date: ${bookmark.created_at}\n\n`);
    }

    // Close the file
    file.close();
  }
}
```

This code uses the <code>node-fetch</code> library to make HTTP requests to the raindrop.io API, and the <code>fs</code> module to create and write to files. It first fetches a list of your public collections and then loops through each collection, creating a new file for that collection and writing the collection's title to the file. Then it fetches the bookmarks for that collection and writes each bookmark's details to the file. The bookmark details include the title, link, tags, and date.  
I hope this helps! Let me know if you have any other questions.

***

## *Exported By **Dustin Smith** on 12/23/2022, 5:54:28 AM*

---

#AI #ChatGPT
