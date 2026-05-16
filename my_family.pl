% my_family.pl — Emilio's custom family tree

:- discontiguous male/1.
:- discontiguous female/1.

% --- GENERATION 1 (Grandparents) ---
male(coddy).     
male(jose).      
female(cynthia).
female(diana).

% --- GENERATION 2 (Parents + Siblings) ---
male(brian).     
male(caleb).     
female(joan).
female(abigael).

% --- GENERATION 3 (Children) ---
male(emilio).    
male(ian).       
female(sofi).
female(brenda).

% --- parent/2 facts ---
parent(coddy, brian).
parent(coddy, joan).
parent(cynthia, brian).
parent(cynthia, joan).

parent(jose, caleb).
parent(jose, abigael).
parent(diana, caleb).
parent(diana, abigael).

parent(brian, emilio).
parent(brian, sofi).
parent(joan, emilio).
parent(joan, sofi).

parent(caleb, ian).
parent(abigael, brenda).

% --- RULES ---
father(X, Y)      :- parent(X, Y), male(X).
mother(X, Y)      :- parent(X, Y), female(X).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
grandfather(X, Z) :- grandparent(X, Z), male(X).
grandmother(X, Z) :- grandparent(X, Z), female(X).
grandchild(X, Z)  :- grandparent(Z, X).

sibling(X, Y)     :- parent(P, X), parent(P, Y), X \= Y.
brother(X, Y)     :- sibling(X, Y), male(X).
sister(X, Y)      :- sibling(X, Y), female(X).

uncle(X, Y)       :- parent(P, Y), brother(X, P).
aunt(X, Y)        :- parent(P, Y), sister(X, P).

cousin(X, Y)      :-
    parent(PX, X),
    parent(PY, Y),
    sibling(PX, PY).