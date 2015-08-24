<?php

include __DIR__ . '/clicolors.php';
$colors = new Colors();


$db  = new PDO("pgsql:host=localhost;port=5432;dbname=dragonnet;user=moodle;password=helloworld");
var_dump($db);

$filename = '/Users/Anthony/Desktop/Library Exports/Secondary All.csv';

$file = file_get_contents($filename);
$lines = explode("\n", $file);

$outputFilename = '/Users/Anthony/Desktop/Library Exports/Secondary All Wrong.csv';
$outputFile = fopen($outputFilename, "w+");

foreach ($lines as $lineNumber => $line) {

	$fields = explode(',', $line);
	foreach ($fields as &$field) {
		$field = trim($field, '"');
	}

	if (stripos($fields[9], 'Student') === false) {
		continue;
	}

	if (substr($fields[0], 0, 2) !== 'P ') {
		$str = "\nInvalid barcode format: Line " . $lineNumber . " '" . $fields[0]. "'";

		fwrite($outputFile, "\n". $line);

		echo $colors->getColoredString($str, 'red');
		continue;
	}

	$idnumber = substr($fields[0], 2);
	$q = $db->prepare('SELECT * FROM ssismdl_user WHERE idnumber = ?');
	$q->execute(array($idnumber));
	if ($user = $q->fetch(PDO::FETCH_OBJ)) {

		$str = "\nBarcode {$fields[0]} matches DragonNet user " . $user->username;
		echo $colors->getColoredString($str, 'green');

	} else {
		$str = "\nUser not found on DragonNet: Line " . $lineNumber . " " . $fields[0];

		fwrite($outputFile, "\n". $line);

		echo $colors->getColoredString($str, 'purple');
	}



	/*if ($fields[0][0] == 'P' && (stripos($fields[9], 'Student') === false) && $fields[9] != 'Parent') {
		echo "\n" . $line;
	}*/

}
