import express from "express";
import bodyParser from "body-parser";
import axios from "axios";
import pg from "pg";

const app = express();
const port = 3000;

app.use(express.static("./public"));
app.use(bodyParser.urlencoded({ extended: true }));

const bookCovers = {
  "La Odisea": 9781505595161,
  "Wimpy Kid": 9789955222729,
  "GOT" : 9780553381689,
  "Meditations": 9780812968255,
  "The Art of War": 9781566192972,
  "Bible" : 9781885217950,
  "1984": 9780451524935,
  "To Kill a Mockingbird": 9780061120084,
  "The Catcher in the Rye": 9780316769488,
  "Pride and Prejudice": 9780486284736,
  "Harry Potter and the Philosopher's Stone": 9780590353403,
  "The Great Gatsby": 9780743273565,
  "The Lord of the Rings": 9780544003415,
  "The Hobbit": 9780618260300,
  "The Hunger Games": 9780439023481,
  "Animal Farm": 9780451526342,
  "Alice's Adventures in Wonderland": 9780141439761,
  "The Chronicles of Narnia": 9780064404990,
  "The Da Vinci Code": 9780307474278,
  "The Shining": 9780307743657,
  "The Girl with the Dragon Tattoo": 9780307454546,
  "The Help": 9780425232200,
  "The Alchemist": 9780062315007,
  "The Catcher in the Rye": 9780316769488,
  "The Girl on the Train": 9781594634024,
  "The Girl with the Dragon Tattoo": 9780307454546,
  "The Kite Runner": 9781594634024,
  "The Book Thief": 9780375842207,
  "Gone with the Wind": 9780446675536,
  "Twilight": 9780316015844,
  "Divergent": 9780062387240,
  "The Fault in Our Stars": 9780142424179,
  "The Lovely Bones": 9780316666343,
  "The Help": 9780425232200,
  "The Hunger Games": 9780439023481,
  "The Notebook": 9780446605236,
  "Harry Potter and the Sorcerer's Stone": 9780590353427,
  "Harry Potter and the Chamber of Secrets": 9780439064873,
  "Harry Potter and the Prisoner of Azkaban": 9780439136365,
  "Harry Potter and the Goblet of Fire": 9780439139601,
  "Harry Potter and the Order of the Phoenix": 9780439358071,
  "Harry Potter and the Half-Blood Prince": 9780439785969,
  "Harry Potter and the Deathly Hallows": 9780545010221,
  "The Da Vinci Code": 9780307474278,
  "Angels & Demons": 9780743493468,
  "Inferno": 9781101974789,
  "The Lost Symbol": 9780307950688,
  "Digital Fortress": 9781250020155,
  "Jurassic Park": 9780345538987,
  "The Lost World": 9780345402882,
  "The Andromeda Strain": 9780061703157,
  "Timeline": 9780345539014,
  "Sphere": 9780345538987,
  "Prey": 9780061703157,
  "Congo": 9780345378491,
  "Eaters of the Dead": 9780345415486,
  "Rising Sun": 9780399141146,
  "The Rainmaker": 9780345531964,
  "The Firm": 9780440245926,
  "The Pelican Brief": 9780385339709,
  "A Time to Kill": 9780385338603,
  "The Chamber": 9780440225706,
  "The Client": 9780440213529,
  "The Runaway Jury": 9780385472944,
  "The Street Lawyer": 9780440225706,
  "The Testament": 9780440234746,
  "The Brethren": 9780440236672,
  "A Painted House": 9780385721003,
  "Skipping Christmas": 9780385505848,
  "The Summons": 9780385503820,
  "The King of Torts": 9780385508047,
  "The Last Juror": 9780385339686,
  "Bleachers": 9780385511610,
  "Playing for Pizza": 9780345481847,
  "The Appeal": 9780385523200,
  "The Associate": 9780385517834,
  "Ford County": 9780385523583,
  "The Confession": 9780385534138,
  "The Litigators": 9780385535135,
  "Calico Joe": 9780385536071,
  "The Racketeer": 9780385535142,
  "Sycamore Row": 9780385537139,
  "Gray Mountain": 9780385539164,
  "Rogue Lawyer": 9780385539430,
  "The Whistler": 9780385541198,
  "Camino Island": 9780385543055,
  "The Rooster Bar": 9780385541174,
  "The Reckoning": 9780385544151,
  "The Guardians": 9780385544182,
  "A Time for Mercy": 9780385545967,
  "Sooley": 9780385547688,
  "The Hill We Climb": 9780593465271,
  "Where the Crawdads Sing": 9780735219090,
  "American Dirt": 9781250209764,
  "The Silent Patient": 9781250301697,
  "Educated": 9780399590504,
  "The Vanishing Half": 9780525536291,
  "Caste": 9780593230251,
  "Becoming": 9781524763138,
  "The Glass Hotel": 9780735219090,
  "Deacon King Kong": 9780735219090,
  "Such a Fun Age": 9780525541905,
  "The Nickel Boys": 9780385537078,
  "Normal People": 9781984822185,
  "The Water Dancer": 9780399590597,
  "The Testaments": 9780385545596,
  "Daisy Jones & The Six": 9781524798628
};

