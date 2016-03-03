#!/usr/bin/perl

use strict;
use warnings;
use feature 'say';

use Net::Ping;

my $msg = 'pingadingaling';
my $p = Net::Ping->new("udp");
$p->hires();
$p->port_number(12000);

my ($alive, $rtt, $adr) = $p->ping('localhost', 1.0);

printf("Host $adr is up; RTT: %.2f ms\n",1000*$rtt) if $alive;
$p->close();
