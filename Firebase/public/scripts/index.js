const loginElement = document.querySelector('#login-form');
const contentElement = document.querySelector("#content-sign-in");
const userDetailsElement = document.querySelector('#user-details');
const authBarElement = document.querySelector("#authentication-bar");

// Elements for sensor readings
const tempElement = document.getElementById("TEMP");
const humElement = document.getElementById("HUM");
const co2Element = document.getElementById("CO2");
const gasesToxicosElement = document.getElementById("gases-toxicos");

// MANAGE LOGIN/LOGOUT UI
const setupUI = (user) => {
  if (user) {
    //toggle UI elements
    loginElement.style.display = 'none';
    contentElement.style.display = 'block';
    authBarElement.style.display ='block';
    userDetailsElement.style.display ='block';
    userDetailsElement.innerHTML = user.email;

    // get user UID to get data from database
    var uid = user.uid;
    console.log(uid);

    // Database paths (with user UID)
    var dbPathTemp = 'UsersData/' + uid.toString() + '/temperatura';
    var dbPathHum = 'UsersData/' + uid.toString() + '/humedad';
    var dbPathCo2 = 'UsersData/' + uid.toString() + '/concentracion';
    var dbPathGasesToxicos = 'UsersData/' + uid.toString() + '/gas';  // Nueva ruta para gases tóxicos

    // Database references
    var dbRefTemp = firebase.database().ref().child(dbPathTemp);
    var dbRefHum = firebase.database().ref().child(dbPathHum);
    var dbRefCo2 = firebase.database().ref().child(dbPathCo2);
    var dbRefGasesToxicos = firebase.database().ref().child(dbPathGasesToxicos);  // Nuevo ref para gases tóxicos

    // Update page with new readings
    dbRefTemp.on('value', snap => {
      tempElement.innerText = snap.val().toFixed(2);
    });

    dbRefHum.on('value', snap => {
      humElement.innerText = snap.val().toFixed(2);
    });

    dbRefCo2.on('value', snap => {
      co2Element.innerText = snap.val().toFixed(2);
    });

    dbRefGasesToxicos.on('value', snap => {
      gasesToxicosElement.innerText = snap.val().toFixed(2);
    });

  // if user is logged out
  } else{
    // toggle UI elements
    loginElement.style.display = 'block';
    authBarElement.style.display ='none';
    userDetailsElement.style.display ='none';
    contentElement.style.display = 'none';
  }
}
