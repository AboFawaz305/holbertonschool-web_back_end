export default function getStudentsByLocation(stds, location) {
	return stds.filter((e) => e.location === location)
}
