var toto = require('./leveldown.js');
var db = new toto('./AHAHHAH');
db.open(err => {
    if (err) {
        console.log('open: ', err);
    } else {
        db.put('test', 'titi', err => {
            if ('put: ', err) {
                console.log(err);
            } else {
                db.get('test', (err, data) => {
                    if (err) {
                        console.log('get: ', err);
                    } else {
                        console.log(data.toString());
                    }
                });
            }
        });
    }
});
