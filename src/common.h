/* Copyright (c) 2012-2017 LevelDOWN contributors
 * See list at <https://github.com/level/leveldown#contributing>
 * MIT License <https://github.com/level/leveldown/blob/master/LICENSE.md>
 */

#ifndef LD_COMMON_H
#define LD_COMMON_H

#include <nan.h>

namespace leveldown {

NAN_INLINE bool BooleanOptionValue(v8::Local<v8::Object> options,
                                   const char* _key,
                                   bool def = false) {
  Nan::HandleScope scope;
  v8::Local<v8::String> key = Nan::New(_key).ToLocalChecked();
  return !options.IsEmpty()
    && options->Has(Nan::GetCurrentContext(), key).ToChecked()
    ? options->Get(Nan::GetCurrentContext(), key).ToLocalChecked()->BooleanValue(v8::Isolate::GetCurrent())
    : def;
}

NAN_INLINE uint32_t UInt32OptionValue(v8::Local<v8::Object> options,
                                      const char* _key,
                                      uint32_t def) {
  Nan::HandleScope scope;
  v8::Local<v8::String> key = Nan::New(_key).ToLocalChecked();
  return !options.IsEmpty()
    && options->Has(Nan::GetCurrentContext(), key).ToChecked()
    && options->Get(Nan::GetCurrentContext(), key).ToLocalChecked()->IsNumber()
    ? options->Get(Nan::GetCurrentContext(), key).ToLocalChecked()->Uint32Value(Nan::GetCurrentContext()).ToChecked()
    : def;
}

NAN_INLINE uint64_t UInt64OptionValue(v8::Local<v8::Object> options,
                                      const char* _key,
                                      uint64_t def) {
  Nan::HandleScope scope;
  v8::Local<v8::String> key = Nan::New(_key).ToLocalChecked();
  return !options.IsEmpty()
    && options->Has(Nan::GetCurrentContext(), key).ToChecked()
    && options->Get(Nan::GetCurrentContext(), key).ToLocalChecked()->IsNumber()
    ? options->Get(Nan::GetCurrentContext(), key).ToLocalChecked()->IntegerValue(Nan::GetCurrentContext()).ToChecked()
    : def;
}

} // namespace leveldown

#endif
