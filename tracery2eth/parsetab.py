
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LBRACKET RBRACKET HASH COLON PERIOD LITERALrule :rule : literal rule\n            | apply rule\n            | generate ruleliteral : LITERALapply : HASH LITERAL HASHapply : HASH LITERAL PERIOD modifiers HASHmodifiers : LITERALmodifiers : LITERAL PERIOD modifiersgenerate : LBRACKET LITERAL COLON rule RBRACKET'
    
_lr_action_items = {'HASH':([0,2,5,6,7,8,13,15,16,17,20,21,22,],[1,1,-5,1,1,13,-6,1,-8,20,-7,-10,-9,]),'PERIOD':([8,16,],[14,19,]),'LBRACKET':([0,2,5,6,7,13,15,20,21,],[4,4,-5,4,4,-6,4,-7,-10,]),'LITERAL':([0,1,2,4,5,6,7,13,14,15,19,20,21,],[5,8,5,10,-5,5,5,-6,16,5,16,-7,-10,]),'COLON':([10,],[15,]),'RBRACKET':([2,5,6,7,9,11,12,13,15,18,20,21,],[-1,-5,-1,-1,-2,-3,-4,-6,-1,21,-7,-10,]),'$end':([0,2,3,5,6,7,9,11,12,13,20,21,],[-1,-1,0,-5,-1,-1,-2,-3,-4,-6,-7,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'apply':([0,2,6,7,15,],[6,6,6,6,6,]),'literal':([0,2,6,7,15,],[2,2,2,2,2,]),'modifiers':([14,19,],[17,22,]),'generate':([0,2,6,7,15,],[7,7,7,7,7,]),'rule':([0,2,6,7,15,],[3,9,11,12,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> rule","S'",1,None,None,None),
  ('rule -> <empty>','rule',0,'p_emptyrule','tracery.py',84),
  ('rule -> literal rule','rule',2,'p_rule','tracery.py',88),
  ('rule -> apply rule','rule',2,'p_rule','tracery.py',89),
  ('rule -> generate rule','rule',2,'p_rule','tracery.py',90),
  ('literal -> LITERAL','literal',1,'p_literal','tracery.py',94),
  ('apply -> HASH LITERAL HASH','apply',3,'p_apply_unmodified','tracery.py',98),
  ('apply -> HASH LITERAL PERIOD modifiers HASH','apply',5,'p_apply_modified','tracery.py',102),
  ('modifiers -> LITERAL','modifiers',1,'p_modifier','tracery.py',107),
  ('modifiers -> LITERAL PERIOD modifiers','modifiers',3,'p_multiple_modifier','tracery.py',111),
  ('generate -> LBRACKET LITERAL COLON rule RBRACKET','generate',5,'p_generate','tracery.py',121),
]