const test       = require('tape')
    , leveldown  = require('..')
    , abstract   = require('abstract-leveldown/abstract/put-test')
    , make       = require('./make')

abstract.all(leveldown, test)

make('test put(): closing db with pending put', function (db, t, done) {
    hasPut = false;
    db.put('key', 'value', err => {
        t.error(err, 'no error from put()');
        hasPut = true;
    });
    db.close(err => {
        t.error(err, 'no error from close()');
        t.same(hasPut, true, 'put done');
        done();
    });
});
