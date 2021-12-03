function findSolution(inputData) {
	let lampsNumber = inputData.split(" ")[0];
	let firstLamp = inputData.split(" ")[1];

	let bad = 0;
	let good = firstLamp*lampsNumber;
	let m = (good + bad)/2;

	while (good - bad > 0.005) {
		if (isGoodEnough(firstLamp, lampsNumber, m)) {
			good = m;
		}
		else {
			bad = m;
		}
		m = (good + bad)/2;
	}
	console.log(m);
}

function isGoodEnough(firstLamp, lampsNumber, candidate) {
	let lamps = [firstLamp, candidate];
	for(let i = 2; i <= lampsNumber; i++){
	    if (lamps[i] < 0) {
	    	return false;
    	}
	    lamps[i + 1] = 2*lamps[i] + 2 - lamps[i - 1];
	}
	return true;
}

findSolution("8 15");