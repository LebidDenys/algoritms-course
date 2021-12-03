function processData(input) {
    const res = [];
    const data = input.split("\n");
    const clientsArr = data[1].split(" ");
    const halfLen = Math.round(clientsArr.length/2);
    const multiArr = [
        clientsArr.slice(0, halfLen),
        clientsArr.slice(halfLen)];
    const sumsArr = multiArr.map(item => item.reduce((acc, cur) => parseInt(acc) + parseInt(cur), 0));
    for(let i = 3; i < 3+parseInt(data[2]); i++) {
        const comand = data[i].split(" ");
        if (comand[0] === "COUNT") {
            let from = parseInt(comand[1]);
            let to = parseInt(comand[2]);

            if (from === 1 && to === halfLen) {
                res.push(sumsArr[0]);
                continue;
            }
            if ((from - halfLen) === 1 && to === clientsArr.length) {
                res.push(sumsArr[1]);
                continue;
            }
            let fromSum;
            let toSum;
            let fromIndex = (from > halfLen ? from - halfLen : from) - 1;
            let toIndex = (to > halfLen ? to - halfLen : to) - 1;
            if ((to - 1) < halfLen) {
                res.push(sumsArr[0]
                    - multiArr[0].slice(0, fromIndex).reduce((acc, cur) => acc + parseInt(cur), 0)
                    - multiArr[0].slice(toIndex+1).reduce((acc, cur) => acc + parseInt(cur), 0));
                continue;
            }
            if (from > halfLen) {
                res.push(sumsArr[1]
                    - multiArr[1].slice(0, fromIndex).reduce((acc, cur) => acc + parseInt(cur), 0)
                    - multiArr[1].slice(toIndex+1).reduce((acc, cur) => acc + parseInt(cur), 0));
                continue;
            }

            let arrIndexFrom = from <= halfLen ? 0 : 1;
            let fromSubArr = multiArr[arrIndexFrom];
            if (from === 1 && to > halfLen) {
                fromSum = sumsArr[0];
            }
            else if ((fromSubArr.length - fromIndex + 1) <= fromSubArr.length/2) {
                fromSum = fromSubArr.slice(fromIndex).reduce((acc, cur) => acc + parseInt(cur), 0);
            }
            else {
                fromSum = sumsArr[arrIndexFrom] - fromSubArr.slice(0, fromIndex).reduce((acc, cur) => acc + parseInt(cur), 0);
            }
            let arrIndexTo = to > halfLen ? 1 : 0;
            let toSubArr = multiArr[arrIndexTo];
            if (from < halfLen && to === clientsArr.length) {
                toSum = sumsArr[1];
            }
            else if ((toSubArr.length - toIndex) >= toSubArr.length/2) {
                toSum = toSubArr.slice(0, toIndex+1).reduce((acc, cur) => acc + parseInt(cur), 0);
            }
            else {
                toSum = sumsArr[arrIndexTo] - toSubArr.slice(toIndex+1).reduce((acc, cur) => acc + parseInt(cur), 0);
            }
            res.push(fromSum + toSum);
        }
        else {
            let comandAction = comand[0] === "ENTER" ? 1 : (-1);
            let enterIndex = parseInt(comand[1]);
            let subArrIndex = enterIndex > halfLen ? 1 : 0;
            let subSubArrIndex = (subArrIndex === 1 ? enterIndex - halfLen : enterIndex) - 1;
            multiArr[subArrIndex][subSubArrIndex] = parseInt(multiArr[subArrIndex][subSubArrIndex]) + comandAction;
            sumsArr[subArrIndex] = sumsArr[subArrIndex] + comandAction;
        }
    }
    // res.forEach(i => console.log(i))
}

let dataToProcess = "20000\n"
for (let j = 0; j < 20000; j++) {
	dataToProcess+=randomInteger(1, 1000000) + " ";
}
dataToProcess = dataToProcess.slice(0, -1) + "\n20000";
for (let i = 0; i < 20000; i++) {
	let one = randomInteger(1, 10);
	let two = randomInteger(1, 10);
	dataToProcess += "\nCOUNT " + Math.min(one, two) + " " + Math.max(one, two) + "\nENTER " + randomInteger(1, 10) + "\nLEAVE " + randomInteger(1, 10); 
}

function randomInteger(min, max) {
  // получить случайное число от (min-0.5) до (max+0.5)
  let rand = min - 0.5 + Math.random() * (max - min + 1);
  return Math.round(rand);
}
// console.log(dataToProcess);


console.time('star');
let res = processData(dataToProcess);
console.timeEnd('star');