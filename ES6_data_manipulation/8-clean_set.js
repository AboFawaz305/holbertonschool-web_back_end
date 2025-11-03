/**
 * @param {Set} set
 * @param {string} pre
 *
 * @returns {string}
 */
export default function cleanSet(set, pre) {
  if (!pre) pre = "";
  if (typeof pre !== "string") return "";
  let result = "";
  for (const cur of set) {
    if (pre !== "" && cur.startsWith(pre)) {
      result += "-" + cur.slice(pre.length);
    }
  }
  return result.slice(1);
}
