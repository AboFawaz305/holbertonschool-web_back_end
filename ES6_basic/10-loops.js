export default function appendToEachArrayValue(array, appendString) {
  const result = []
  for (var value of array) {
    result.push(appendString + value);
  }
  for (var e of result)
    array.push(e)
  return result;
}
