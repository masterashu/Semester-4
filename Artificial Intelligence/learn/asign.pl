% Species Name
% species_name(common_name, species).
    species_name('african wild dog', 'lycaon pictus').
    species_name('common fox', 'vulpes vulpes').
    species_name('arctic fox', 'vulpes lagopus').
    species_name('fennec fox', 'vulpes zerda').
    species_name('red wolf', 'canis rufus').
    species_name('coyote', 'canis latrans').
    species_name(X, Y) :-
        sub_species_name(X, Z),
        sub_species(Z, Y).

% sub_species(species, sub-species)
    sub_species('canis lupus', 'canis lupus').
    sub_species('canis lupus familiaris', 'canis lupus').

% sub-species_name
    sub_species_name('gray wolf', 'canis lupus').
    sub_species_name('dog', 'canis lupus familiaris').


% Species Genus
% species_genus(species, genus).
    species_genus('lycaon pictus', 'lycaon').
    species_genus('vulpes vulpes', 'vulpes').
    species_genus('vulpes lagopus', 'vulpes').
    species_genus('vulpes zerda', 'vulpes').
    species_genus('canis rufus', 'canis').
    species_genus('canis latrans', 'canis').
    species_genus('canis lupus', 'canis').
    species_genus('canis lupus familiaris', 'canis').

% Genus Family
% genus_family(genus, family).
    genus_family('lycaon', 'canidae').
    genus_family('vulpes', 'canidae').
    genus_family('canis', 'canidae').


% Common Genus
common_genus(X, Y) :-
    species_name(X, A),
    species_genus(A, Z),
    species_name(Y, B),
    species_genus(B, Z),
    \=(X, Y),
    format('~w is of the same genus (~w) as ~w', [X, Z, Y]).


% Common Species
common_species(X, Y) :- 
    species_name(X, Z), 
    species_name(Y, Z),
    format('~w is of the same species as ~w', [X, Y]).


% Relation path
relation_path(X, Y, List) :-
    species_name(X, Z),
    species_name(Y, Z),
    \=(X, Y),
    =(List, [X, Z, Y]),
    format('~w <-> ~w <-> ~w', List).


relation_path(X, Y, List) :-
    species_name(X, A),
    species_genus(A, Z),
    species_name(Y, B),
    species_genus(B, Z),
    \=(X, Y),
    =(List, [X, A, Z, B, Y]),
    format('~w <-> ~w <-> ~w <-> ~w <-> ~w', List).

relation_path(X, Y, List) :-
    species_name(X, A),
    species_genus(A, C),
    genus_family(C, Z),
    species_name(Y, B),
    species_genus(B, D),
    genus_family(D, Z),
    \=(X, Y),
    =(List, [X, A, C, Z, D, B, Y]),
    format('~w <-> ~w <-> ~w <-> ~w <-> ~w <-> ~w <-> ~w', List).

