%kingdom(название, запрет на проживание)
kingdom(wraemor, _, francisc).
kingdom(bortodir,elf, _).
kingdom(thelamel,dwarf, _).

person(karl,21,elf,wraemor,hunter).
person(mary,16,human,wraemor,peasant).
person(francisc,43,human,wraemor,king).

proffesion(X,Y) :-
    person(X,_,_,_,Y).
age(X,Y) :-
    person(X,Y,_,_,_).
where(X, Y) :-
    person(X,_,_,Y,_).
race(X, Y) :-
    person(X,_,Y,_,_).

is_king(X) :-
    person(X,_,_,_,Y), Y = king.
do_live(X, D) :-
    person(X,_,_,Z,_), Z = D.

can_move(X, D) :-
    person(X,_,R,_,Y), Y \= king, \+ do_live(X, D), kingdom(D, L, _), R \= L.