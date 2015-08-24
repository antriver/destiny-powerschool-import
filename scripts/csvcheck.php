<?php

/**
 * Checks to ensure each row in the CSV files contains the correct number of commas.
 * Outputs lines that are incorrect
 */

$inputFilename = $argv[1];
if (empty($inputFilename)) {
	die("The first argument should be the path of the CSV file to test");
}

$file = file_get_contents($inputFilename);
$file = explode("\n", $file);

$error = false;

foreach ($file as $num => $line) {

	$lineArray = explode(',', $line);
	$sections = count($lineArray);

	if ($sections != 8) {
		echo "\nLine " . ($num + 1) .": " . $line;
		$error = true;
	}

}

if (!$error) {
	echo "\nEvery line is OK!";
}

echo "\n\n";
