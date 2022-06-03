# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto\x12\x04todo\"$\n\x08TodoItem\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\"*\n\tTodoItems\x12\x1d\n\x05items\x18\x01 \x03(\x0b\x32\x0e.todo.TodoItem\"%\n\x0bTodoRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x42\x05\n\x03_id2e\n\x04Todo\x12,\n\ncreateTodo\x12\x0e.todo.TodoItem\x1a\x0e.todo.TodoItem\x12/\n\treadTodos\x12\x11.todo.TodoRequest\x1a\x0f.todo.TodoItemsb\x06proto3')



_TODOITEM = DESCRIPTOR.message_types_by_name['TodoItem']
_TODOITEMS = DESCRIPTOR.message_types_by_name['TodoItems']
_TODOREQUEST = DESCRIPTOR.message_types_by_name['TodoRequest']
TodoItem = _reflection.GeneratedProtocolMessageType('TodoItem', (_message.Message,), {
  'DESCRIPTOR' : _TODOITEM,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.TodoItem)
  })
_sym_db.RegisterMessage(TodoItem)

TodoItems = _reflection.GeneratedProtocolMessageType('TodoItems', (_message.Message,), {
  'DESCRIPTOR' : _TODOITEMS,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.TodoItems)
  })
_sym_db.RegisterMessage(TodoItems)

TodoRequest = _reflection.GeneratedProtocolMessageType('TodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _TODOREQUEST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.TodoRequest)
  })
_sym_db.RegisterMessage(TodoRequest)

_TODO = DESCRIPTOR.services_by_name['Todo']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TODOITEM._serialized_start=20
  _TODOITEM._serialized_end=56
  _TODOITEMS._serialized_start=58
  _TODOITEMS._serialized_end=100
  _TODOREQUEST._serialized_start=102
  _TODOREQUEST._serialized_end=139
  _TODO._serialized_start=141
  _TODO._serialized_end=242
# @@protoc_insertion_point(module_scope)
