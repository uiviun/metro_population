#!/usr/bin/perl

open CA,"./metro_station_estate_distance_cal.txt";
$line1 = <CA>;
chomp($line1);
@array1 = split /\s+/,$line1;

while($line1 = <CA>)
{
	chomp($line1);
	@array2 = split /\s+/,$line1,3;
	@array3 = split /\s+/,$array2[2];
	my $min = $array3[0];
	$min=10000000;
	foreach $i (keys @array3)
	{
		if ($array3[$i] < $min)
		{
			$min = $array3[$i];
			$sta=$array1[$i+2];
		}
		
	}
	print $array2[0]."\t".$array2[1]."\t".$min."\t".$sta."\n";
}
close CA;