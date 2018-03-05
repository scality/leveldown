const test       = require('tape')
    , leveldown  = require('..')
    , abstract   = require('abstract-leveldown/abstract/del-test')
    , make       = require('./make')

abstract.all(leveldown, test)

make('test del(): closing db with pending del', function (db, t, done) {
    var hasDel = false;
    db.put('key1', 'value', err => {
        t.error(err, 'no error from put()');
        db.del('key1', err => {
            t.error(err, 'no error from del()');
            hasDel = true;
        });
        db.close(err => {
            t.error(err, 'no error from close()');
            t.same(hasDel, true, 'del done');
            done();
        });
    });
});
