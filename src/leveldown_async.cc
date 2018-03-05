/* Copyright (c) 2012-2018 LevelDOWN contributors
 * See list at <https://github.com/level/leveldown#contributing>
 * MIT License <https://github.com/level/leveldown/blob/master/LICENSE.md>
 */

#include <leveldb/db.h>

#include "leveldown.h"
#include "leveldown_async.h"

namespace leveldown {

/** DESTROY WORKER **/

DestroyWorker::DestroyWorker(Nan::Utf8String* location,
                             Nan::Callback *callback,
                             leveldb::Env *env)
  : AsyncWorker(NULL, callback, "leveldown:destroy"), location(location)
{
    this->options = new leveldb::Options();
    this->options->env = env;
}

DestroyWorker::~DestroyWorker() {
  delete location;
}

void DestroyWorker::Execute() {
  leveldb::Options options;
  SetStatus(leveldb::DestroyDB(**location, *(this->options)));
}

/** REPAIR WORKER **/

RepairWorker::RepairWorker(Nan::Utf8String* location, Nan::Callback *callback)
  : AsyncWorker(NULL, callback, "leveldown:repair"), location(location)
{}

RepairWorker::~RepairWorker() {
  delete location;
}

void RepairWorker::Execute() {
  leveldb::Options options;
  SetStatus(leveldb::RepairDB(**location, options));
}

} // namespace leveldown
