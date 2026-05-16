% family_try.pl — Basic Prolog family example

% --- Facts: parent(Parent, Child) ---
parent(emilio, lewis).
parent(emilio, lyn).
parent(emmanuel, ann).
parent(emmanuel, sakwa).

% --- Facts: male / female ---
male(emilio).
male(emmanuel).
male(lewis).
male(sakwa).
female(lyn).
female(ann).

% --- Rules ---
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.