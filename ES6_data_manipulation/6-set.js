export default function setFromArray(array) {
  return array.reduce((acc, curr) => {
    return acc.add(curr);
  }, new Set());
}
