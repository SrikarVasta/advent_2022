const fs = require("fs");

async function get_values() {
  let x;
  await fs.readFile("advent_3.in", async (err, data) => {
    if (err) throw err;
    x = await data.toString().split("\n");
    findCommonItems(x);
  });
}
get_values();
function findCommonItems(rucksacks) {
  let commonItems = [];
  let prioritySum = 0;
  for (let i = 0; i < rucksacks.length; i++) {
    let rucksack = rucksacks[i];
    let firstCompartment = rucksack.slice(0, rucksack.length / 2);
    let secondCompartment = rucksack.slice(rucksack.length / 2);
    let commonItemType = "";
    for (let j = 0; j < firstCompartment.length; j++) {
      if (secondCompartment.includes(firstCompartment[j])) {
        commonItemType = firstCompartment[j];
        break;
      }
    }
    commonItems.push(commonItemType);
    if (
      commonItemType.charCodeAt(0) >= 97 &&
      commonItemType.charCodeAt(0) <= 122
    ) {
      prioritySum += commonItemType.charCodeAt(0) - 96;
    } else if (
      commonItemType.charCodeAt(0) >= 65 &&
      commonItemType.charCodeAt(0) <= 90
    ) {
      prioritySum += commonItemType.charCodeAt(0) - 38;
    }
  }
  console.log(commonItems);
  console.log("priority sum", prioritySum);
}

let rucksacks = [
  "vJrwpWtwJgWrhcsFMMfFFhFp",
  "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
  "PmmdzqPrVvPwwTWBwg",
  "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
  "ttgJtRGJQctTZtZT",
  "CrZsJsPPZsGzwwsLwLmpwMDw",
];
