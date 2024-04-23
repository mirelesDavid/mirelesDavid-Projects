import express from "express";
import bodyParser from "body-parser";

const app = express();
const port = 3000;
app.use(express.static("./public"));
app.use(bodyParser.urlencoded({ extended: true }));

let posts = [];

app.get("/", (req, res) => {
    res.render("index.ejs", { posts: posts });
  });

app.get("/create", (req, res) => {
res.render("create.ejs");
});

app.get("/edit", (req, res) => {
    res.render("edit.ejs");
});

app.post("/post-create", (req, res) => {
    const username = req.body.username;
    const title = req.body.title;
    const description = req.body.description;
    const image = req.body.image;

    const newPost = {
        username: username,
        title: title,
        description: description,
        image: image
    };

    posts.push(newPost);
    res.redirect("/");
});

app.post("/edit-post", (req, res) => {
    const username = req.body.username;
    const title = req.body.title;
    const post = posts.find(post => post.username === username && post.title === title);

    if (post) {
        res.render("edit-post.ejs", { post: post });
    } else {
        res.render("edit.ejs");
    }
});


app.post("/modify", (req, res) => {
    const action = req.body.action;
    const oldUsername = req.body.oldUsername;
    const oldTitle = req.body.oldTitle;
    const postIndex = posts.findIndex(post => post.username === oldUsername && post.title === oldTitle);

    if (action === "modify"){
        const newUsername = req.body.username;
        const newTitle = req.body.title;
        const newDescription = req.body.description;
        const newImage = req.body.image;

        posts[postIndex].username = newUsername;
        posts[postIndex].title = newTitle;
        posts[postIndex].description = newDescription;
        posts[postIndex].image = newImage;

    } else if (action === "delete"){
        posts.splice(postIndex, 1);
    }

    res.redirect("/");
});

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
  });

/*

Título: "Into the Wilderness"
Descripción: "Embark on a visual journey through untamed landscapes and rugged terrains. Witness the raw beauty of untouched nature through my lens, where every frame tells a story of adventure and discovery."
Nombre de usuario: "WildExplorer"

Título: "The Art of Macro"
Descripción: "Delve into the miniature world of macro photography, where tiny subjects become larger-than-life masterpieces. Explore the intricate details and hidden wonders that unfold beneath the lens."
Nombre de usuario: "MacroMaestro"

Título: "Infinite Horizons"
Descripción: "Chase the horizon and capture the boundless expanse of the world around us. From endless seas to rolling hills, let's embrace the vastness of our planet through the art of landscape photography."
Nombre de usuario: "HorizonHunter"

Título: "Soulful Portraits"
Descripción: "Peel back the layers of the human spirit and reveal its essence through captivating portraits. Each frame captures the depth of emotion and unique beauty found within every individual."
Nombre de usuario: "SoulfulLens"

https://i.pinimg.com/originals/ec/1f/a8/ec1fa82d3bc48935499dbcd167358b9f.jpg

    https://bst.icons8.com/wp-content/themes/icons8/app/uploads/2017/08/black-and-white-fog.jpg

https://upload.wikimedia.org/wikipedia/commons/6/67/Top_view_of_a_white_flower_in_black-and-white_%28Unsplash%29.jpg

https://bwvision.com/wp-content/uploads/2018/07/NYC-Aerial-view-min.jpg

*/
