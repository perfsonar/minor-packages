#!/usr/bin/perl -w
# Query ISCs ntp deamon
# Requires perl 5.x, ntpq and ntpd 4.2.6 or higher
# Version 2011071401
# Tijn Lambrechtsen <tijn.lambrechtsen@m4n.nl>
#
# Version 2009051102
# Helmut Schneider <jumper99@gmx.de>
#
# Version 2009051201
# Helmut Schneider <jumper99@gmx.de>
# Fixed reporting refid if unknown

use strict;

my $host=$ARGV[0]; 
$host="localhost" unless ( $host );
shift;

my %stats = ();
my @params=("offset", "frequency", "sys_jitter", "clk_jitter", "clk_wander", "refid", "rootdisp", "stratum", "reftype");

foreach (@params) {
	$stats{$_}="U";
}

open(NTP, "/usr/sbin/ntpq -c \"host $host\" -c rv -c peers |") || die "Cannot connect to host $host: $!";

while (<NTP>) {
	if ( m/frequency=([-]?\d+.\d+)/ ) { $stats{frequency}=$1; }
	if ( m/sys_jitter=([-]?\d+.\d+)/ ) { $stats{sys_jitter}=$1; }
	if ( m/clk_jitter=([-]?\d+.\d+)/ ) { $stats{clk_jitter}=$1; }
	if ( m/offset=([-]?\d+.\d+)/ ) { $stats{offset}=$1; }
	if ( m/clk_wander=([-]?\d+.\d+)/ ) { $stats{clk_wander}=$1; }
	if ( m/rootdisp=([\d\.]*)/ ) { $stats{rootdisp}=$1; }
	if ( m/stratum=([\d\.]*)/ ) { $stats{stratum}=$1; }
	if ( m/refid=([\d+\w+\.\(\)]+)/ ) { $stats{refid}=$1; }
	if ( $stats{refid} ne "U" ) {
		if ( $stats{refid}=~/LOCAL/ ) { $stats{reftype}=1; }
		elsif ( $stats{refid}=~/DCFa/ ) { $stats{reftype}=2; }
		elsif ( $stats{refid}=~/GPS/ ) { $stats{reftype}=3; }
		elsif ( $stats{refid}=~/PPS/ ) { $stats{reftype}=4; }
		elsif ( $stats{refid}=~/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/ ) { $stats{reftype}=5; }
		else { $stats{reftype}=6; }
	} else { $stats{reftype}=0; }
}
close(NTP);

print "frequency:" . $stats{frequency} .  " offset:" . $stats{offset} . " sys_jitter:" . $stats{sys_jitter} . " clk_wander:" . $stats{clk_wander} . " clk_jitter:" . $stats{clk_jitter} . " stratum:" . $stats{stratum} . " rootdisp:" . $stats{rootdisp} . " refid:" . $stats{refid} . " reftype:" . $stats{reftype};

