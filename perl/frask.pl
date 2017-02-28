#!/usr/bin/env perl

# rendent Perl moins permissif
use strict;
use warnings;

open(my $fh, "<", $ARGV[0]) or die("open: $!"); # ouvre le fichier source
open(my $fh2, ">", $ARGV[1]) or die("open: $!"); # ouvre le fichier à écrire
while( defined(my $l = <$fh> ) ) { # lit le fichier source ligne par ligne
    $l =~ s/Booléen/Bool/g;
    $l =~ s/Faux/False/g;
    $l =~ s/Vrai/True/g;
    $l =~ s/et/&&/g;
    $l =~ s/ou/or/g;
    $l =~ s/non/not/g;
    $l =~ s/autrement/otherwise/g;
    $l =~ s/Peut être/Maybe/g;
    $l =~ s/Rien/Nothing/g;
    $l =~ s/Juste/Just/g;
    $l =~ s/peut être/maybe/g;
    $l =~ s/Soit/Either/g;
    $l =~ s/D'abord/Right/g;
    $l =~ s/Ensuite/Left/g;

    print $fh2 $l; # écrit $l après l'avoir modifié
}
close($fh); # ferme le fichier source
close($fh2); # ferme le fichier créé
