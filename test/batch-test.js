const test       = require('tape')
    , leveldown  = require('..')
    , abstract   = require('abstract-leveldown/abstract/batch-test')
    , make       = require('./make')

abstract.all(leveldown, test)

make('test batch(): closing db with pending batch', function (db, t, done) {
    var hasBatch = false;
    const opts = [{ type: 'put', key: 'key1', value: 'value' }];
    db.batch(opts, err => {
        t.error(err, 'no error from batch()');
        hasBatch = true;
    });
    db.close(err => {
        t.error(err, 'no error from close()');
        t.same(hasBatch, true, 'batch done');
        done();
    });
});
