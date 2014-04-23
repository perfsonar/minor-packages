#!/usr/bin/perl 

use strict;
use warnings;

use FindBin qw($RealBin);

my $template_path = $RealBin."/cacti_graph_template_ntp_quality_query-ntpd_pl.xml";

# Verify that the template exists
unless ( -f $template_path) {
    die("Can't find template to import");
}

# Import the template
system("/usr/bin/php", "/usr/share/cacti/cli/import_template.php", "--with-template-rras", "--filename=$template_path");
if ($? != 0) {
    die("Problem importing template");
}

my $template_id;
open(TEMPLATES, "/usr/bin/php /usr/share/cacti/cli/add_graphs.php --list-graph-templates |") or die("Couldn't list graph templates");
while(<TEMPLATES>) {
    if (/(\d+)\s+(.*)/) {
        my $curr_id   = $1;
        my $curr_name = $2;

        if ($curr_name =~ /NTP Quality/) {
            print "Template: $curr_name = $curr_id\n";
            $template_id = $curr_id;
        }
    }
}
close(TEMPLATES);

unless ($template_id) {
    die("Couldn't find newly added template");
}


# XXX: lookup 'localhost'
system("/usr/bin/php", "/usr/share/cacti/cli/add_graphs.php", "--graph-type=cg", "--graph-template-id=$template_id", "--host-id=1");
if ($? != 0) {
    die("Problem adding graph for localhost");
}
