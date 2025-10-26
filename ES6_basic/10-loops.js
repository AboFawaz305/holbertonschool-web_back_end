export default function appendToEachArrayValue(array, appendString) {
  const res = [];
  for (const e of array) {
    res.push(appendString + e);
  }

  return res;
}
