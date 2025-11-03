export default function hasValuesFromArray(set, array) {
  return array.reduce((acc, cur) => acc && set.has(cur), true);
}