function getISBN(title) {
    return bookCovers[title] || null;
}

async function getImageUrl(isbn) {
    try {
      const response = await axios.get(`https://covers.openlibrary.org/b/isbn/${isbn}-M.jpg`);
      return response.config.url;
    } catch (error) {
      console.error('Error fetching image:', error);
      return null;
    }
}

const db = new pg.Client({
    user: "postgres",
    host: "localhost",
    database: "book",
    password: "maple",
    port: 5432,
});

db.connect();

app.get("/", async (req, res) => {
    try {
        const result = await db.query("SELECT * FROM posts ORDER BY rating DESC");
        const items = result.rows;
        res.render("index.ejs", {
            listItems: items
        });
      } catch (err) {
        console.log(err);
      }
});

app.get("/create", (req, res) => {
    res.render("create.ejs");
});

app.get("/edit", (req, res) => {
  const id = req.query.editItemId; 
  res.render("edit.ejs", { postId: id });
});

app.post("/modify", async (req, res) => {
  let { username, title, description, rating, id } = req.body;
  console.log(req.body);

  try {
    const result = await db.query("SELECT * FROM posts WHERE id = $1", [id]);
    const item = result.rows[0];
    console.log(item);
  
    if (username == undefined || username == null || username == ''){
      username = item.username;
    }
    
    if (title == undefined || title == null || title == ''){
      title = item.title;
    }

    if (description == undefined || description == null || description == '') {
      description = item.description;
    }

    if (rating == undefined || rating == null || rating == '') {
      rating = item.rating;
    }

    const isbn = getISBN(title);
    const imageURL = await getImageUrl(isbn);
    const updateQuery = `
    UPDATE posts
    SET username = $1, title = $2, description = $3, rating = $4, image = $5
    WHERE id = $6`;
    await db.query(updateQuery, [username, title, description, rating, imageURL, id]);

    res.redirect("/");
  } catch (err) {
    console.error("Error modifying post:", err);
  }
});




app.get("/home", (req, res) => {
  res.redirect("/");
});

app.post("/post-create", async (req, res) => {
    const username = req.body.username;
    const title = req.body.title;
    const description = req.body.description;
    const rating = req.body.rating;
    const isbn = getISBN(title);
    const imageUrl = await getImageUrl(isbn);
  
    try {
      await db.query("INSERT INTO posts (username, title, description, rating, image) VALUES ($1, $2, $3, $4, $5)", [
        username,
        title,
        description,
        rating,
        imageUrl,
      ]);
      res.redirect("/");
    } catch (err) {
      console.log(err);
    }

});

app.post("/delete", async (req, res) => {
    const id = req.body.deleteItemId;
    try {
      await db.query("DELETE FROM posts WHERE id = $1", [id]);
      res.redirect("/");
    } catch (err) {
      console.log(err);
    }
});


app.listen(port, () => {
    console.log(`Server running on port ${port}`)
});
