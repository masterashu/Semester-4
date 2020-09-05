% AI Assignment 3
%       - by Ashutosh Chauhan
% Species Name
% species_name(Symbol, species).
species_name('african wild dog', 'lycaon pictus').
species_name('common fox', 'vulpes vulpes').
species_name('arctic fox', 'vulpes lagopus').
species_name('fennec fox', 'vulpes zerda').
species_name('red wolf', 'canis rufus').
species_name('coyote', 'canis latrans').
species_name(X, Y) :- 
    sub_species(X, Z), 
    species_sub_species(Z, Y).

% Sub-Species Species
% sub_species(Symbol, sub-species).
sub_species('dog', 'canis lupus familiaris').
sub_species('gray wolf', 'canis lupus').

species_sub_species('canis lupus familiaris', 'canis lupus').
species_sub_species('canis lupus', 'canis lupus').

% Species Genus
% species_genus(species, genus).
species_genus('lycaon pictus', 'lycaon').
species_genus('vulpes vulpes', 'vulpes').
species_genus('vulpes lagopus', 'vulpes').
species_genus('vulpes zerda', 'vulpes').
species_genus('canis rufus', 'canis').
species_genus('canis latrans', 'canis').
species_genus('canis lupus', 'canis').

% Genus Family
% genus_family(family, genus).
genus_family('lycaon', 'canidae').
genus_family('vulpes', 'canidae').
genus_family('canis', 'canidae').

% Common Genus
    % check common name
    common_genus(X, Y) :-
        species_genus(A, Z), 
        species_name(X, A), 
        species_genus(B, Z), 
        species_name(Y, B),
        \=(Y, X),
        format('~s "~w" <-> "~w" <-> "~w" <-> "~w" <-> "~w".', ['Relation Path:', X, A, Z, B, Y]).

% Common Species
    % check common name
    common_species(X, Y) :- 
        species_name(X, Z), 
        species_name(Y, Z),
        \=(X, Y),
        format('"~w" ~s "~w" ~s "~w".', [X, 'belongs to the same species', Z,  'as', Y]).

% Relation Path
    % Get relation path for same species:
    relation_path(X, Y, L) :-
        species_name(X, Z), 
        species_name(Y, Z),
        \=(Y, X),
        =(L, [ X, Z, Y]),
        format('~s "~w" <-> "~w" <-> "~w".', ['Relation Path:', X, Z, Y]).

    % Get relation path for same genus:
    relation_path(X, Y, L) :-
        species_genus(A, Z), 
        species_name(X, A), 
        species_genus(B, Z), 
        species_name(Y, B),
        \=(Y, X),
        =(L, [X, A, Z, B, Y]),
        format('~s "~w" <-> "~w" <-> "~w" <-> "~w" <-> "~w".', ['Relation Path:', X, A, Z, B, Y]).

    % Get relation path for same family:
    relation_path(X, Y, L) :-
        genus_family(C, Z),
        species_genus(A, C), 
        species_name(X, A),
        genus_family(D, Z), 
        species_genus(B, D), 
        species_name(Y, B),
        \=(Y, X),
        =(L, [X, A, C, Z, D, B, Y]),
        format('~s "~w" <-> "~w" <-> "~w" <-> "~w" <-> "~w" <-> "~w" <-> "~w".', ['Relation Path:', X, A, C, Z, D, B, Y]).