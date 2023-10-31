%kingdom(название, запрет на проживание)
kingdom(wraemor, _, francisc).
kingdom(bortodir,elf, stromrat).
kingdom(thelamel,dwarf, elidir).

person(karl,21,human,wraemor,hunter).
person(mary,16,human,wraemor,peasant).
person(francisc,43,human,wraemor,king).
person(oku,32,human,wraemor,knight).
person(gerald,93,human,wraemor,peasant).
person(mummout,156,dwarf,wraemor,hunter).
person(nuovis,216,elf,wraemor,knight).
person(mitalar,145,elf,thelamel,knight).
person(elidir,98,elf,thelamel,king).
person(falael,118,elf,thelamel,hunter).
person(tanelia,195,elf,thelamel,knight).
person(aila,86,elf,thelamel,peasant).
person(frederika,43,human,thelamel,peasant).
person(katar,143,elf,thelamel,knight).
person(stromrat,132,dwarf,bortodir,king).
person(yordrat,96,dwarf,bortodir,knight).
person(forsubelle,56,dwarf,bortodir,peasant).
person(nagnaeda,43,dwarf,bortodir,hunter).
person(henry,58,human,bortodir,hunter).
person(hoummoud,100,dwarf,knight).
person(sakrac,78,dwarf,peasant).


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
against_law(X, K) :-
    person(X, _, R,_,_), kingdom(K,L,_), R = L.

can_move(X, D) :-
    person(X,_,R,_,Y), Y \= king, \+ do_live(X, D), kingdom(D, L, _), R \= L.