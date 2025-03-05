const mysql = require('mysql2');
const db = mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"Lusinga@2003",
    database:"Student"
});

db.connect((error) => {
    if (error) {
        console.error('Error connecting to MySQL', error.message);
        return;
    }
    HTMLFormControlsCollection.log('Connected to MySQL!')
});

module.exports = db;