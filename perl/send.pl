#!/usr/bin/perl

use Net::SMTP;
use strict;
use warnings;

        # demande l'hôte (smtp.xxxx.xxx)
        print "Smtp host : ";
        my $MailHost = <>;
        chomp $MailHost;
    
        # demande l'expéditeur
        print "From : ";
        my $MailFrom = <>;
        chomp $MailFrom;
    
        # demande le récepteur
        print "To : ";
        my $MailTo = <>;
        chomp $MailTo;
        
        # demande le sujet
        print "Subject : ";
        my $subject = <>;
        chomp $subject;
        
        # demande le corps du message
        my $MailBody = "";
        my $ligne = "";
        print "Body : ";
        while($ligne ne ".\n") {
            print "> ";
            $ligne = <>;
            $MailBody = $MailBody . $ligne;
        }
        
        #Étape 1
        my $smtp = Net::SMTP->new($MailHost, Debug => 1, Timeout => 10) or die 'Impossible de se connecter au serveur : ' . $!;
        
        #Étape 2
        $smtp->mail($MailFrom) or die 'Un problème est survenu avec la méthode mail() !';
        
        #Étape 3
        $smtp->to($MailTo) or die 'Un problème est survenu avec la méthode to() !';
        
        #$smtp->cc('*****@hotmail.fr') or die 'Un problème est survenu avec la méthode cc() !';
        #$smtp->bcc('*****@hotmail.fr') or die 'Un problème est survenu avec la méthode bcc() !';
        
        #Étape 4
        $smtp->data() or die 'Un problème est survenu avec la méthode data() !';
        $smtp->datasend("To: $MailTo\n") or die 'Un problème est survenu avec la méthode datasend() !';
        $smtp->datasend("From: $MailFrom\n") or die 'Un problème est survenu avec la méthode datasend() !';
        $smtp->datasend("Subject: $subject\n") or die 'Un problème est survenu avec la méthode datasend() !';
        $smtp->datasend("\n")  or die 'Un problème est survenu avec la méthode datasend() !';
        $smtp->datasend("$MailBody") or die 'Un problème est survenu avec la méthode datasend() !';
        $smtp->dataend() or die 'Un problème est survenu avec la méthode dataend() !';
        
        #Étape 5
        $smtp->quit() or die 'Un problème est survenu avec la méthode quit() !';