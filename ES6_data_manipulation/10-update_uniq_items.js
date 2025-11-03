export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw new Error("Cannot process");
  for (const v of map.entries()) if (v[1] == 1) map.set(v[0], 100);
  return map;
}
